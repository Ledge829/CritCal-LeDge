"""
Weapon type and recommended-weapon data for CritiCal's character database.

Kept as a SEPARATE additive module from characters.py rather than merged
in-place -- this means adding/fixing weapon data can never accidentally
touch the already-verified scaling/crit-ratio config (e.g. Flins,
Neuvillette) that required real leaderboard data to get right.

Confidence levels:
- weapon_type: deterministic game data (each character has exactly one
  fixed weapon type) -- high confidence across the board.
- recommended_weapons: community BiS/meta consensus, inherently more
  subjective and patch-dependent than weapon_type. Reliable for
  well-established characters; a few very recently released characters
  (noted below) are based on early post-launch guides and may shift as
  the meta settles.
- A handful of entries are marked LOWER CONFIDENCE below where my own
  certainty was genuinely borderline -- worth spot-checking those first.
"""
from typing import Dict, Any

WEAPON_DATA: Dict[str, Dict[str, Any]] = {
    # ===== PYRO =====
    "arlecchino": {"weapon_type": "Polearm", "recommended_weapons": ["Crimson Moon's Semblance", "Deathmatch"]},
    "bennett": {"weapon_type": "Sword", "recommended_weapons": ["Aquila Favonia", "Sacrificial Sword"]},
    "chevreuse": {"weapon_type": "Polearm", "recommended_weapons": ["Favonius Lance", "Prototype Starglitter"]},
    "dehya": {"weapon_type": "Claymore", "recommended_weapons": ["Redhorn Stonethresher", "Serpent Spine"]},
    "diluc": {"weapon_type": "Claymore", "recommended_weapons": ["Wolf's Gravestone", "Serpent Spine"]},
    "gaming": {"weapon_type": "Claymore", "recommended_weapons": ["Redhorn Stonethresher", "Serpent Spine"]},
    "hutao": {"weapon_type": "Polearm", "recommended_weapons": ["Staff of Homa", "Dragon's Bane"]},
    "klee": {"weapon_type": "Catalyst", "recommended_weapons": ["Lost Prayer to the Sacred Winds", "Sacrificial Fragments"]},
    "lyney": {"weapon_type": "Bow", "recommended_weapons": ["Aqua Simulacra", "Rust"]},
    "mavuika": {"weapon_type": "Claymore", "recommended_weapons": ["Verdict", "Serpent Spine"]},
    "thoma": {"weapon_type": "Polearm", "recommended_weapons": ["Favonius Lance", "Prototype Starglitter"]},
    "xiangling": {"weapon_type": "Polearm", "recommended_weapons": ["Engulfing Lightning", "Favonius Lance"]},
    "xinyan": {"weapon_type": "Claymore", "recommended_weapons": ["Serpent Spine", "Rainslasher"]},

    # ===== HYDRO =====
    "barbara": {"weapon_type": "Catalyst", "recommended_weapons": ["Prototype Amber", "Sacrificial Fragments"]},
    "candace": {"weapon_type": "Polearm", "recommended_weapons": ["Favonius Lance", "Prototype Starglitter"]},
    "childe": {"weapon_type": "Bow", "recommended_weapons": ["Polar Star", "Aqua Simulacra"]},
    "furina": {"weapon_type": "Sword", "recommended_weapons": ["Splendor of Tranquil Waters", "Sacrificial Sword"]},
    "kokomi": {"weapon_type": "Catalyst", "recommended_weapons": ["Everlasting Moonglow", "Prototype Amber"]},
    "mona": {"weapon_type": "Catalyst", "recommended_weapons": ["Thrilling Tales of Dragon Slayers", "Sacrificial Fragments"]},
    "mualani": {"weapon_type": "Catalyst", "recommended_weapons": ["Surf's Up", "Prototype Amber"]},
    "neuvillette": {"weapon_type": "Catalyst", "recommended_weapons": ["Tome of the Eternal Flow", "Prototype Amber"]},
    "nilou": {"weapon_type": "Sword", "recommended_weapons": ["Key of Khaj-Nisut", "Festering Desire"]},
    "sigewinne": {"weapon_type": "Bow", "recommended_weapons": ["Fleuve Cendre Ferryman", "Sacrificial Bow"]},
    "xingqiu": {"weapon_type": "Sword", "recommended_weapons": ["Sacrificial Sword", "Favonius Sword"]},
    "yelan": {"weapon_type": "Bow", "recommended_weapons": ["Aqua Simulacra", "Sacrificial Bow"]},

    # ===== ANEMO =====
    "chasca": {"weapon_type": "Bow", "recommended_weapons": ["The First Great Magic", "Hunter's Path"]},
    "faruzan": {"weapon_type": "Bow", "recommended_weapons": ["Hunter's Path", "Sacrificial Bow"]},
    "heizou": {"weapon_type": "Catalyst", "recommended_weapons": ["Lost Prayer to the Sacred Winds", "Sacrificial Fragments"]},
    "jean": {"weapon_type": "Sword", "recommended_weapons": ["Freedom-Sworn", "Sacrificial Sword"]},
    "kazuha": {"weapon_type": "Sword", "recommended_weapons": ["Freedom-Sworn", "Iron Sting"]},
    # LOWER CONFIDENCE: Lan Yan's exact weapon type wasn't fully certain in review -- worth spot-checking.
    "lanyan": {"weapon_type": "Catalyst", "recommended_weapons": ["Prototype Amber", "Sacrificial Fragments"]},
    "lynette": {"weapon_type": "Sword", "recommended_weapons": ["Iron Sting", "Sacrificial Sword"]},
    "sayu": {"weapon_type": "Claymore", "recommended_weapons": ["Katsuragikiri Nagamasa", "Favonius Greatsword"]},
    "sucrose": {"weapon_type": "Catalyst", "recommended_weapons": ["Sacrificial Fragments", "Prototype Amber"]},
    "venti": {"weapon_type": "Bow", "recommended_weapons": ["Elegy for the End", "Sacrificial Bow"]},
    "wanderer": {"weapon_type": "Catalyst", "recommended_weapons": ["Tulaytullah's Remembrance", "Lost Prayer to the Sacred Winds"]},
    "xianyun": {"weapon_type": "Bow", "recommended_weapons": ["Aqua Simulacra", "Sacrificial Bow"]},

    # ===== ELECTRO =====
    "beidou": {"weapon_type": "Claymore", "recommended_weapons": ["Serpent Spine", "Favonius Greatsword"]},
    "clorinde": {"weapon_type": "Sword", "recommended_weapons": ["Absolution", "Wolf-Fang"]},
    "cyno": {"weapon_type": "Polearm", "recommended_weapons": ["Staff of the Scarlet Sands", "Deathmatch"]},
    "dori": {"weapon_type": "Claymore", "recommended_weapons": ["Favonius Greatsword", "Prototype Starglitter"]},
    "fischl": {"weapon_type": "Bow", "recommended_weapons": ["Polar Star", "Sacrificial Bow"]},
    # LOWER CONFIDENCE: Flins's weapon type -- I believe Catalyst but this was borderline in review.
    # CORRECTED: confirmed Polearm (Game8, GameWith, KQM all agree, and
    # independently verified via Enka's own game data: WeaponType WEAPON_POLE).
    # Was previously miscatalogued here as Catalyst.
    "flins": {"weapon_type": "Polearm", "recommended_weapons": ["Bloodsoaked Ruins", "Prospector's Shovel"]},
    "keqing": {"weapon_type": "Sword", "recommended_weapons": ["Mistsplitter Reforged", "Black Sword"]},
    "kukishinobu": {"weapon_type": "Sword", "recommended_weapons": ["Freedom-Sworn", "Iron Sting"]},
    "lisa": {"weapon_type": "Catalyst", "recommended_weapons": ["Lost Prayer to the Sacred Winds", "Sacrificial Fragments"]},
    "ororon": {"weapon_type": "Bow", "recommended_weapons": ["Hunter's Path", "Sacrificial Bow"]},
    "raiden": {"weapon_type": "Polearm", "recommended_weapons": ["Engulfing Lightning", "The Catch"]},
    "razor": {"weapon_type": "Claymore", "recommended_weapons": ["Wolf's Gravestone", "Serpent Spine"]},
    "sara": {"weapon_type": "Bow", "recommended_weapons": ["Favonius Warbow", "Sacrificial Bow"]},
    "sethos": {"weapon_type": "Bow", "recommended_weapons": ["Hunter's Path", "The First Great Magic"]},
    "yaemiko": {"weapon_type": "Catalyst", "recommended_weapons": ["Kagura's Verity", "Sacrificial Fragments"]},

    # ===== DENDRO =====
    "alhaitham": {"weapon_type": "Sword", "recommended_weapons": ["Light of Foliar Incision", "Xiphos' Moonlight"]},
    "baizhu": {"weapon_type": "Catalyst", "recommended_weapons": ["Jadefall's Splendor", "Prototype Amber"]},
    "collei": {"weapon_type": "Bow", "recommended_weapons": ["Sacrificial Bow", "Favonius Warbow"]},
    "emilie": {"weapon_type": "Polearm", "recommended_weapons": ["Crimson Moon's Semblance", "Deathmatch"]},
    "kaveh": {"weapon_type": "Claymore", "recommended_weapons": ["Beacon of the Reed Sea", "Favonius Greatsword"]},
    "kinich": {"weapon_type": "Claymore", "recommended_weapons": ["Redhorn Stonethresher", "Serpent Spine"]},
    "nahida": {"weapon_type": "Catalyst", "recommended_weapons": ["A Thousand Floating Dreams", "Sacrificial Fragments"]},
    "tighnari": {"weapon_type": "Bow", "recommended_weapons": ["Hunter's Path", "The First Great Magic"]},
    "yaoyao": {"weapon_type": "Polearm", "recommended_weapons": ["Favonius Lance", "Prototype Starglitter"]},

    # ===== CRYO =====
    "ayaka": {"weapon_type": "Sword", "recommended_weapons": ["Mistsplitter Reforged", "Amenoma Kageuchi"]},
    "charlotte": {"weapon_type": "Catalyst", "recommended_weapons": ["Prototype Amber", "Sacrificial Fragments"]},
    "chongyun": {"weapon_type": "Claymore", "recommended_weapons": ["Favonius Greatsword", "Serpent Spine"]},
    "citlali": {"weapon_type": "Catalyst", "recommended_weapons": ["Tome of the Eternal Flow", "Prototype Amber"]},
    "diona": {"weapon_type": "Bow", "recommended_weapons": ["Sacrificial Bow", "Favonius Warbow"]},
    "eula": {"weapon_type": "Claymore", "recommended_weapons": ["Song of Broken Pines", "Serpent Spine"]},
    "freminet": {"weapon_type": "Claymore", "recommended_weapons": ["Serpent Spine", "Redhorn Stonethresher"]},
    "ganyu": {"weapon_type": "Bow", "recommended_weapons": ["Amos' Bow", "Polar Star"]},
    "kaeya": {"weapon_type": "Sword", "recommended_weapons": ["Sacrificial Sword", "Favonius Sword"]},
    "layla": {"weapon_type": "Sword", "recommended_weapons": ["Sacrificial Sword", "Favonius Sword"]},
    "mika": {"weapon_type": "Polearm", "recommended_weapons": ["Favonius Lance", "Prototype Starglitter"]},
    "qiqi": {"weapon_type": "Sword", "recommended_weapons": ["Sacrificial Sword", "Favonius Sword"]},
    "rosaria": {"weapon_type": "Polearm", "recommended_weapons": ["Deathmatch", "Favonius Lance"]},
    "shenhe": {"weapon_type": "Polearm", "recommended_weapons": ["Calamity Queller", "Deathmatch"]},
    "skirk": {"weapon_type": "Sword", "recommended_weapons": ["The Black Sword", "Mistsplitter Reforged"]},
    "wriothesley": {"weapon_type": "Catalyst", "recommended_weapons": ["Tome of the Eternal Flow", "Prototype Amber"]},

    # ===== GEO =====
    "albedo": {"weapon_type": "Sword", "recommended_weapons": ["Cinnabar Spindle", "Iron Sting"]},
    "chiori": {"weapon_type": "Sword", "recommended_weapons": ["Uraku Misugiri", "Iron Sting"]},
    "gorou": {"weapon_type": "Bow", "recommended_weapons": ["Sacrificial Bow", "Favonius Warbow"]},
    "itto": {"weapon_type": "Claymore", "recommended_weapons": ["Redhorn Stonethresher", "Serpent Spine"]},
    # CORRECTED: confirmed Polearm (GameWith's guide explicitly discusses
    # "DEF polearms" for her build, and independently verified via Enka's
    # own game data: WeaponType WEAPON_POLE). Was previously miscatalogued
    # here as Claymore.
    "kachina": {"weapon_type": "Polearm", "recommended_weapons": ["Favonius Lance", "Prototype Starglitter"]},
    "navia": {"weapon_type": "Claymore", "recommended_weapons": ["Crimson Moon's Semblance", "Serpent Spine"]},
    "ningguang": {"weapon_type": "Catalyst", "recommended_weapons": ["Lost Prayer to the Sacred Winds", "Sacrificial Fragments"]},
    "noelle": {"weapon_type": "Claymore", "recommended_weapons": ["Redhorn Stonethresher", "Serpent Spine"]},
    # LOWER CONFIDENCE: Xilonen's weapon type -- believed Sword, worth spot-checking.
    "xilonen": {"weapon_type": "Sword", "recommended_weapons": ["Absolution", "Iron Sting"]},
    "yunjin": {"weapon_type": "Polearm", "recommended_weapons": ["Favonius Lance", "Deathmatch"]},

    # ===== TRAVELER =====
    "traveler": {"weapon_type": "Sword", "recommended_weapons": ["Iron Sting", "Sacrificial Sword"]},
    "anemotraveler": {"weapon_type": "Sword", "recommended_weapons": ["Freedom-Sworn", "Iron Sting"]},
    "geotraveler": {"weapon_type": "Sword", "recommended_weapons": ["Iron Sting", "Favonius Sword"]},
    "electrotraveler": {"weapon_type": "Sword", "recommended_weapons": ["Sacrificial Sword", "Favonius Sword"]},
    "dendrotraveler": {"weapon_type": "Sword", "recommended_weapons": ["Sacrificial Sword", "Favonius Sword"]},
    "hydrotraveler": {"weapon_type": "Sword", "recommended_weapons": ["Iron Sting", "Sacrificial Sword"]},
    "pyrotraveler": {"weapon_type": "Sword", "recommended_weapons": ["Iron Sting", "Sacrificial Sword"]},

    # ===== NEW CHARACTERS (post-Jan-2026 cutoff, researched live) =====
    "ineffa": {"weapon_type": "Polearm", "recommended_weapons": ["Fractured Halo", "Staff of the Scarlet Sands"]},
    "illuga": {"weapon_type": "Polearm", "recommended_weapons": ["Favonius Lance", "Kitain Cross Spear"]},
    "zibai": {"weapon_type": "Sword", "recommended_weapons": ["Absolution", "Iron Sting"]},
    "columbina": {"weapon_type": "Catalyst", "recommended_weapons": ["Nocturne's Curtain Call", "Sacrificial Jade"]},
    "lohen": {"weapon_type": "Polearm", "recommended_weapons": ["Disaster and Remorse", "Primordial Jade Winged-Spear"]},
    "linnea": {"weapon_type": "Bow", "recommended_weapons": ["Golden Frostbound Oath", "Aqua Simulacra"]},
    "varka": {"weapon_type": "Claymore", "recommended_weapons": ["Gest of the Mighty Wolf", "A Thousand Blazing Suns"]},
    "nicole": {"weapon_type": "Catalyst", "recommended_weapons": ["Prototype Amber", "Sacrificial Fragments"]},
    "prune": {"weapon_type": "Claymore", "recommended_weapons": ["Favonius Greatsword", "Prototype Starglitter"]},
    "aloy": {"weapon_type": "Bow", "recommended_weapons": ["Thundering Pulse", "The Stringless"]},
    "durin": {"weapon_type": "Sword", "recommended_weapons": ["Athame Artis", "Favonius Sword"]},
    "jahoda": {"weapon_type": "Bow", "recommended_weapons": ["Elegy for the End", "Favonius Warbow"]},
}
