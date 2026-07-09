import os
import random
import time
from datetime import datetime, timezone

import requests
from flask import Blueprint, jsonify, request

status_bp = Blueprint("status", __name__)

UPTIMEROBOT_API_KEY = os.environ.get("UPTIMEROBOT_API_KEY")

UPTIMEROBOT_STATUS_MAP = {
    0: "paused",
    1: "not_checked",
    2: "up",
    8: "seems_down",
    9: "down",
}

# ==========================================================
# SIMPLE IN-MEMORY CACHE TO PROTECT API LIMITS
# ==========================================================
STATUS_CACHE = {
    "data": None,
    "cached_at": 0,
    "monitor_id": None
}
CACHE_TTL_SECONDS = 60

# ==========================================================
# STATUS MESSAGES
# ==========================================================

UP_MESSAGES = [
    "◆ CritCal is online and judging builds.",
    "✦ Lunar signal stable. CritCal is operational.",
    "✓ All systems nominal. Ready for another build.",
    "⚡ Servers are healthy and responding.",
    "☾ CritCal is standing by.",
]

DEGRADED_MESSAGES = [
    "◇ Lunar interference detected. Some services may be slower.",
    "⚠ Partial outage detected.",
    "⚡ CritCal is operational, but not everything is healthy.",
]

DOWN_MESSAGES = [
    "✖ CritCal has lost its lunar signal.",
    "☠ CritCal is currently offline.",
    "⚠ No response from CritCal.",
    "◇ Servers appear to be unavailable.",
]

PAUSED_MESSAGES = [
    "❚❚ Monitoring is currently paused.",
    "◇ Status monitoring has been disabled.",
]

UNKNOWN_MESSAGES = [
    "❔ Unable to determine CritCal's status.",
    "◇ Status information is unavailable.",
]

# ==========================================================
# HELPERS
# ==========================================================


def format_timestamp(unix_time):
    """
    Returns both unix and ISO timestamp.
    """
    if not unix_time:
        return None

    try:
        unix_time = int(unix_time)
        return {
            "unix": unix_time,
            "utc": datetime.fromtimestamp(
                unix_time,
                tz=timezone.utc
            ).isoformat()
        }
    except Exception:
        return None


def parse_ratio(ratio_string):
    """
    Converts custom uptime ratios into a dict safely.
    """
    if not ratio_string:
        return {"24h": None, "7d": None, "30d": None}

    values = ratio_string.split("-")
    
    # Pad out out-of-bounds lists safely to prevent IndexErrors
    while len(values) < 3:
        values.append(None)

    return {
        "24h": values[0],
        "7d": values[1],
        "30d": values[2],
    }


def build_summary(monitors):
    up = sum(m["status_code"] == 2 for m in monitors)
    down = sum(m["status_code"] == 9 for m in monitors)
    paused = sum(m["status_code"] == 0 for m in monitors)
    unknown = len(monitors) - up - down - paused

    total = len(monitors)
    health = round((up / total) * 100, 1) if total > 0 else 0.0

    return {
        "total": total,
        "up": up,
        "down": down,
        "paused": paused,
        "unknown": unknown,
        "overall_health": health,
    }


def choose_message(summary):
    if summary["total"] == 0:
        return random.choice(UNKNOWN_MESSAGES)
    if summary["down"] == summary["total"]:
        return random.choice(DOWN_MESSAGES)
    if summary["down"] > 0:
        return random.choice(DEGRADED_MESSAGES)
    if summary["paused"] == summary["total"]:
        return random.choice(PAUSED_MESSAGES)
    return random.choice(UP_MESSAGES)


# ==========================================================
# UPTIMEROBOT FETCH
# ==========================================================


def get_uptime_status(monitor_id=None):
    payload = {
        "api_key": UPTIMEROBOT_API_KEY,
        "format": "json",
        "logs": 1,
        "logs_limit": 5,
        "response_times": 1,
        "response_times_limit": 10,
        "response_times_average": 1,
        "custom_uptime_ratios": "1-7-30",
        "all_time_uptime_ratio": 1,
    }

    if monitor_id:
        payload["monitors"] = str(monitor_id)

    response = requests.post(
        "https://api.uptimerobot.com/v2/getMonitors",
        data=payload,
        headers={
            "Content-Type": "application/x-www-form-urlencoded",
            "Cache-Control": "no-cache",
        },
        timeout=10,
    )
    response.raise_for_status()
    data = response.json()

    if data.get("stat") != "ok":
        raise ValueError(
            data.get("error", {}).get(
                "message",
                "Unknown UptimeRobot error."
            )
        )

    monitors = []
    for monitor in data.get("monitors", []):
        status_code = monitor.get("status")
        monitor_data = {
            "id": monitor.get("id"),
            "friendly_name": monitor.get("friendly_name"),
            "url": monitor.get("url"),
            "type": monitor.get("type"),
            "status": UPTIMEROBOT_STATUS_MAP.get(status_code, "unknown"),
            "status_code": status_code,
            "check_interval_seconds": monitor.get("interval"),
            "created": format_timestamp(monitor.get("create_datetime")),
            "last_check": format_timestamp(monitor.get("last_check_date")),
            "uptime": {
                **parse_ratio(monitor.get("custom_uptime_ratio")),
                "all_time": monitor.get("all_time_uptime_ratio"),
            },
            "average_response_ms": monitor.get("average_response_time"),
            "recent_response_times": monitor.get("response_times", []),
            "recent_logs": monitor.get("logs", []),
        }
        monitors.append(monitor_data)

    summary = build_summary(monitors)

    return {
        "generated_at": format_timestamp(int(datetime.now(timezone.utc).timestamp())),
        "message": choose_message(summary),
        "summary": summary,
        "monitors": monitors,
    }


# ==========================================================
# STATUS ROUTE
# ==========================================================

@status_bp.route("/status", methods=["GET"])
def status():
    """
    Returns CritCal's current uptime information with 60s fallback caching.
    """
    monitor_id = request.args.get("id")

    if monitor_id is not None and not monitor_id.isdigit():
        return jsonify({
            "success": False,
            "error": "'id' must be a numeric UptimeRobot monitor ID."
        }), 400

    current_time = time.time()

    # If cache is valid for this specific query configuration, return it immediately
    if (
        STATUS_CACHE["data"] is not None
        and (current_time - STATUS_CACHE["cached_at"]) < CACHE_TTL_SECONDS
        and STATUS_CACHE["monitor_id"] == monitor_id
    ):
        return jsonify(STATUS_CACHE["data"]), 200

    try:
        result = get_uptime_status(monitor_id)
        summary = result["summary"]

        if summary["down"] == summary["total"] and summary["total"] > 0:
            overall_status = "offline"
        elif summary["down"] > 0:
            overall_status = "degraded"
        elif summary["paused"] == summary["total"] and summary["total"] > 0:
            overall_status = "paused"
        elif summary["up"] == summary["total"] and summary["total"] > 0:
            overall_status = "online"
        else:
            overall_status = "unknown"

        response_payload = {
            "success": True,
            "service": "CritCal",
            "version": "status-v1",
            "status": overall_status,
            "generated_at": result["generated_at"],
            "message": result["message"],
            "summary": result["summary"],
            "monitors": result["monitors"]
        }

        # Update cache values
        STATUS_CACHE["data"] = response_payload
        STATUS_CACHE["cached_at"] = current_time
        STATUS_CACHE["monitor_id"] = monitor_id

        return jsonify(response_payload), 200

    except requests.Timeout:
        return jsonify({
            "success": False,
            "status": "error",
            "error": "Timed out while contacting UptimeRobot."
        }), 504
    except requests.ConnectionError:
        return jsonify({
            "success": False,
            "status": "error",
            "error": "Unable to connect to UptimeRobot."
        }), 502
    except requests.RequestException as e:
        return jsonify({
            "success": False,
            "status": "error",
            "error": f"Request failed: {str(e)}"
        }), 502
    except ValueError as e:
        return jsonify({
            "success": False,
            "status": "error",
            "error": str(e)
        }), 502
    except Exception as e:
        return jsonify({
            "success": False,
            "status": "error",
            "error": str(e)
        }), 500


# ==========================================================
# HEALTHCHECK
# ==========================================================

@status_bp.route("/health", methods=["GET"])
def health():
    """
    Lightweight endpoint for Render health checks.
    """
    return jsonify({
        "success": True,
        "status": "healthy",
        "service": "CritCal",
    }), 200
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
  
