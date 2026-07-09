from flask import Flask, request, jsonify
from scoring import rate_build
from enka_client import get_character_build
from status import status_bp

...
app = Flask(__name__)
app.register_blueprint(status_bp)

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "status": "online",
        "endpoints": {
            "POST /rate/manual": "Rate a build from manually entered stats.",
            "POST /rate/uid": "Rate a build pulled live from Enka.Network via UID.",
            "GET /ping": "Health check (used by UptimeRobot to keep the service awake).",
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

    try:
        result = rate_build(
            character=body["character"],
            crit_rate=float(body["crit_rate"]),
            crit_dmg=float(body["crit_dmg"]),
            atk=float(body["atk"]),
            hp=float(body.get("hp", 0)),
            defense=float(body.get("def", 0)),
            elemental_mastery=float(body.get("elemental_mastery", 0)),
            energy_recharge=float(body.get("energy_recharge", 100)),
            substat_totals=body.get("substats", {}),
            character_scaling=body.get("character_scaling"),
            ideal_crit_ratio=float(body["ideal_crit_ratio"]) if "ideal_crit_ratio" in body else None,
            include_relative_damage=bool(body.get("include_relative_damage", False)),
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
        build = get_character_build(
            uid=str(body["uid"]),
            character_name=body.get("character"),
        )
        result = rate_build(
            character=build["character"],
            crit_rate=build["crit_rate"],
            crit_dmg=build["crit_dmg"],
            atk=build["atk"],
            hp=build["hp"],
            defense=build["defense"],
            elemental_mastery=build["elemental_mastery"],
            energy_recharge=build["energy_recharge"],
            substat_totals=build["substat_totals"],
            character_scaling=body.get("character_scaling"),
            ideal_crit_ratio=float(body["ideal_crit_ratio"]) if "ideal_crit_ratio" in body else None,
            include_relative_damage=bool(body.get("include_relative_damage", False)),
        )
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

    if "error" in result:
        return jsonify(result), 400

    result["source"] = "enka.network live showcase"
    return jsonify(result), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
  
