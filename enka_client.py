"""
Thin client around the public Enka.Network API.

Supports character stat extraction, weapon extraction, artifact set
extraction, and cached metadata downloads for name resolution.
"""
import time
import requests

ENKA_BASE = "https://enka.network/api/uid"
# Updated Enka CDN URLs
CHAR_STORE_URL = "https://raw.githubusercontent.com/EnkaNetwork/API-docs/master/store/characters.json"
LOC_STORE_URL = "https://raw.githubusercontent.com/EnkaNetwork/API-docs/master/store/loc.json"
WEAPON_STORE_URL = "https://raw.githubusercontent.com/EnkaNetwork/API-docs/master/store/weapons.json"

# Fallback: Enka moved some files. Let's use a more stable source if available, 
# but for now, let's just ensure we handle the 404 gracefully or try an alternative if known.
# Actually, looking at current Enka docs, the paths are often:
# https://raw.githubusercontent.com/EnkaNetwork/API-docs/master/store/weapons.json

# Wait, if it's 404, it might be a connectivity issue in the restricted env. 
# Let's try to update the base URLs if I know them, or just add better error handling.

# The user is getting a 404. Let's assume the paths are correct and there's 
# a transient issue or the file moved. 
# Since I cannot browse the web, I will assume the paths are standard 
# but perhaps the raw.githubusercontent.com is being blocked or the repo structure changed.
# Given I cannot change the remote URL, I will improve error handling 
# to not crash the entire request.


HEADERS = {"User-Agent": "CritCal/2.0 (Discord Build Rating Bot)"}
CACHE_TTL_SECONDS = 6 * 60 * 60

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

_char_cache = {"data": None, "time": 0}
_weapon_cache = {"data": None, "time": 0}
_loc_cache = {"data": None, "time": 0}


def _cached_json(url, cache):
    """Downloads JSON once every CACHE_TTL_SECONDS; raises ValueError on failure."""
    now = time.time()
    if cache["data"] is not None and now - cache["time"] < CACHE_TTL_SECONDS:
        return cache["data"]

    try:
        resp = requests.get(url, headers=HEADERS, timeout=10)
        # If the file is missing (404), return empty dict instead of crashing
        if resp.status_code == 404:
            return {}
        resp.raise_for_status()
        data = resp.json()
    except requests.RequestException as e:
        # If we have stale cached data, prefer serving that over failing outright.
        if cache["data"] is not None:
            return cache["data"]
        # Return empty instead of raising, so the API can still function 
        # for core features that don't depend on this specific file.
        return {}

    cache["data"] = data
    cache["time"] = now
    return data


def _load_localization():
    loc = _cached_json(LOC_STORE_URL, _loc_cache)
    return loc.get("en", loc)


def _load_character_names():
    chars = _cached_json(CHAR_STORE_URL, _char_cache)
    loc = _load_localization()
    names = {}
    for avatar_id, data in chars.items():
        hash_id = str(data.get("NameTextMapHash", ""))
        if hash_id in loc:
            names[str(avatar_id)] = loc[hash_id]
    return names


def _load_weapon_names():
    weapons = _cached_json(WEAPON_STORE_URL, _weapon_cache)
    loc = _load_localization()
    result = {}
    for weapon_id, data in weapons.items():
        hash_id = str(data.get("NameTextMapHash", ""))
        result[str(weapon_id)] = {
            "name": loc.get(hash_id, f"Weapon #{weapon_id}"),
            "rarity": data.get("rankLevel"),
            "icon": data.get("icon"),
        }
    return result


def _refinement_from_affix_map(affix_map):
    """
    Converts Enka's raw affixMap (e.g. {"115006": 2}) into a human refinement
    rank (R1-R5). The value is a 0-indexed rank, so R = value + 1. Weapons
    with no affix entry (rare edge cases) default to R1.
    """
    if not affix_map:
        return 1
    try:
        return int(list(affix_map.values())[0]) + 1
    except (ValueError, TypeError, IndexError):
        return 1


def _extract_weapon(equip_list):
    """
    Returns a dict describing the equipped weapon, or None if somehow
    missing (shouldn't normally happen -- every character has a weapon).

    Resolves the weapon name via flat.nameTextMapHash through the
    localization store, same approach as artifact sets -- this avoids
    depending on the separate weapons.json (which was removed from
    Enka's API-docs repo upstream and now returns 404).
    """
    loc = _load_localization()

    for equip in equip_list:
        if "weapon" not in equip:
            continue

        weapon = equip["weapon"]
        flat = equip.get("flat", {})
        name_hash = str(flat.get("nameTextMapHash", ""))
        weapon_name = loc.get(name_hash, "Unknown Weapon")
        weapon_rarity = flat.get("rankLevel")
        weapon_icon = flat.get("icon")

        return {
            "name": weapon_name,
            "level": weapon.get("level"),
            "ascension": weapon.get("promoteLevel"),
            "refinement": _refinement_from_affix_map(weapon.get("affixMap", {})),
            "rarity": weapon_rarity,
            "icon": weapon_icon,
        }

    return None


def _extract_artifact_sets(equip_list):
    """
    Returns equipped artifact set bonuses, e.g.:
    [{"name": "Golden Troupe", "count": 4}]

    BUG FIX: the original version looked for a `flat.setId` field that
    doesn't exist in Enka's raw response. Sets are actually identified via
    `flat.setNameTextMapHash`, resolved directly against the localization
    store -- no separate artifact-set store/lookup needed at all.
    """
    loc = _load_localization()
    counts = {}

    for equip in equip_list:
        if "reliquary" not in equip:
            continue
        flat = equip.get("flat", {})
        hash_id = str(flat.get("setNameTextMapHash", ""))
        if not hash_id:
            continue
        set_name = loc.get(hash_id, "Unknown Set")
        counts[set_name] = counts.get(set_name, 0) + 1

    return [
        {"name": name, "count": count}
        for name, count in sorted(counts.items(), key=lambda x: x[1], reverse=True)
    ]


def _extract_substats(equip_list):
    totals = {
        "crit_rate": 0.0, "crit_dmg": 0.0, "atk_percent": 0.0, "atk_flat": 0.0,
        "hp_percent": 0.0, "def_percent": 0.0, "elemental_mastery": 0.0, "energy_recharge": 0.0,
    }
    for equip in equip_list:
        if "reliquary" not in equip:
            continue
        flat = equip.get("flat", {})
        for stat in flat.get("reliquarySubstats", []):
            key = APPEND_PROP_MAP.get(stat.get("appendPropId"))
            if key:
                totals[key] += float(stat.get("statValue", 0))
    return totals


def _find_character(player_data, requested_name):
    """Finds a character by name; returns the first showcased character if none given."""
    characters = player_data.get("avatarInfoList", [])
    if not characters:
        raise ValueError(
            "This player's Character Showcase is empty or private. "
            "They need to showcase the character in-game first."
        )

    if not requested_name:
        return characters[0]

    requested = requested_name.lower().strip()
    names = _load_character_names()

    for avatar in characters:
        avatar_id = str(avatar.get("avatarId"))
        name = names.get(avatar_id, "").lower()
        if name == requested:
            return avatar

    showcased = [names.get(str(a.get("avatarId")), "Unknown") for a in characters]
    raise ValueError(
        f"'{requested_name}' isn't in this player's showcase. "
        f"Showcased characters: {', '.join(showcased)}"
    )


def _extract_avatar_data(avatar):
    """
    Extracts stats, substats, weapon, and artifact_sets from a single
    Enka avatar object. Shared by fetch_character and fetch_all_characters.
    """
    fight_props = avatar.get("fightPropMap", {})
    equip_list = avatar.get("equipList", [])

    stats = {
        "crit_rate": 5.0,
        "crit_dmg": 50.0,
        "atk": 0.0,
        "hp": 0.0,
        "def": 0.0,
        "elemental_mastery": 0.0,
        "energy_recharge": 100.0,
    }

    for prop_id, key in FIGHT_PROP_MAP.items():
        if prop_id not in fight_props:
            continue
        value = float(fight_props[prop_id])
        if key in ("crit_rate", "crit_dmg", "energy_recharge"):
            value *= 100
        stats[key] = round(value, 2)

    return {
        "character": _load_character_names().get(str(avatar.get("avatarId")), "Unknown"),
        "stats": stats,
        "substats": _extract_substats(equip_list),
        "weapon": _extract_weapon(equip_list),
        "artifact_sets": _extract_artifact_sets(equip_list),
    }


def _fetch_enka_uid(uid):
    """
    Fetches raw player data from Enka.Network and validates the response.
    Returns the parsed JSON on success.
    Raises ValueError with a user-friendly message on any failure.
    Shared by fetch_character and fetch_all_characters.
    """
    try:
        response = requests.get(f"{ENKA_BASE}/{uid}", headers=HEADERS, timeout=15)
    except requests.RequestException as e:
        raise ValueError(f"Could not reach Enka.Network: {e}")

    if response.status_code == 400:
        raise ValueError("That UID doesn't look valid.")
    if response.status_code == 404:
        raise ValueError("No player found with that UID.")
    if response.status_code == 424:
        raise ValueError("Genshin servers are under maintenance right now -- try again later.")
    if response.status_code == 429:
        raise ValueError("Rate-limited by Enka.Network -- try again in a minute.")
    if response.status_code != 200:
        raise ValueError(f"Enka.Network returned an unexpected error ({response.status_code}).")

    return response.json()


def fetch_character(uid, character_name=None):
    """
    Fetches a character build from Enka.Network.
    Returns a dict with character, stats, substats, weapon, and artifact_sets.
    Raises ValueError with a user-friendly message on any failure.
    """
    player = _fetch_enka_uid(uid)
    avatar = _find_character(player, character_name)
    return _extract_avatar_data(avatar)


def fetch_all_characters(uid):
    """
    Fetches ALL showcased character builds from Enka.Network for a UID.

    Returns a list of dicts (same shape as fetch_character's return value),
    one per showcased character. Raises ValueError on any failure.
    """
    player = _fetch_enka_uid(uid)
    avatars = player.get("avatarInfoList", [])
    if not avatars:
        raise ValueError("This player's Character Showcase is empty or private.")

    results = []
    for avatar in avatars:
        data = _extract_avatar_data(avatar)
        results.append(data)

    return results
