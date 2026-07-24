"""
Weapon type data for CritCal's character database.

Kept as a SEPARATE additive module from characters.py rather than merged
in-place -- this means adding/fixing weapon data can never accidentally
touch the already-verified scaling/crit-ratio config (e.g. Flins,
Neuvillette) that required real leaderboard data to get right.

NOTE: Curated BiS/secondary/f2p/niche weapon picks now live in
build_data.py's WEAPON_TIERS dict, which supersedes the older
recommended_weapons list that was previously here.

Confidence levels:
- weapon_type: deterministic game data (each character has exactly one
  fixed weapon type) -- high confidence across the board.
- A handful of entries are marked LOWER CONFIDENCE below where my own
  certainty was genuinely borderline -- worth spot-checking those first.
"""
from typing import Dict, Any

WEAPON_DATA: Dict[str, Dict[str, Any]] = {
    # ===== PYRO =====
    "arlecchino": {"weapon_type": "Polearm"},
    "bennett": {"weapon_type": "Sword"},
    "chevreuse": {"weapon_type": "Polearm"},
    "dehya": {"weapon_type": "Claymore"},
    "diluc": {"weapon_type": "Claymore"},
    "gaming": {"weapon_type": "Claymore"},
    "hutao": {"weapon_type": "Polearm"},
    "klee": {"weapon_type": "Catalyst"},
    "lyney": {"weapon_type": "Bow"},
    "mavuika": {"weapon_type": "Claymore"},
    "thoma": {"weapon_type": "Polearm"},
    "xiangling": {"weapon_type": "Polearm"},
    "xinyan": {"weapon_type": "Claymore"},

    # ===== HYDRO =====
    "barbara": {"weapon_type": "Catalyst"},
    "candace": {"weapon_type": "Polearm"},
    "childe": {"weapon_type": "Bow"},
    "furina": {"weapon_type": "Sword"},
    "kokomi": {"weapon_type": "Catalyst"},
    "mona": {"weapon_type": "Catalyst"},
    "mualani": {"weapon_type": "Catalyst"},
    "neuvillette": {"weapon_type": "Catalyst"},
    "nilou": {"weapon_type": "Sword"},
    "sigewinne": {"weapon_type": "Bow"},
    "xingqiu": {"weapon_type": "Sword"},
    "yelan": {"weapon_type": "Bow"},

    # ===== ANEMO =====
    "chasca": {"weapon_type": "Bow"},
    "faruzan": {"weapon_type": "Bow"},
    "heizou": {"weapon_type": "Catalyst"},
    "jean": {"weapon_type": "Sword"},
    "kazuha": {"weapon_type": "Sword"},
    # LOWER CONFIDENCE: Lan Yan's exact weapon type wasn't fully certain in review -- worth spot-checking.
    "lanyan": {"weapon_type": "Catalyst"},
    "lynette": {"weapon_type": "Sword"},
    "sayu": {"weapon_type": "Claymore"},
    "sucrose": {"weapon_type": "Catalyst"},
    "venti": {"weapon_type": "Bow"},
    "wanderer": {"weapon_type": "Catalyst"},
    "xianyun": {"weapon_type": "Catalyst"},

    # ===== ELECTRO =====
    "beidou": {"weapon_type": "Claymore"},
    "clorinde": {"weapon_type": "Sword"},
    "cyno": {"weapon_type": "Polearm"},
    "dori": {"weapon_type": "Claymore"},
    "fischl": {"weapon_type": "Bow"},
    # LOWER CONFIDENCE: Flins's weapon type -- I believe Catalyst but this was borderline in review.
    # CORRECTED: confirmed Polearm (Game8, GameWith, KQM all agree, and
    # independently verified via Enka's own game data: WeaponType WEAPON_POLE).
    # Was previously miscatalogued here as Catalyst.
    "flins": {"weapon_type": "Polearm"},
    "keqing": {"weapon_type": "Sword"},
    "kukishinobu": {"weapon_type": "Sword"},
    "lisa": {"weapon_type": "Catalyst"},
    "ororon": {"weapon_type": "Bow"},
    "raiden": {"weapon_type": "Polearm"},
    "razor": {"weapon_type": "Claymore"},
    "sara": {"weapon_type": "Bow"},
    "sethos": {"weapon_type": "Bow"},
    "yaemiko": {"weapon_type": "Catalyst"},

    # ===== DENDRO =====
    "alhaitham": {"weapon_type": "Sword"},
    "baizhu": {"weapon_type": "Catalyst"},
    "collei": {"weapon_type": "Bow"},
    "emilie": {"weapon_type": "Polearm"},
    "kaveh": {"weapon_type": "Claymore"},
    "kinich": {"weapon_type": "Claymore"},
    "nahida": {"weapon_type": "Catalyst"},
    "tighnari": {"weapon_type": "Bow"},
    "yaoyao": {"weapon_type": "Polearm"},

    # ===== CRYO =====
    "ayaka": {"weapon_type": "Sword"},
    "charlotte": {"weapon_type": "Catalyst"},
    "chongyun": {"weapon_type": "Claymore"},
    "citlali": {"weapon_type": "Catalyst"},
    "diona": {"weapon_type": "Bow"},
    "eula": {"weapon_type": "Claymore"},
    "freminet": {"weapon_type": "Claymore"},
    "ganyu": {"weapon_type": "Bow"},
    "kaeya": {"weapon_type": "Sword"},
    "layla": {"weapon_type": "Sword"},
    "mika": {"weapon_type": "Polearm"},
    "qiqi": {"weapon_type": "Sword"},
    "rosaria": {"weapon_type": "Polearm"},
    "shenhe": {"weapon_type": "Polearm"},
    "skirk": {"weapon_type": "Sword"},
    "wriothesley": {"weapon_type": "Catalyst"},

    # ===== GEO =====
    "albedo": {"weapon_type": "Sword"},
    "chiori": {"weapon_type": "Sword"},
    "gorou": {"weapon_type": "Bow"},
    "itto": {"weapon_type": "Claymore"},
    # CORRECTED: confirmed Polearm (GameWith's guide explicitly discusses
    # "DEF polearms" for her build, and independently verified via Enka's
    # own game data: WeaponType WEAPON_POLE). Was previously miscatalogued
    # here as Claymore.
    "kachina": {"weapon_type": "Polearm"},
    "navia": {"weapon_type": "Claymore"},
    "ningguang": {"weapon_type": "Catalyst"},
    "noelle": {"weapon_type": "Claymore"},
    # LOWER CONFIDENCE: Xilonen's weapon type -- believed Sword, worth spot-checking.
    "xilonen": {"weapon_type": "Sword"},
    "yunjin": {"weapon_type": "Polearm"},

    # ===== TRAVELER =====
    "traveler": {"weapon_type": "Sword"},
    "anemotraveler": {"weapon_type": "Sword"},
    "geotraveler": {"weapon_type": "Sword"},
    "electrotraveler": {"weapon_type": "Sword"},
    "dendrotraveler": {"weapon_type": "Sword"},
    "hydrotraveler": {"weapon_type": "Sword"},
    "pyrotraveler": {"weapon_type": "Sword"},

    # ===== NEW CHARACTERS (post-Jan-2026 cutoff, researched live) =====
    "ineffa": {"weapon_type": "Polearm"},
    "illuga": {"weapon_type": "Polearm"},
    "zibai": {"weapon_type": "Sword"},
    "columbina": {"weapon_type": "Catalyst"},
    "lohen": {"weapon_type": "Polearm"},
    "linnea": {"weapon_type": "Bow"},
    "varka": {"weapon_type": "Claymore"},
    "nicole": {"weapon_type": "Catalyst"},
    "prune": {"weapon_type": "Claymore"},
    "aloy": {"weapon_type": "Bow"},
    "durin": {"weapon_type": "Sword"},
    "jahoda": {"weapon_type": "Bow"},
    "ain": {"weapon_type": "Bow"},
    "amber": {"weapon_type": "Bow"},
    "ayato": {"weapon_type": "Sword"},
    "ifa": {"weapon_type": "Catalyst"},
    "iansan": {"weapon_type": "Polearm"},
    "kirara": {"weapon_type": "Sword"},
    "lauma": {"weapon_type": "Catalyst"},
    "mizuki": {"weapon_type": "Catalyst"},
    "nefer": {"weapon_type": "Catalyst"},
    "sandrone": {"weapon_type": "Claymore"},
    "varesa": {"weapon_type": "Catalyst"},
    "xiao": {"weapon_type": "Polearm"},
    "yanfei": {"weapon_type": "Catalyst"},
    "dahlia": {"weapon_type": "Sword"},
    "escoffier": {"weapon_type": "Polearm"},
    "yoimiya": {"weapon_type": "Bow"},
    "zhongli": {"weapon_type": "Polearm"},
}
