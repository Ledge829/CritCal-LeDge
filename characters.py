"""
Character-specific configuration for CritiCal.

This file contains all data that differs between characters:
- aliases
- stat scaling
- crit ratio targets
- ER exceptions
- archetypes and stat benchmarks
- future-proofing mechanic hooks
"""
from typing import Dict, Any

CRIT_RATIO_TARGET: float = 2.0

DEFAULT_CHARACTER_CONFIG: Dict[str, Any] = {
    "scaling": "atk",
    "crit_ratio_target": CRIT_RATIO_TARGET,
    "high_er_allowed": False,
    "build_title": "Standard DPS / Support",
    "benchmarks": {},
    # Future-proofing extension hooks
    "ignore_high_ratio_warning": False,
    "freeze_build": False,
    "special_crit_logic": False
}

CHARACTER_CONFIGS: Dict[str, Dict[str, Any]] = {
    # EM scalers
    "nahida": {
        "scaling": "em", 
        "build_title": "Reaction Driver / Off-field DPS",
        "benchmarks": {"elemental_mastery": 800.0}
    },
    "kazuha": {
        "scaling": "em", 
        "build_title": "VV Swirl Support",
        "benchmarks": {"elemental_mastery": 900.0}
    },
    "sucrose": {
        "scaling": "em", 
        "build_title": "EM Buffing Support",
        "benchmarks": {"elemental_mastery": 700.0}
    },

    # HP scalers
    "hutao": {
        "scaling": "hp", 
        "build_title": "Vaporize Main DPS",
        "benchmarks": {"hp": 30000.0, "elemental_mastery": 100.0}
    },
    "yelan": {
        "scaling": "hp", 
        "build_title": "Off-field Hydro DPS / Enabler",
        "benchmarks": {"hp": 32000.0, "energy_recharge": 180.0}
    },
    "neuvillette": {
        "scaling": "hp",
        "crit_ratio_target": 4.2, # High target due to Marechaussee Hunter artifact set
        "build_title": "Hypercarry Charged Attacker",
        "benchmarks": {"hp": 35000.0},
        "ignore_high_ratio_warning": True # Naturally stacks extreme Crit DMG
    },
    "flins": {
        "crit_ratio_target": 4.9, # Confirmed via real Akasha top-97th-percentile build data
        "build_title": "Hypercarry Physical/Elemental DPS",
        "benchmarks": {"atk": 2000.0},
        "ignore_high_ratio_warning": True # Kit-driven temporary Crit buffs make raw panel ratio misleading
    },

    # DEF scalers
    "itto": {
        "scaling": "def",
        "crit_ratio_target": 2.2,
        "build_title": "Geo Hypercarry DPS",
        "benchmarks": {"defense": 2200.0}
    },
    "albedo": {
        "scaling": "def", 
        "build_title": "Off-field Geo DPS",
        "benchmarks": {"defense": 2000.0}
    },
    "chiori": {
        "scaling": "def", 
        "build_title": "Dual-Sword Off-field DPS",
        "benchmarks": {"defense": 2100.0}
    },
    "noelle": {
        "scaling": "def", 
        "build_title": "Main DPS / Shield Support",
        "benchmarks": {"defense": 2000.0}
    },

    # Burst-reliant characters
    "raiden": {
        "high_er_allowed": True, 
        "build_title": "Hypercarry / Burst Support",
        "benchmarks": {"energy_recharge": 250.0, "atk": 1800.0}
    },
    "mona": {
        "high_er_allowed": True, 
        "build_title": "Omen Nuke Support",
        "benchmarks": {"energy_recharge": 200.0}
    },
    "faruzan": {
        "high_er_allowed": True, 
        "build_title": "Anemo Dedicated Support",
        "benchmarks": {"energy_recharge": 240.0}
    },

    # Cryo Blizzard Strayer Hooks
    "ayaka": {
        "scaling": "atk",
        "build_title": "Freeze Premium Main DPS",
        "benchmarks": {"atk": 2000.0, "energy_recharge": 130.0},
        "freeze_build": True,
        "ignore_high_ratio_warning": True # Free Crit Rate from Blizzard Strayer means high ratio is normal
    },
    "ganyu": {
        "scaling": "atk",
        "build_title": "Melt / Freeze Archer DPS",
        "benchmarks": {"atk": 2100.0},
        "freeze_build": True,
        "ignore_high_ratio_warning": True
    }
}

# Strictly translating non-standard spellings to canonical keys
CHARACTER_ALIASES: Dict[str, str] = {
    "raidenshogun": "raiden", "ei": "raiden",
    "scara": "wanderer", "scaramouche": "wanderer",
    "tartaglia": "childe",
    "arle": "arlecchino", "father": "arlecchino",
    "kaedeharakazuha": "kazuha",
    "kamisatoayaka": "ayaka",
    "kamisatoayato": "ayato",
    "miko": "yaemiko",
    "kuki": "kukishinobu", "shinobu": "kukishinobu",
    "heizou": "shikanoinheizou",
    "neuvi": "neuvillette", "neuv": "neuvillette",
    "cloudretainer": "xianyun",
    "aratakiitto": "itto"
}

def normalize_character(name: str) -> str:
    """Normalize user input into a canonical character key without crashing."""
    if not isinstance(name, str):
        return ""
    return (
        name.lower()
        .strip()
        .replace(" ", "")
        .replace("-", "")
        .replace("'", "")
        .replace("\r", "")
        .replace("\n", "")
    )

def get_character_config(character: str) -> dict:
    """
    Returns the merged configuration for a character.
    Unknown characters fall back to DEFAULT_CHARACTER_CONFIG.
    """
    normalized = normalize_character(character)
    normalized = CHARACTER_ALIASES.get(normalized, normalized)

    config = DEFAULT_CHARACTER_CONFIG.copy()
    config.update(CHARACTER_CONFIGS.get(normalized, {}))

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
