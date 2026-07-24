from flask import Flask, request, jsonify
from flask_cors import CORS
from scoring import rate_build, parse_artifact_sets_text, parse_weapon_text
from enka_client import fetch_character, fetch_all_characters
from characters import get_all_characters, get_character_config, splash_from_portrait
from display_names import display_name
from item_catalog import WEAPONS, ARTIFACT_SETS
from status import status_bp

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 1 * 1024 * 1024  # Limit requests to 1MB
app.register_blueprint(status_bp)

# CORS: without this, a browser calling this API from critcal.vercel.app
# (or any other site) gets silently blocked by the browser itself before
# the request even reaches Flask -- this is a browser-side security rule,
# not something wrong with the request. BDFD never hit this because it's
# a server-to-server call, not a browser one, so it never came up before.
#
# Wide open (*) is fine here: this API has no auth/cookies/user accounts,
# every endpoint is public read-only scoring, so there's nothing a
# malicious site could steal by calling it cross-origin. If that ever
# changes (logins, saved builds, etc.), swap "*" for an explicit list of
# allowed origins, e.g. origins=["https://critcal.vercel.app"].
CORS(app, resources={r"/*": {"origins": "*"}})

# [build] 2026-07-24 — splash art integration + API cleanup


@app.route("/")
def home():
    return jsonify({
        "status": "online",
        "endpoints": {
            "POST /rate/manual": "Rate a build from manually entered stats.",
            "POST /rate/uid": "Rate a build pulled live from Enka.Network via UID.",
            "GET /ping": "Health check (used by UptimeRobot to keep the service awake).",
            "GET /status": "Live uptime/monitor status.",
        }
    })


@app.route("/ping")
def ping():
    return "OK", 200


@app.route("/characters", methods=["GET"])
def list_characters():
    """
    Lists every character CritCal currently supports, with a display
    name plus their element/rarity/region/roles metadata (from
    characters.py's new schema fields) -- powers the website's browse
    page and the analyze form's autocomplete. Sorted alphabetically by
    display name so it reads naturally in a UI without extra client-side
    sorting logic.
    """
    keys = [k for k in get_all_characters() if k != "unknown"]
    characters_list = []
    for key in keys:
        config = get_character_config(key)
        characters_list.append({
            "key": key,
            "name": display_name(key),
            "element": config.get("element"),
            "rarity": config.get("rarity"),
            "region": config.get("region"),
            "roles": config.get("roles", []),
            "weapon_type": config.get("weapon_type"),
            "portrait": config.get("portrait"),
            "splash": splash_from_portrait(config.get("portrait")),
        })
    characters_list.sort(key=lambda c: c["name"])
    return jsonify({"characters": characters_list, "count": len(characters_list)})


@app.route("/stats", methods=["GET"])
def get_stats():
    """Returns aggregate counts for characters, weapons, and artifact sets."""
    char_count = len([k for k in get_all_characters() if k != "unknown"])
    weapon_count = len(WEAPONS)
    five_star_count = sum(1 for _, (_, is5) in WEAPONS.items() if is5)
    set_count = len(ARTIFACT_SETS)
    modern_set_count = sum(1 for _, modern in ARTIFACT_SETS.items() if modern)
    return jsonify({
        "characters": char_count,
        "weapons": weapon_count,
        "weapons_five_star": five_star_count,
        "artifact_sets": set_count,
        "artifact_sets_modern": modern_set_count,
    })
@app.route("/debug/echo", methods=["POST"])
def debug_echo():
    """
    Diagnostic endpoint: shows exactly what the server received, regardless
    of whether it parses as JSON. Point BDFD or reqbin at this if a real
    endpoint is behaving oddly -- it'll show you the raw body, headers,
    and whether JSON parsing succeeded, so mismatches are obvious.
    """
    return jsonify({
        "content_type_header": request.content_type,
        "raw_body": request.get_data(as_text=True),
        "parsed_json_strict": request.get_json(silent=True),
        "parsed_json_forced": request.get_json(silent=True, force=True),
    }), 200


@app.route("/rate/manual", methods=["POST"])
def rate_manual():
    # force=True parses the body as JSON even if Content-Type isn't set
    # exactly to application/json -- some HTTP clients (BDFD, reqbin) are
    # inconsistent about that header.
    body = request.get_json(silent=True, force=True)
    if not body:
        return jsonify({
            "error": "Couldn't parse your request — make sure you're sending valid JSON.",
            "raw_body_received": request.get_data(as_text=True)
        }), 400

    required = ["character", "crit_rate", "crit_dmg", "atk"]
    missing = [f for f in required if f not in body]
    if missing:
        return jsonify({"error": f"Missing some required info: {', '.join(missing)}"}), 400

    # ------------------------------------------------------------------
    # QUICK-INPUT SUPPORT
    #
    # BDFD slash commands are painful to fill out with nested/structured
    # fields (artifact_set_1_name, piece_1, artifact_set_2_name, piece_2,
    # weapon.name, weapon.refinement...). So both `weapon` and
    # `artifact_sets` now also accept a single plain-text string:
    #
    #   "weapon": "Staff of Homa r1"
    #   "artifacts": "4pc Golden Troupe"
    #   "artifacts": "2pc Emblem of Severed Fate, 2pc Noblesse Oblige"
    #
    # The old structured formats (weapon as an object, artifact_sets as a
    # list of {"name","count"} objects) still work exactly as before --
    # this is purely additive, nothing already wired in BDFD breaks.
    # ------------------------------------------------------------------

    # Optional weapon: either {"name": "...", "refinement": 1-5}, or a
    # single free-text string like "Staff of Homa r1".
    weapon = body.get("weapon")
    if isinstance(weapon, str):
        weapon = parse_weapon_text(weapon)
    elif weapon is not None and not isinstance(weapon, dict):
        return jsonify({
            "error": "'weapon' should be plain text like \"Staff of Homa r1\" or an object with \"name\" and \"refinement\"."
        }), 400

    artifacts_text = body.get("artifacts")
    if artifacts_text is not None and not isinstance(artifacts_text, str):
        return jsonify({"error": "'artifacts' should be plain text like \"4pc Golden Troupe\"."}), 400

    artifact_sets = body.get("artifact_sets")
    if artifact_sets is not None:
        if not isinstance(artifact_sets, list) or not all(isinstance(s, dict) for s in artifact_sets):
            return jsonify({"error": "'artifact_sets' should be a list of objects with \"name\" and \"count\"."}), 400

    if artifacts_text and not artifact_sets:
        artifact_sets = parse_artifact_sets_text(artifacts_text)

    def _optional_float(key, default):
        # Treats a missing key AND a blank string as "not provided" and
        # falls back to default, instead of raising. BDFD (and similar
        # no-code bot builders) often quote every field as a JSON string
        # for safety, so an unfilled optional slash-command option comes
        # through as "" rather than being omitted entirely -- without
        # this, float("") would raise and reject an otherwise-valid
        # request just because the user skipped an optional stat.
        value = body.get(key, default)
        if value is None or (isinstance(value, str) and value.strip() == ""):
            return default
        return float(value)

    try:
        result = rate_build(
            character=body["character"],
            crit_rate=float(body["crit_rate"]),
            crit_dmg=float(body["crit_dmg"]),
            atk=float(body["atk"]),
            hp=_optional_float("hp", 0),
            defense=_optional_float("def", 0),
            elemental_mastery=_optional_float("elemental_mastery", 0),
            energy_recharge=_optional_float("energy_recharge", 100),
            substat_totals=body.get("substats", {}),
            character_scaling=body.get("character_scaling") or None,
            ideal_crit_ratio=_optional_float("ideal_crit_ratio", None),
            include_relative_damage=bool(body.get("include_relative_damage", False)),
            weapon=weapon,
            artifact_sets=artifact_sets,
        )
    except (TypeError, ValueError) as e:
        return jsonify({"error": f"Invalid stat values: {e}"}), 400

    # rate_build() returns {"error": ...} internally instead of raising for
    # bad numeric input -- must check for that explicitly or a malformed
    # request would silently return HTTP 200 with a broken/incomplete body.
    if "error" in result:
        return jsonify(result), 400

    return jsonify(result), 200


@app.route("/rate/uid", methods=["POST"])
def rate_uid():
    body = request.get_json(silent=True, force=True)
    if not body:
        return jsonify({
            "error": "Couldn't read your request — send JSON with a \"uid\" field and optionally a \"character\" name.",
            "raw_body_received": request.get_data(as_text=True)
        }), 400
    if "uid" not in body:
        return jsonify({"error": "Your request parsed as JSON but doesn't have a \"uid\" field — make sure you're sending one.", "body_received": body}), 400

    try:
        build = fetch_character(
            uid=str(body["uid"]),
            character_name=body.get("character"),
        )
        stats = build["stats"]
        result = rate_build(
            character=build["character"],
            crit_rate=stats["crit_rate"],
            crit_dmg=stats["crit_dmg"],
            atk=stats["atk"],
            hp=stats["hp"],
            defense=stats["def"],
            elemental_mastery=stats["elemental_mastery"],
            energy_recharge=stats["energy_recharge"],
            substat_totals=build["substats"],
            character_scaling=body.get("character_scaling"),
            ideal_crit_ratio=float(body["ideal_crit_ratio"]) if "ideal_crit_ratio" in body else None,
            include_relative_damage=bool(body.get("include_relative_damage", False)),
            weapon=build["weapon"],
            artifact_sets=build["artifact_sets"],
        )
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

    if "error" in result:
        return jsonify(result), 400

    result["source"] = "enka.network live showcase"
    return jsonify(result), 200


@app.route("/uid/<uid>/showcase", methods=["GET"])
def uid_showcase(uid):
    """
    Returns every showcased character for a UID with a quick summary
    (grade, score, crit values, weapon/artifact tier) so the frontend
    can render a grid of mini-cards without calling /rate/uid N times.
    """
    try:
        characters = fetch_all_characters(uid)
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

    # Build a reverse lookup: Enka character name -> canonical key,
    # so we can attach portrait/element/rarity from characters.py.
    from display_names import DISPLAY_NAMES
    name_to_key = {}
    for key, dname in DISPLAY_NAMES.items():
        name_to_key[dname.lower()] = key
    # Also index canonical keys themselves (they match after .lower()).
    for key in get_all_characters():
        name_to_key[key.lower().replace("_", "").replace("-", "").replace(" ", "")] = key

    from characters import normalize_character, CHARACTER_ALIASES
    results = []
    for build in characters:
        char_name = build["character"]
        stats = build["stats"]

        # resolve canonical key for portrait/element/rarity
        normalized = char_name.lower().strip()
        alias_resolved = CHARACTER_ALIASES.get(normalized, normalized)
        canonical = name_to_key.get(normalized) or name_to_key.get(alias_resolved) or alias_resolved
        config = get_character_config(canonical) if canonical else {}

        try:
            result = rate_build(
                character=char_name,
                crit_rate=stats["crit_rate"],
                crit_dmg=stats["crit_dmg"],
                atk=stats["atk"],
                hp=stats["hp"],
                defense=stats["def"],
                elemental_mastery=stats["elemental_mastery"],
                energy_recharge=stats["energy_recharge"],
                substat_totals=build["substats"],
                weapon=build["weapon"],
                artifact_sets=build["artifact_sets"],
            )
        except (ValueError, TypeError):
            continue

        if "error" in result:
            # Skip characters that failed scoring (shouldn't normally happen).
            continue

        # Merge the full rating result with character metadata so
        # the frontend has everything it needs without extra API calls.
        result["portrait"] = config.get("portrait")
        result["splash"] = splash_from_portrait(config.get("portrait"))
        result["element"] = config.get("element")
        result["rarity"] = config.get("rarity")
        results.append(result)

    return jsonify({
        "uid": uid,
        "characters": results,
        "count": len(results),
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
