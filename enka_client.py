"""
Thin client around the public Enka.Network API.

Enka pulls whatever the player has showcased in-game — if their showcase
is private/empty, or the requested character isn't shown, we surface a
clear error rather than guessing.
"""
import time
import requests

ENKA_BASE = "https://enka.network/api/uid"
CHAR_STORE_URL = "https://raw.githubusercontent.com/EnkaNetwork/API-docs/master/store/characters.json"
LOC_STORE_URL = "https://raw.githubusercontent.com/EnkaNetwork/API-docs/master/store/loc.json"

HEADERS = {
    # Enka asks API consumers to set a distinct User-Agent so they can
    # track/troubleshoot usage. Change the contact info if you want.
    "User-Agent": "GenshinBuildRaterBot/1.0 (Discord bot via BDFD)"
}

FIGHT_PROP_MAP = {
    "20": "crit_rate",
    "22": "crit_dmg",
    "23": "energy_recharge",
    "28": "elemental_mastery",
    "2000": "hp",
    "2001": "atk",
    "2002": "def",
}

APPEND_PROP_MAP = {
    "FIGHT_PROP_CRITICAL": "crit_rate",
    "FIGHT_PROP_CRITICAL_HURT": "crit_dmg",
    "FIGHT_PROP_CHARGE_EFFICIENCY": "energy_recharge",
    "FIGHT_PROP_ELEMENT_MASTERY": "elemental_mastery",
    "FIGHT_PROP_ATTACK_PERCENT": "atk_percent",
    "FIGHT_PROP_ATTACK": "atk_flat",
    "FIGHT_PROP_HP_PERCENT": "hp_percent",
    "FIGHT_PROP_DEFENSE_PERCENT": "def_percent",
}

_char_name_cache = {"map": None, "fetched_at": 0}
CACHE_TTL_SECONDS = 6 * 60 * 60  # refresh character name table every 6h


def _load_character_names():
    """
    Builds {avatarId(str): "English Name"} from Enka's own reference data.
    Falls back gracefully (returns {}) if the format changes or fetch fails
    -- the caller will just display the raw avatarId instead of a name.
    """
    now = time.time()
    if _char_name_cache["map"] is not None and now - _char_name_cache["fetched_at"] < CACHE_TTL_SECONDS:
        return _char_name_cache["map"]

    try:
        chars = requests.get(CHAR_STORE_URL, headers=HEADERS, timeout=10).json()
        loc = requests.get(LOC_STORE_URL, headers=HEADERS, timeout=10).json()

        # loc.json is keyed by language, each containing hash -> text
        en_loc = loc.get("en", loc)

        name_map = {}
        for avatar_id, data in chars.items():
            name_hash = str(data.get("NameTextMapHash", ""))
            name = en_loc.get(name_hash)
            if name:
                name_map[str(avatar_id)] = name

        if name_map:
            _char_name_cache["map"] = name_map
            _char_name_cache["fetched_at"] = now
            return name_map
    except Exception:
        pass

    return _char_name_cache["map"] or {}


def fetch_profile(uid):
    """Raises ValueError with a user-friendly message on failure."""
    url = f"{ENKA_BASE}/{uid}/"
    try:
        resp = requests.get(url, headers=HEADERS, timeout=10)
    except requests.RequestException as e:
        raise ValueError(f"Could not reach Enka.Network: {e}")

    if resp.status_code == 400:
        raise ValueError("That UID doesn't look valid.")
    if resp.status_code == 404:
        raise ValueError("No player found with that UID.")
    if resp.status_code == 424:
        raise ValueError("Genshin servers are under maintenance right now — try again later.")
    if resp.status_code == 429:
        raise ValueError("Rate-limited by Enka.Network — try again in a minute.")
    if resp.status_code != 200:
        raise ValueError(f"Enka.Network returned an unexpected error ({resp.status_code}).")

    data = resp.json()
    if "avatarInfoList" not in data or not data["avatarInfoList"]:
        raise ValueError(
            "This player's Character Showcase is empty or private. "
            "They need to showcase the character in-game first."
        )
    return data


def _extract_substats(equip_list):
    totals = {}
    for equip in equip_list:
        if "reliquary" not in equip:
            continue  # this equip slot is the weapon, skip
        flat = equip.get("flat", {})
        for sub in flat.get("reliquarySubstats", []):
            key = APPEND_PROP_MAP.get(sub.get("appendPropId"))
            if key:
                totals[key] = totals.get(key, 0) + sub.get("statValue", 0)
        # Main stat can also matter (e.g. EM flower is rare but possible)
        main = flat.get("reliquaryMainstat", {})
        main_key = APPEND_PROP_MAP.get(main.get("mainPropId"))
        if main_key and main_key != "atk_flat":  # avoid double counting flat ATK weapon-like mains
            totals[main_key] = totals.get(main_key, 0) + main.get("statValue", 0)
    return totals


def get_character_build(uid, character_name=None):
    """
    Returns a normalized dict ready for scoring.rate_build(), plus the
    resolved character name and a list of other showcased characters if
    the requested one wasn't found (helps the bot give a useful error).
    """
    data = fetch_profile(uid)
    name_map = _load_character_names()

    avatars = data["avatarInfoList"]
    showcased_names = []
    match = None

    for avatar in avatars:
        avatar_id = str(avatar["avatarId"])
        resolved_name = name_map.get(avatar_id, f"Character #{avatar_id}")
        showcased_names.append(resolved_name)
        if character_name and resolved_name.lower() == character_name.lower():
            match = avatar
        elif not character_name and match is None:
            match = avatar  # default to first showcased character

    if match is None:
        raise ValueError(
            f"'{character_name}' isn't in this player's showcase. "
            f"Showcased characters: {', '.join(showcased_names)}"
        )

    resolved_name = name_map.get(str(match["avatarId"]), f"Character #{match['avatarId']}")
    fight_props = match.get("fightPropMap", {})

    stats = {}
    for prop_id, key in FIGHT_PROP_MAP.items():
        value = fight_props.get(prop_id, 0)
        if key in ("crit_rate", "crit_dmg", "energy_recharge"):
            value *= 100  # Enka returns these as fractions (0.65 -> 65%)
        stats[key] = value

    substat_totals = _extract_substats(match.get("equipList", []))

    return {
        "character": resolved_name,
        "crit_rate": round(stats.get("crit_rate", 0), 2),
        "crit_dmg": round(stats.get("crit_dmg", 0), 2),
        "atk": round(stats.get("atk", 0), 2),
        "hp": round(stats.get("hp", 0), 2),
        "defense": round(stats.get("def", 0), 2),
        "elemental_mastery": round(stats.get("elemental_mastery", 0), 2),
        "energy_recharge": round(stats.get("energy_recharge", 0), 2),
        "substat_totals": substat_totals,
      }
      
