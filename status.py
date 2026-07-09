import os
import requests
from flask import Blueprint, jsonify

status_bp = Blueprint("status", __name__)

# Prefer an environment variable so the key isn't hardcoded in source.
# The literal fallback below should be removed once you've rotated the key
# (it was shared in plaintext, so treat it as compromised).
UPTIMEROBOT_API_KEY = os.environ.get(
    "UPTIMEROBOT_API_KEY", "u3623262-124c05e69f6301a904686336"
)

UPTIMEROBOT_STATUS_MAP = {
    0: "paused",
    1: "not checked yet",
    2: "up",
    8: "seems down",
    9: "down",
}


def get_uptime_status():
    """Fetch monitor data from UptimeRobot and return a simplified dict."""
    response = requests.post(
        "https://api.uptimerobot.com/v2/getMonitors",
        data={
            "api_key": UPTIMEROBOT_API_KEY,
            "format": "json",
            "logs": 0,
            "response_times": 0,
        },
        headers={
            "Content-Type": "application/x-www-form-urlencoded",
            "Cache-Control": "no-cache",
        },
        timeout=10,
    )
    response.raise_for_status()
    data = response.json()

    if data.get("stat") != "ok":
        raise ValueError(data.get("error", {}).get("message", "Unknown UptimeRobot API error"))

    monitors = []
    for m in data.get("monitors", []):
        code = m.get("status")
        monitors.append({
            "id": m.get("id"),
            "friendly_name": m.get("friendly_name"),
            "url": m.get("url"),
            "status": UPTIMEROBOT_STATUS_MAP.get(code, "unknown"),
            "status_code": code,
        })

    return {
        "monitors": monitors,
        "count": len(monitors),
        "up": sum(1 for m in monitors if m["status_code"] == 2),
        "down": sum(1 for m in monitors if m["status_code"] == 9),
    }


@status_bp.route("/status")
def status():
    try:
        result = get_uptime_status()
    except requests.RequestException as e:
        return jsonify({"error": f"Failed to reach UptimeRobot: {e}"}), 502
    except ValueError as e:
        return jsonify({"error": str(e)}), 502

    return jsonify(result), 200
  
