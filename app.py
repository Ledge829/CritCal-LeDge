from flask import Flask, request, jsonify
from scoring import rate_build
from enka_client import get_character_build

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


@app.route("/rate/manual", methods=["POST"])
def rate_manual():
    body = request.get_json(silent=True)
    if not body:
        return jsonify({"error": "Missing or invalid JSON body."}), 400

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
            character_scaling=body.get("character_scaling", "atk"),
        )
        return jsonify(result), 200
    except (TypeError, ValueError) as e:
        return jsonify({"error": f"Invalid stat values: {e}"}), 400


@app.route("/rate/uid", methods=["POST"])
def rate_uid():
    body = request.get_json(silent=True)
    if not body or "uid" not in body:
        return jsonify({"error": "Missing 'uid' field."}), 400

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
            character_scaling=body.get("character_scaling", "atk"),
        )
        result["source"] = "enka.network live showcase"
        return jsonify(result), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
