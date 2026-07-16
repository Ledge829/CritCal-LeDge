from flask import Flask, request, jsonify
from flask_cors import CORS
from scoring import rate_build, parse_artifact_sets_text, parse_weapon_text
from enka_client import fetch_character
from status import status_bp

app = Flask(__name__)
app.register_blueprint(status_bp)

CORS(app, resources={r"/*": {"origins": "*"}})

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
            "error": "Missing or invalid JSON body.",
            "raw_body_received": request.get_data(as_text=True)
        }), 400

    required = ["character", "crit_rate", "crit_dmg", "atk"]
    missing = [f for f in required if f not in body]
    if missing:
        return jsonify({"error": f"Missing required fields: {', '.join(missing)}"}), 400

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
            "error": "'weapon' must be a string (e.g. \"Staff of Homa r1\") "
                     "or an object, e.g. {\"name\": \"...\", \"refinement\": 1}"
        }), 400

    # Optional artifact sets: either a list of {"name": "...", "count": 1-5}
    # objects, or a single free-text "artifacts" string like "4pc Golden
    # Troupe" / "2pc Emblem of Severed Fate, 2pc Noblesse Oblige". The
    # plain-text "artifacts" field is checked first since it's the easier
    # path for quick slash-command use; "artifact_sets" remains available
    # for anything sending structured data directly.
    artifacts_text = body.get("artifacts")
    if artifacts_text is not None and not isinstance(artifacts_text, str):
        return jsonify({"error": "'artifacts' must be a string, e.g. \"4pc Golden Troupe\""}), 400

    artifact_sets = body.get("artifact_sets")
    if artifact_sets is not None:
        if not isinstance(artifact_sets, list) or not all(isinstance(s, dict) for s in artifact_sets):
            return jsonify({"error": "'artifact_sets' must be a list of objects, e.g. [{\"name\": \"...\", \"count\": 4}]"}), 400

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
            "error": "Could not parse a JSON body from the request.",
            "raw_body_received": request.get_data(as_text=True)
        }), 400
    if "uid" not in body:
        return jsonify({"error": "JSON body parsed fine, but no 'uid' field was in it.", "body_received": body}), 400

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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    
