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
    """Returns both unix and ISO timestamp."""
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


def humanize_seconds_ago(unix_time):
    """'15 seconds ago' style string from a unix timestamp."""
    if not unix_time:
        return None
    try:
        delta = max(0, int(time.time() - int(unix_time)))
    except Exception:
        return None

    if delta < 60:
        return f"{delta} second{'s' if delta != 1 else ''} ago"
    minutes = delta // 60
    if minutes < 60:
        return f"{minutes} minute{'s' if minutes != 1 else ''} ago"
    hours = minutes // 60
    if hours < 24:
        return f"{hours} hour{'s' if hours != 1 else ''} ago"
    days = hours // 24
    return f"{days} day{'s' if days != 1 else ''} ago"


def humanize_interval(seconds):
    """'Every 5 minutes' style string from a check interval in seconds."""
    if not seconds:
        return None
    try:
        seconds = int(seconds)
    except Exception:
        return None

    if seconds % 60 == 0:
        minutes = seconds // 60
        return f"Every {minutes} minute{'s' if minutes != 1 else ''}"
    return f"Every {seconds} second{'s' if seconds != 1 else ''}"


def parse_ratio(ratio_string):
    """Converts custom uptime ratios into a dict safely."""
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


def derive_last_check(response_times):
    """
    UptimeRobot's API has no direct 'last checked' field -- the most
    reliable proxy is the newest entry in the response_times list, since
    each entry is timestamped per actual check.
    """
    if not response_times:
        return None
    newest = max(response_times, key=lambda r: r.get("datetime", 0))
    return newest.get("datetime")


def derive_average_response_ms(monitor, response_times):
    """
    Prefer UptimeRobot's own average_response_time field; if it's missing
    (e.g. averaging window too narrow, or no data in that window), fall
    back to averaging the raw response_times entries we already fetched.
    """
    avg = monitor.get("average_response_time")
    if avg not in (None, "", 0):
        try:
            return round(float(avg))
        except (TypeError, ValueError):
            pass

    if response_times:
        values = [float(r["value"]) for r in response_times if "value" in r]
        if values:
            return round(sum(values) / len(values))

    return None


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
        # In MINUTES -- 1 was too narrow and often returned nothing if
        # checks run every 5 minutes. 60 gives UptimeRobot's own average
        # over the last hour; we still fall back to a manual average of
        # the raw response_times below if this comes back empty.
        "response_times_average": 60,
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
        response_times = monitor.get("response_times", [])
        last_check_unix = derive_last_check(response_times)
        interval_seconds = monitor.get("interval")

        monitor_data = {
            "id": monitor.get("id"),
            "friendly_name": monitor.get("friendly_name"),
            "url": monitor.get("url"),
            "type": monitor.get("type"),
            "status": UPTIMEROBOT_STATUS_MAP.get(status_code, "unknown"),
            "status_code": status_code,
            "check_interval_seconds": interval_seconds,
            "check_interval_human": humanize_interval(interval_seconds),
            "created": format_timestamp(monitor.get("create_datetime")),
            "last_check": format_timestamp(last_check_unix),
            "last_check_ago": humanize_seconds_ago(last_check_unix),
            "uptime": {
                **parse_ratio(monitor.get("custom_uptime_ratio")),
                "all_time": monitor.get("all_time_uptime_ratio"),
            },
            "average_response_ms": derive_average_response_ms(monitor, response_times),
            "recent_response_times": response_times,
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

        # ---- Flattened top-level keys for BDFD (which doesn't support
        # nested/dot-notation lookups in $httpResult) -- mirrors the first
        # monitor's data as plain, non-nested keys.
        if result["monitors"]:
            primary = result["monitors"][0]
            response_payload.update({
                "monitor_id": primary["id"],
                "monitor_name": primary["friendly_name"],
                "monitor_url": primary["url"],
                "monitor_status": primary["status"],
                "monitor_uptime_24h": primary["uptime"]["24h"],
                "monitor_uptime_7d": primary["uptime"]["7d"],
                "monitor_uptime_30d": primary["uptime"]["30d"],
                "monitor_uptime_all_time": primary["uptime"]["all_time"],
                "monitor_avg_response_ms": primary["average_response_ms"],
                "monitor_last_check_ago": primary["last_check_ago"],
                "monitor_check_interval_human": primary["check_interval_human"],
            })

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
