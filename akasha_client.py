"""
Best-effort client for akasha.cv leaderboard data, via the unofficial
`akasha-py` wrapper.

IMPORTANT: akasha.cv has no official public API. This wrapper is
community-maintained and its own README states the underlying API
"changes very frequently (and without notice)" and may break at any
time. Because of that, EVERY call in this module is designed to fail
silently and return None rather than raise -- CritiCal's own heuristic
scoring must always work even if Akasha is unreachable, has changed
its response shape, or simply doesn't have this player/character
calculated yet (new UID, obscure character, etc).

If this stops working entirely after an akasha.cv update, that's
expected per their own maintainer's warning -- check
https://github.com/seriaati/akasha-py for wrapper updates, or fall
back to running without this feature until it's fixed.
"""
import asyncio


def _normalize(name):
    return name.lower().replace(" ", "").replace("-", "").replace("'", "")


async def _fetch(uid, character_name):
    import akasha  # imported lazily so a broken/missing dependency can't crash the whole app

    target = _normalize(character_name)

    async with akasha.AkashaAPI(akasha.Language.ENGLISH) as api:
        characters = await api.get_calculations_for_user(int(uid))

        for character in characters:
            if _normalize(character.name) != target:
                continue
            if not character.calculations:
                continue

            calc = character.calculations[0]
            return {
                "top_percent": round(calc.top_percent, 2),
                "ranking": calc.ranking,
                "out_of": calc.out_of,
                "weapon": calc.weapon.name,
                "damage_result": round(calc.result),
                "leaderboard_url": f"https://akasha.cv/leaderboards/{calc.id}",
            }

    return None  # player found, but this character isn't calculated on Akasha


def get_akasha_data(uid, character_name):
    """
    Returns a dict of Akasha leaderboard data for this character, or None
    if unavailable for ANY reason (not on Akasha, character not supported,
    API changed/down, network issue, etc). Never raises.
    """
    try:
        return asyncio.run(_fetch(uid, character_name))
    except Exception:
        # Deliberately broad: this is a bonus feature layered on top of an
        # unofficial, frequently-changing API. Any failure here should be
        # invisible to the person using the bot, not a broken response.
        return None
  
