"""
Character-specific configuration for CritiCal.

This file acts as the character database for the scoring engine.

Contains:
- aliases
- stat scaling
- crit ratio targets
- ER exceptions
- archetypes
- benchmark goals
- future-proofing flags
"""

from typing import Dict, Any

CRIT_RATIO_TARGET: float = 2.0

DEFAULT_CHARACTER_CONFIG: Dict[str, Any] = {
    "scaling": "atk",
    "crit_ratio_target": CRIT_RATIO_TARGET,
    "high_er_allowed": False,

    "build_title": "Standard DPS / Support",

    "benchmarks": {},

    # Future hooks
    "ignore_high_ratio_warning": False,
    "freeze_build": False,
    "special_crit_logic": False,
}

CHARACTER_CONFIGS: Dict[str, Dict[str, Any]] = {

# ==========================================================
# PYRO
# ==========================================================

    "arlecchino": {
        "build_title": "Hypercarry Pyro DPS",
        "benchmarks": {
            "atk": 2200.0,
        },
    },

    "bennett": {
        "high_er_allowed": True,
        "build_title": "ATK Buffer / Burst Support",
        "benchmarks": {
            "energy_recharge": 220.0,
        },
    },

    "chevreuse": {
        "high_er_allowed": True,
        "build_title": "Overload Support",
        "benchmarks": {
            "hp": 35000.0,
            "energy_recharge": 180.0,
        },
    },

    "dehya": {
        "build_title": "Bruiser / Defensive DPS",
        "benchmarks": {
            "hp": 35000.0,
            "atk": 1700.0,
        },
    },

    "diluc": {
        "build_title": "Pyro Hypercarry",
        "benchmarks": {
            "atk": 2100.0,
            "elemental_mastery": 100.0,
        },
    },

    "gaming": {
        "build_title": "Plunging DPS",
        "benchmarks": {
            "atk": 2100.0,
            "elemental_mastery": 120.0,
        },
    },

    "hutao": {
        "scaling": "hp",
        "build_title": "Vaporize Main DPS",
        "benchmarks": {
            "hp": 30000.0,
            "elemental_mastery": 100.0,
        },
    },

    "klee": {
        "build_title": "On-field Pyro DPS",
        "benchmarks": {
            "atk": 2100.0,
        },
    },

    "lyney": {
        "build_title": "Mono Pyro Charged DPS",
        "benchmarks": {
            "atk": 2200.0,
        },
    },

    "mavuika": {
        "build_title": "Pyro Hypercarry",
        "benchmarks": {
            "atk": 2200.0,
            "energy_recharge": 140.0,
        },
    },

    "thoma": {
        "scaling": "hp",
        "high_er_allowed": True,
        "build_title": "Shield Support / Burgeon",
        "benchmarks": {
            "hp": 32000.0,
            "energy_recharge": 220.0,
        },
    },

    "xiangling": {
        "high_er_allowed": True,
        "build_title": "Off-field Pyro DPS",
        "benchmarks": {
            "energy_recharge": 220.0,
            "atk": 1600.0,
        },
    },

    "xinyan": {
        "build_title": "Physical DPS / Shield",
        "benchmarks": {
            "atk": 2000.0,
        },
    },

# ==========================================================
# HYDRO
# ==========================================================

    "barbara": {
        "scaling": "hp",
        "build_title": "Healing Support",
        "benchmarks": {
            "hp": 30000.0,
            "energy_recharge": 180.0,
        },
    },

    "candace": {
        "scaling": "hp",
        "high_er_allowed": True,
        "build_title": "Hydro Infusion Support",
        "benchmarks": {
            "hp": 32000.0,
            "energy_recharge": 200.0,
        },
    },

    "childe": {
        "build_title": "On-field Hydro DPS",
        "benchmarks": {
            "atk": 2100.0,
        },
    },

    "furina": {
        "scaling": "hp",
        "high_er_allowed": True,
        "build_title": "Universal Buffer / Off-field Hydro",
        "benchmarks": {
            "hp": 40000.0,
            "energy_recharge": 180.0,
        },
    },

    "kokomi": {
        "scaling": "hp",
        "build_title": "Healing Driver",
        "benchmarks": {
            "hp": 40000.0,
            "energy_recharge": 180.0,
        },
    },

    "mona": {
        "high_er_allowed": True,
        "build_title": "Omen Nuke Support",
        "benchmarks": {
            "energy_recharge": 200.0,
        },
    },

    "mualani": {
        "scaling": "hp",
        "build_title": "Hydro Hypercarry",
        "benchmarks": {
            "hp": 35000.0,
            "elemental_mastery": 100.0,
        },
    },

    "neuvillette": {
        "scaling": "hp",
        "crit_ratio_target": 4.2,
        "build_title": "Hypercarry Charged Attacker",
        "benchmarks": {
            "hp": 35000.0,
        },
        "ignore_high_ratio_warning": True,
    },

    "nilou": {
        "scaling": "hp",
        "build_title": "Bloom Enabler",
        "benchmarks": {
            "hp": 55000.0,
        },
    },

    "sigewinne": {
        "scaling": "hp",
        "build_title": "Healing Support",
        "benchmarks": {
            "hp": 45000.0,
        },
    },

    "xingqiu": {
        "high_er_allowed": True,
        "build_title": "Off-field Hydro DPS",
        "benchmarks": {
            "energy_recharge": 220.0,
            "atk": 1600.0,
        },
    },

    "yelan": {
        "scaling": "hp",
        "build_title": "Off-field Hydro DPS / Enabler",
        "benchmarks": {
            "hp": 32000.0,
            "energy_recharge": 180.0,
        },
    },

# ==========================================================
# ANEMO
# ==========================================================

    "chasca": {
        "build_title": "Aerial Hypercarry DPS",
        "benchmarks": {
            "atk": 2100.0,
        },
    },

    "faruzan": {
        "high_er_allowed": True,
        "build_title": "Anemo Dedicated Support",
        "benchmarks": {
            "energy_recharge": 240.0,
        },
    },

    "heizou": {
        "build_title": "Catalyst Driver / Burst DPS",
        "benchmarks": {
            "atk": 1900.0,
            "elemental_mastery": 100.0,
        },
    },

    "jean": {
        "build_title": "Healing Support / Anemo Driver",
        "benchmarks": {
            "atk": 2000.0,
            "energy_recharge": 160.0,
        },
    },

    "kazuha": {
        "scaling": "em",
        "build_title": "VV Swirl Support",
        "benchmarks": {
            "elemental_mastery": 900.0,
        },
    },

    "lanyan": {
        "scaling": "atk",
        "build_title": "Anemo Shield Support",
        "benchmarks": {
            "atk": 1800.0,
            "energy_recharge": 180.0,
        },
    },

    "lynette": {
        "build_title": "Quick-Swap Anemo Support",
        "benchmarks": {
            "atk": 1800.0,
            "energy_recharge": 180.0,
        },
    },

    "sayu": {
        "scaling": "em",
        "build_title": "Healing Swirl Support",
        "benchmarks": {
            "elemental_mastery": 700.0,
            "energy_recharge": 180.0,
        },
    },

    "sucrose": {
        "scaling": "em",
        "build_title": "EM Buffing Support",
        "benchmarks": {
            "elemental_mastery": 700.0,
        },
    },

    "venti": {
        "scaling": "em",
        "high_er_allowed": True,
        "build_title": "Crowd Control Support",
        "benchmarks": {
            "elemental_mastery": 800.0,
            "energy_recharge": 180.0,
        },
    },

    "wanderer": {
        "build_title": "Hypercarry Catalyst DPS",
        "benchmarks": {
            "atk": 2100.0,
        },
    },

    "xianyun": {
        "scaling": "atk",
        "build_title": "Plunge Support / Healer",
        "benchmarks": {
            "atk": 3000.0,
            "energy_recharge": 180.0,
        },
    },

# ==========================================================
# ELECTRO
# ==========================================================

    "beidou": {
        "high_er_allowed": True,
        "build_title": "Burst Sub DPS",
        "benchmarks": {
            "atk": 1800.0,
            "energy_recharge": 180.0,
        },
    },

    "clorinde": {
        "build_title": "Aggravate / Electro DPS",
        "benchmarks": {
            "atk": 2100.0,
            "elemental_mastery": 100.0,
        },
    },

    "cyno": {
        "build_title": "Quickbloom Hypercarry",
        "benchmarks": {
            "atk": 1800.0,
            "elemental_mastery": 250.0,
        },
    },

    "dori": {
        "high_er_allowed": True,
        "build_title": "Battery / Healing Support",
        "benchmarks": {
            "energy_recharge": 220.0,
            "hp": 30000.0,
        },
    },

    "fischl": {
        "build_title": "Off-field Electro DPS",
        "benchmarks": {
            "atk": 2000.0,
            "elemental_mastery": 80.0,
        },
    },

    "flins": {
        "scaling": "atk",
        "crit_ratio_target": 4.9,
        "build_title": "On-Field Lunar Electro DPS",
        "benchmarks": {
            "atk": 2000.0,
            "elemental_mastery": 200.0,
        },
        "ignore_high_ratio_warning": True,
    },

    "keqing": {
        "build_title": "Aggravate Main DPS",
        "benchmarks": {
            "atk": 2000.0,
            "elemental_mastery": 150.0,
        },
    },

    "kukishinobu": {
        "scaling": "em",
        "build_title": "Hyperbloom Trigger",
        "benchmarks": {
            "elemental_mastery": 1000.0,
        },
    },

    "lisa": {
        "build_title": "Electro Support / Aggravate",
        "benchmarks": {
            "atk": 1800.0,
            "elemental_mastery": 150.0,
        },
    },

    "ororon": {
        "build_title": "Electro Support",
        "benchmarks": {
            "atk": 1800.0,
            "energy_recharge": 180.0,
        },
    },

    "raiden": {
        "high_er_allowed": True,
        "build_title": "Hypercarry / Burst Support",
        "benchmarks": {
            "energy_recharge": 250.0,
            "atk": 1800.0,
        },
    },

    "razor": {
        "build_title": "Physical / Aggravate DPS",
        "benchmarks": {
            "atk": 2100.0,
        },
    },

    "sara": {
        "high_er_allowed": True,
        "build_title": "ATK Buffer / Burst Support",
        "benchmarks": {
            "energy_recharge": 200.0,
        },
    },

    "sethos": {
        "build_title": "Charged Shot Electro DPS",
        "benchmarks": {
            "elemental_mastery": 300.0,
        },
    },

    "yaemiko": {
        "build_title": "Turret Sub DPS",
        "benchmarks": {
            "atk": 2000.0,
            "elemental_mastery": 100.0,
        },
    },

# ==========================================================
# DENDRO
# ==========================================================

    "alhaitham": {
        "scaling": "em",
        "build_title": "Spread Hypercarry",
        "benchmarks": {
            "elemental_mastery": 350.0,
            "atk": 1600.0,
        },
    },

    "baizhu": {
        "scaling": "hp",
        "high_er_allowed": True,
        "build_title": "Healing Support / Dendro Enabler",
        "benchmarks": {
            "hp": 50000.0,
            "energy_recharge": 180.0,
        },
    },

    "collei": {
        "high_er_allowed": True,
        "build_title": "Off-field Dendro Support",
        "benchmarks": {
            "energy_recharge": 200.0,
        },
    },

    "emilie": {
        "build_title": "Burning Sub DPS",
        "benchmarks": {
            "atk": 2200.0,
        },
    },

    "kaveh": {
        "scaling": "em",
        "build_title": "Bloom Driver",
        "benchmarks": {
            "elemental_mastery": 700.0,
            "energy_recharge": 180.0,
        },
    },

    "kinich": {
        "build_title": "Burning Hypercarry",
        "benchmarks": {
            "atk": 2200.0,
            "elemental_mastery": 100.0,
        },
    },

    "nahida": {
        "scaling": "em",
        "build_title": "Reaction Driver / Off-field DPS",
        "benchmarks": {
            "elemental_mastery": 800.0,
        },
    },

    "tighnari": {
        "scaling": "em",
        "build_title": "Spread Charged Shot DPS",
        "benchmarks": {
            "elemental_mastery": 350.0,
            "atk": 1700.0,
        },
    },

    "yaoyao": {
        "scaling": "hp",
        "high_er_allowed": True,
        "build_title": "Healing Support",
        "benchmarks": {
            "hp": 35000.0,
            "energy_recharge": 180.0,
        },
    },

# ==========================================================
# CRYO
# ==========================================================

    "ayaka": {
        "build_title": "Freeze Premium Main DPS",
        "benchmarks": {
            "atk": 2000.0,
            "energy_recharge": 130.0,
        },
        "freeze_build": True,
        "ignore_high_ratio_warning": True,
    },

    "charlotte": {
        "high_er_allowed": True,
        "build_title": "Healing Support",
        "benchmarks": {
            "atk": 1800.0,
            "energy_recharge": 200.0,
        },
    },

    "chongyun": {
        "build_title": "Cryo Infusion Support",
        "benchmarks": {
            "atk": 1800.0,
            "energy_recharge": 160.0,
        },
    },

    "citlali": {
        "scaling": "def",
        "build_title": "Cryo Reaction Support",
        "benchmarks": {
            "defense": 2200.0,
            "energy_recharge": 180.0,
        },
    },

    "diona": {
        "scaling": "hp",
        "high_er_allowed": True,
        "build_title": "Shield / Healing Support",
        "benchmarks": {
            "hp": 30000.0,
            "energy_recharge": 200.0,
        },
    },

    "eula": {
        "build_title": "Physical Hypercarry",
        "benchmarks": {
            "atk": 2200.0,
            "energy_recharge": 140.0,
        },
    },

    "freminet": {
        "build_title": "Physical / Cryo DPS",
        "benchmarks": {
            "atk": 2000.0,
        },
    },

    "ganyu": {
        "build_title": "Melt / Freeze Archer DPS",
        "benchmarks": {
            "atk": 2100.0,
        },
        "freeze_build": True,
        "ignore_high_ratio_warning": True,
    },

    "kaeya": {
        "build_title": "Cryo Sub DPS",
        "benchmarks": {
            "atk": 1900.0,
            "energy_recharge": 160.0,
        },
    },

    "layla": {
        "scaling": "hp",
        "build_title": "Shield Support",
        "benchmarks": {
            "hp": 40000.0,
        },
    },

    "mika": {
        "high_er_allowed": True,
        "build_title": "Physical Support",
        "benchmarks": {
            "energy_recharge": 200.0,
            "hp": 30000.0,
        },
    },

    "qiqi": {
        "build_title": "Healing Support",
        "benchmarks": {
            "atk": 2000.0,
        },
    },

    "rosaria": {
        "build_title": "Cryo Burst DPS / Crit Support",
        "benchmarks": {
            "atk": 1900.0,
            "energy_recharge": 160.0,
        },
    },

    "shenhe": {
        "build_title": "Cryo Dedicated Buffer",
        "benchmarks": {
            "atk": 3500.0,
            "energy_recharge": 180.0,
        },
    },

    "skirk": {
        "build_title": "Flexible Cryo DPS",
        "benchmarks": {
            "atk": 2200.0,
        },
    },

    "wriothesley": {
        "build_title": "Cryo Catalyst Hypercarry",
        "benchmarks": {
            "atk": 2100.0,
        },
    },

# ==========================================================
# GEO
# ==========================================================

    "albedo": {
        "scaling": "def",
        "build_title": "Off-field Geo DPS",
        "benchmarks": {
            "defense": 2000.0,
        },
    },

    "chiori": {
        "scaling": "def",
        "build_title": "Dual-Sword Off-field DPS",
        "benchmarks": {
            "defense": 2100.0,
        },
    },

    "gorou": {
        "scaling": "def",
        "high_er_allowed": True,
        "build_title": "Geo DEF Buffer",
        "benchmarks": {
            "defense": 1800.0,
            "energy_recharge": 220.0,
        },
    },

    "itto": {
        "scaling": "def",
        "crit_ratio_target": 2.2,
        "build_title": "Geo Hypercarry DPS",
        "benchmarks": {
            "defense": 2200.0,
        },
    },

    "kachina": {
        "scaling": "def",
        "build_title": "Geo Support",
        "benchmarks": {
            "defense": 2000.0,
            "energy_recharge": 180.0,
        },
    },

    "navia": {
        "build_title": "Crystalize Hypercarry",
        "benchmarks": {
            "atk": 2400.0,
        },
    },

    "ningguang": {
        "build_title": "Geo Catalyst DPS",
        "benchmarks": {
            "atk": 2000.0,
        },
    },

    "noelle": {
        "scaling": "def",
        "build_title": "Main DPS / Shield Support",
        "benchmarks": {
            "defense": 2000.0,
        },
    },

    "xilonen": {
        "scaling": "def",
        "build_title": "Geo Support / RES Shred",
        "benchmarks": {
            "defense": 2600.0,
            "energy_recharge": 180.0,
        },
    },

    "yunjin": {
        "scaling": "def",
        "high_er_allowed": True,
        "build_title": "Normal Attack Buffer",
        "benchmarks": {
            "defense": 2500.0,
            "energy_recharge": 220.0,
        },
    },

# ==========================================================
# TRAVELER
# ==========================================================

    "traveler": {
        "build_title": "Flexible Traveler Build",
        "benchmarks": {
            "atk": 1800.0,
        },
    },

    "anemotraveler": {
        "scaling": "em",
        "build_title": "Swirl Traveler",
        "benchmarks": {
            "elemental_mastery": 700.0,
            "energy_recharge": 180.0,
        },
    },

    "geotraveler": {
        "build_title": "Geo Burst DPS",
        "benchmarks": {
            "atk": 1900.0,
            "energy_recharge": 160.0,
        },
    },

    "electrotraveler": {
        "high_er_allowed": True,
        "build_title": "Battery Support",
        "benchmarks": {
            "energy_recharge": 240.0,
        },
    },

    "dendrotraveler": {
        "high_er_allowed": True,
        "build_title": "Dendro Support",
        "benchmarks": {
            "energy_recharge": 220.0,
        },
    },

    "hydrotraveler": {
        "build_title": "Hydro On-field DPS",
        "benchmarks": {
            "atk": 1900.0,
        },
    },

    "pyrotraveler": {
        "build_title": "Pyro DPS",
        "benchmarks": {
            "atk": 2000.0,
        },
    },

    "unknown": {
        "build_title": "Unknown Character",
        "benchmarks": {},
    },
}

# ==========================================================
# CHARACTER ALIASES
# ==========================================================

CHARACTER_ALIASES: Dict[str, str] = {

    # PYRO
    "arle": "arlecchino",
    "father": "arlecchino",
    "benny": "bennett",
    "benett": "bennett",
    "hu": "hutao",
    "hu_tao": "hutao",
    "hutao": "hutao",
    "xl": "xiangling",

    # HYDRO
    "tartaglia": "childe",
    "ajax": "childe",
    "neuvi": "neuvillette",
    "neuv": "neuvillette",
    "xq": "xingqiu",

    # ANEMO
    "scara": "wanderer",
    "scaramouche": "wanderer",
    "balladeer": "wanderer",
    "birdmom": "xianyun",
    "cloudretainer": "xianyun",
    "kaedeharakazuha": "kazuha",

    # ELECTRO
    "ei": "raiden",
    "raidenei": "raiden",
    "raidenshogun": "raiden",
    "shogun": "raiden",
    "miko": "yaemiko",
    "yae": "yaemiko",
    "kuki": "kukishinobu",
    "shinobu": "kukishinobu",
    "kujousara": "sara",

    # DENDRO
    "dmc": "dendrotraveler",

    # CRYO
    "ayaya": "ayaka",
    "kamisatoayaka": "ayaka",

    # GEO
    "aratakiitto": "itto",
    "yunjin": "yunjin",

    # TRAVELER
    "aether": "traveler",
    "lumine": "traveler",
    "mc": "traveler",
    "maincharacter": "traveler",
    "anemomc": "anemotraveler",
    "geomc": "geotraveler",
    "electromc": "electrotraveler",
    "dendromc": "dendrotraveler",
    "hydromc": "hydrotraveler",
    "pyrotraveler": "pyrotraveler",
}


# ==========================================================
# NORMALIZATION
# ==========================================================

def normalize_character(name: str) -> str:
    """
    Converts nearly any user input into a canonical key.
    """
    if not isinstance(name, str):
        return ""

    return (
        name.lower()
        .strip()
        .replace(" ", "")
        .replace("-", "")
        .replace("_", "")
        .replace("'", "")
        .replace(".", "")
        .replace("\r", "")
        .replace("\n", "")
    )


# ==========================================================
# CONFIG LOOKUP
# ==========================================================

def get_character_config(character: str) -> Dict[str, Any]:
    """
    Returns a merged configuration.
    Unknown characters automatically receive the default config.
    """
    normalized = normalize_character(character)
    canonical = CHARACTER_ALIASES.get(normalized, normalized)

    config = DEFAULT_CHARACTER_CONFIG.copy()
    if canonical in CHARACTER_CONFIGS:
        config.update(CHARACTER_CONFIGS[canonical])

    return config


# ==========================================================
# OPTIONAL HELPERS
# ==========================================================

def character_exists(character: str) -> bool:
    """
    Returns True if the character exists in the database.
    """
    normalized = normalize_character(character)
    canonical = CHARACTER_ALIASES.get(normalized, normalized)
    return canonical in CHARACTER_CONFIGS


def get_all_characters():
    """
    Returns every canonical character key.
    """
    return sorted(CHARACTER_CONFIGS.keys())


def get_aliases(character: str):
    """
    Returns every alias pointing to a character.
    """
    normalized = normalize_character(character)
    canonical = CHARACTER_ALIASES.get(normalized, normalized)

    return sorted(
        alias
        for alias, target in CHARACTER_ALIASES.items()
        if target == canonical
)
