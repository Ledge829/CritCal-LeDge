"""
Global item catalog for CritCal -- every weapon (with type + rarity) and
every artifact set that exists in the game, independent of any specific
character's curated build_data.py picks.

WHY THIS FILE EXISTS (separate from build_data.py):
build_data.py only tracks ~4 curated weapons and ~3 artifact sets PER
CHARACTER -- a tiny fraction of the ~244 weapons and 62 sets in the game.
Before this file, anything outside a character's curated list fell into
one flat "Unlisted" bucket with no way to tell a genuinely strong
uncatalogued pick (e.g. The Widsith on a support-leaning build) apart
from a plain typo. This catalog fixes that by giving scoring.py a
GLOBAL reference so it can:
  1. Confirm a submitted weapon/set actually exists (catch typos as a
     distinct "Unrecognized" tier instead of lumping them in with valid
     uncatalogued picks).
  2. Flag when a submitted weapon's TYPE doesn't match the character's
     weapon type (e.g. a Bow name submitted for a Catalyst user) --
     something that's impossible in-game but easy to typo in a manual
     request.
  3. Give a graduated "Unlisted" score based on rarity, so an uncatalogued
     5-star isn't scored identically to an uncatalogued 3-star.

COVERAGE: this is a strong starting catalog, not a claim of covering
literally all 244 weapons / 62 sets -- it covers the vast majority of
weapons players actually equip (all 5-star weapons, most notable 4-star
weapons, and the common F2P/craftable 3-stars already referenced in
build_data.py) plus the full modern (4-5 star) artifact set roster and
the legacy 1-3 star sets. Treat it like the character rollout: add to it
incrementally as gaps come up, rather than expecting it to be finished.
Re-verify periodically -- new weapons/sets ship with new patches.

SCHEMA:
  WEAPONS: Dict[str, Tuple[str, bool]]
      lowercased weapon name -> (weapon_type, is_five_star)
      weapon_type is one of: "sword", "claymore", "polearm", "bow", "catalyst"

  ARTIFACT_SETS: Dict[str, bool]
      lowercased set name -> is_modern (True for the 4-5 star sets
      players actually build around; False for the legacy 1-3 star sets
      that exist but are essentially never intentionally equipped)

Lookups elsewhere should go through the WEAPON_TYPES / lookup helpers
below rather than reading these dicts directly, so casing/whitespace
handling stays consistent in one place.
"""

from typing import Dict, Tuple, Optional

# ==========================================================
# WEAPONS
# name (any case) -> (type, is_five_star)
# ==========================================================

_SWORDS = {
    # 5-star
    "mistsplitter reforged": True, "primordial jade cutter": True, "summit shaper": True,
    "freedom-sworn": True, "skyward blade": True, "aquila favonia": True,
    "uraku misugiri": True, "splendor of tranquil waters": True, "light of foliar incision": True,
    "key of khaj-nisut": True, "haran geppaku futsu": True, "absolution": True,
    "azurelight": True, "peak patrol song": True, "athame artis": True,
    # 4-star
    "the dockhand's assistant": False, "fleuve cendre ferryman": False, "wolf-fang": False,
    "toukabou shigure": False, "xiphos' moonlight": False, "sapwood blade": False,
    "kagotsurube isshin": False, "cinnabar spindle": False, "amenoma kageuchi": False,
    "festering desire": False, "the alley flash": False, "the black sword": False,
    "blackcliff longsword": False, "iron sting": False, "prototype rancour": False,
    "lion's roar": False, "royal longsword": False, "sacrificial sword": False,
    "the flute": False, "favonius sword": False, "finale of the deep": False,
    "sword of narzissenkreuz": False, "moonweaver's dawn": False,
    # 3-star / craftable / F2P
    "cool steel": False, "harbinger of dawn": False, "traveler's handy sword": False,
    "skyrider sword": False, "fillet blade": False, "dark iron sword": False,
    "sword of descension": False,
}

_CLAYMORES = {
    # 5-star
    "a thousand blazing suns": True, "fang of the mountain king": True, "verdict": True,
    "beacon of the reed sea": True, "redhorn stonethresher": True, "the unforged": True,
    "song of broken pines": True, "wolf's gravestone": True, "skyward pride": True,
    "gest of the mighty wolf": True, "a teaspoon of transcendence": True,
    # 4-star
    "akuoumaru": False, "makhaira aquamarine": False, "katsuragikiri nagamasa": False,
    "luxurious sea-lord": False, "snow-tombed starsilver": False, "lithic blade": False,
    "serpent spine": False, "blackcliff slasher": False, "whiteblind": False,
    "prototype archaic": False, "rainslasher": False, "royal greatsword": False,
    "sacrificial greatsword": False, "the bell": False, "favonius greatsword": False,
    "fruitful hook": False, "portable power saw": False, "tidal shadow": False,
    "tidal shadows": False, "talking stick": False, "mailed flower": False,
    "forest regalia": False, "ultimate overlord's mega magic sword": False,
    "earth shaker": False, "flame-forged insight": False, "master key": False,
    # 3-star / craftable / F2P
    "debate club": False, "bloodtainted greatsword": False, "white iron greatsword": False,
    "waster greatsword": False, "serpent spine (3-star)": False,
}

_POLEARMS = {
    # 5-star
    "staff of the scarlet sands": True, "engulfing lightning": True, "calamity queller": True,
    "primordial jade winged-spear": True, "vortex vanquisher": True, "skyward spine": True,
    "staff of homa": True, "crimson moon's semblance": True, "lumidouce elegy": True,
    "symphonist of scents": True, "bloodsoaked ruins": True,
    # 4-star
    "prospector's drill": False, "dialogues of the desert sages": False, "rightful reward": False,
    "ballad of the fjords": False, "missive windspear": False, "moonpiercer": False,
    "wavebreaker's fin": False, "the catch": False, "kitain cross spear": False,
    "dragonspine spear": False, "royal spear": False, "favonius lance": False,
    "lithic spear": False, "deathmatch": False, "blackcliff pole": False,
    "crescent pike": False, "prototype starglitter": False, "dragon's bane": False,
    "sacrificer's staff": False, "prospector's shovel": False, "tamayuratei no ohanashi": False,
    "footprint of the rainbow": False, "mountain-bracing bolt": False, "song of days past": False,
    # 3-star / craftable / F2P
    "white tassel": False, "black tassel": False, "halberd": False, "iron point": False,
}

_CATALYSTS = {
    # 5-star
    "nocturne's curtain call": True, "reliquary of truth": True, "nightweaver's looking glass": True,
    "vivid notions": True, "sunny morning sleep-in": True, "starcaller's watch": True,
    "surf's up": True, "crane's echoing call": True, "tome of the eternal flow": True,
    "cashflow supervision": True, "tulaytullah's remembrance": True, "a thousand floating dreams": True,
    "kagura's verity": True, "everlasting moonglow": True, "jadefall's splendor": True,
    "memory of dust": True, "lost prayer to the sacred winds": True, "skyward atlas": True,
    "seven edicts of dust and light": True,
    # 4-star
    "dawning frost": False, "blackmarrow lantern": False,
    "the widsith": False, "solar pearl": False,
    "prototype amber": False, "sacrificial fragments": False, "favonius codex": False,
    "mappa mare": False, "hakushin ring": False, "eye of perception": False,
    "wine and song": False, "blackcliff agate": False, "oathsworn eye": False,
    "ballad of the boundless blue": False, "flowing purity": False, "fruit of fulfillment": False,
    "ring of yaxche": False, "sacrificial jade": False, "frostbearer": False,
    "royal grimoire": False, "waveriding whirl": False, "etherlight spindlelute": False,
    # 3-star / craftable / F2P
    "apprentice's notes": False, "pocket grimoire": False, "otherworldly story": False,
    "emerald orb": False, "magic guide": False, "thrilling tales of dragon slayers": False,
    "twin nephrite": False,
}

_BOWS = {
    # 5-star
    "golden frostbound oath": True, "the daybreak chronicles": True, "astral vulture's crimson plumage": True,
    "silvershower heartstrings": True, "the first great magic": True, "hunter's path": True,
    "thundering pulse": True, "aqua simulacra": True, "polar star": True,
    "elegy for the end": True, "skyward harp": True, "amos' bow": True,
    # 4-star
    "end of the line": False, "fading twilight": False, "stringless": False,
    "sacrificial bow": False, "favonius warbow": False, "prototype crescent": False,
    "compound bow": False, "rust": False, "alley hunter": False,
    "blackcliff warbow": False, "windblume ode": False, "mitternachts waltz": False,
    "ichor of the nail": False, "the viridescent hunt": False, "sequence of solitude": False,
    "hamayumi": False, "song of stillness": False, "chain breaker": False,
    "scion of the blazing sun": False, "ibis piercer": False, "the stringless": False,
    # 3-star / craftable / F2P
    "raven bow": False, "sharpshooter's oath": False, "slingshot": False,
    "messenger": False, "recurve bow": False, "seasoned hunter's bow": False,
    "ebony bow": False,
}

WEAPONS: Dict[str, Tuple[str, bool]] = {}
for _name, _is5 in _SWORDS.items():
    WEAPONS[_name] = ("sword", _is5)
for _name, _is5 in _CLAYMORES.items():
    WEAPONS[_name] = ("claymore", _is5)
for _name, _is5 in _POLEARMS.items():
    WEAPONS[_name] = ("polearm", _is5)
for _name, _is5 in _CATALYSTS.items():
    WEAPONS[_name] = ("catalyst", _is5)
for _name, _is5 in _BOWS.items():
    WEAPONS[_name] = ("bow", _is5)


# ==========================================================
# ARTIFACT SETS
# name (any case) -> is_modern (True = 4-5 star set players actually
# build around; False = legacy 1-3 star set, real but essentially never
# intentionally equipped)
# ==========================================================

ARTIFACT_SETS: Dict[str, bool] = {
    # Modern (4-5 star)
    "gladiator's finale": True, "wanderer's troupe": True, "noblesse oblige": True,
    "bloodstained chivalry": True, "maiden beloved": True, "viridescent venerer": True,
    "crimson witch of flames": True, "thundersoother": True, "thundering fury": True,
    "lavawalker": True, "blizzard strayer": True, "heart of depth": True,
    "tenacity of the millelith": True, "pale flame": True, "shimenawa's reminiscence": True,
    "emblem of severed fate": True, "husk of opulent dreams": True, "ocean-hued clam": True,
    "vermillion hereafter": True, "echoes of an offering": True, "deepwood memories": True,
    "gilded dreams": True, "desert pavilion chronicle": True, "flower of paradise lost": True,
    "nymph's dream": True, "vourukasha's glow": True, "marechaussee hunter": True,
    "golden troupe": True, "song of days past": True, "nighttime whispers in the echoing woods": True,
    "fragment of harmonic whimsy": True, "unfinished reverie": True,
    "scroll of the hero of cinder city": True, "obsidian codex": True,
    "long night's oath": True, "finale of the deep (artifact)": True, "retracing bolide": True,
    "instructor's": True, "archaic petra": True,
    "disenchantment in deep shadow": True, "a day carved from rising winds": True,
    "night of the sky's unveiling": True, "silken moon's serenade": True,
    "finale of the deep galleries": True,
    # Legacy (1-3 star, real but essentially never intentionally equipped)
    "initiate": False, "adventurer": False, "lucky dog": False, "traveling doctor": False,
    "resolution of sojourner": False, "tiny miracle": False, "berserker": False,
    "the exile": False, "defender's will": False, "brave heart": False,
    "martial artist": False, "gambler": False, "scholar": False,
    "prayers for wisdom": False, "prayers for destiny": False,
    "prayers for illumination": False, "prayers to springtime": False,
}


# ==========================================================
# LOOKUP HELPERS
# ==========================================================

def lookup_weapon(name: str) -> Optional[Tuple[str, bool]]:
    """Returns (type, is_five_star) for a weapon name, or None if unrecognized."""
    if not name or not isinstance(name, str):
        return None
    return WEAPONS.get(name.strip().lower())


def lookup_artifact_set(name: str) -> Optional[bool]:
    """Returns is_modern for a set name, or None if unrecognized."""
    if not name or not isinstance(name, str):
        return None
    return ARTIFACT_SETS.get(name.strip().lower())
