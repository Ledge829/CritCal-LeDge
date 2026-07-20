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
- element, rarity, region, roles metadata
"""

from typing import Dict, Any

CRIT_RATIO_TARGET: float = 2.0

DEFAULT_CHARACTER_CONFIG: Dict[str, Any] = {
    "element": "unknown",
    "rarity": 4,
    "region": "unknown",
    "main_scaling": "atk",
    "roles": ["Unknown"],
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
        "element": "pyro",
        "rarity": 5,
        "region": "snezhnaya",
        "main_scaling": "atk",
        "roles": ["Main DPS"],
        "portrait": "https://enka.network/ui/UI_AvatarIcon_Arlecchino.png",
        "build_title": "Hypercarry Pyro DPS",
        "benchmarks": {
            "atk": 2200.0,
        },
    },

    "bennett": {
        "element": "pyro",
        "rarity": 4,
        "region": "mondstadt",
        "main_scaling": "atk",
        "roles": ["Support", "Healer", "Buffer"],
        "portrait": "https://enka.network/ui/UI_AvatarIcon_Bennett.png",
        "high_er_allowed": True,
        "build_title": "ATK Buffer / Burst Support",
        "benchmarks": {
            "energy_recharge": 220.0,
        },
    },

    "chevreuse": {
        "element": "pyro",
        "rarity": 4,
        "region": "fontaine",
        "main_scaling": "hp",
        "roles": ["Support", "Healer"],
        "portrait": "https://enka.network/ui/UI_AvatarIcon_Chevreuse.png",
        "high_er_allowed": True,
        "build_title": "Overload Support",
        "benchmarks": {
            "hp": 35000.0,
            "energy_recharge": 180.0,
        },
    },

    "dehya": {
        "element": "pyro",
        "rarity": 5,
        "region": "sumeru",
        "main_scaling": "hp",
        "roles": ["Sub DPS", "Support"],
        "portrait": "https://enka.network/ui/UI_AvatarIcon_Dehya.png",
        "build_title": "Bruiser / Defensive DPS",
        "benchmarks": {
            "hp": 35000.0,
            "atk": 1700.0,
        },
    },

    "diluc": {
        "element": "pyro",
        "rarity": 5,
        "region": "mondstadt",
        "main_scaling": "atk",
        "roles": ["Main DPS"],
        "portrait": "https://enka.network/ui/UI_AvatarIcon_Diluc.png",
        "build_title": "Pyro Hypercarry",
        "benchmarks": {
            "atk": 2100.0,
            "elemental_mastery": 100.0,
        },
    },

    "gaming": {
        "element": "pyro",
        "rarity": 4,
        "region": "liyue",
        "main_scaling": "atk",
        "roles": ["Main DPS"],
        "portrait": "https://enka.network/ui/UI_AvatarIcon_Gaming.png",
        "build_title": "Plunging DPS",
        "benchmarks": {
            "atk": 2100.0,
            "elemental_mastery": 120.0,
        },
    },

    "hutao": {
        "element": "pyro",
        "rarity": 5,
        "region": "liyue",
        "main_scaling": "hp",
        "roles": ["Main DPS"],
        "portrait": "https://enka.network/ui/UI_AvatarIcon_Hutao.png",
        "scaling": "hp",
        "build_title": "Vaporize Main DPS",
        "benchmarks": {
            "hp": 30000.0,
            "elemental_mastery": 100.0,
        },
    },

    "klee": {
        "element": "pyro",
        "rarity": 5,
        "region": "mondstadt",
        "main_scaling": "atk",
        "roles": ["Main DPS"],
        "portrait": "https://enka.network/ui/UI_AvatarIcon_Klee.png",
        "build_title": "On-field Pyro DPS",
        "benchmarks": {
            "atk": 2100.0,
        },
    },

    "lyney": {
        "element": "pyro",
        "rarity": 5,
        "region": "fontaine",
        "main_scaling": "atk",
        "roles": ["Main DPS"],
        "portrait": "https://enka.network/ui/UI_AvatarIcon_Liney.png",
        "build_title": "Mono Pyro Charged DPS",
        "benchmarks": {
            "atk": 2200.0,
        },
    },

    "mavuika": {
        "element": "pyro",
        "rarity": 5,
        "region": "natlan",
        "main_scaling": "atk",
        "roles": ["Main DPS"],
        "portrait": "https://enka.network/ui/UI_AvatarIcon_Mavuika.png",
        "build_title": "Pyro Hypercarry",
        "benchmarks": {
            "atk": 2200.0,
            "energy_recharge": 140.0,
        },
    },

    "thoma": {
        "element": "pyro",
        "rarity": 4,
        "region": "inazuma",
        "main_scaling": "hp",
        "roles": ["Support", "Shielder"],
        "portrait": "https://enka.network/ui/UI_AvatarIcon_Tohma.png",
        "scaling": "hp",
        "high_er_allowed": True,
        "build_title": "Shield Support / Burgeon",
        "benchmarks": {
            "hp": 32000.0,
            "energy_recharge": 220.0,
        },
    },

    "xiangling": {
        "element": "pyro",
        "rarity": 4,
        "region": "liyue",
        "main_scaling": "atk",
        "roles": ["Sub DPS"],
        "portrait": "https://enka.network/ui/UI_AvatarIcon_Xiangling.png",
        "high_er_allowed": True,
        "build_title": "Off-field Pyro DPS",
        "benchmarks": {
            "energy_recharge": 220.0,
            "atk": 1600.0,
        },
    },

    "xinyan": {
        "element": "pyro",
        "rarity": 4,
        "region": "liyue",
        "main_scaling": "atk",
        "roles": ["Main DPS", "Shielder", "Support"],
        "portrait": "https://enka.network/ui/UI_AvatarIcon_Xinyan.png",
        "build_title": "Physical DPS / Shield",
        "benchmarks": {
            "atk": 2000.0,
        },
    },

# ==========================================================
# HYDRO
# ==========================================================

    "barbara": {
        "element": "hydro",
        "rarity": 4,
        "region": "mondstadt",
        "main_scaling": "hp",
        "roles": ["Healer", "Support"],
        "portrait": "https://enka.network/ui/UI_AvatarIcon_Barbara.png",
        "scaling": "hp",
        "build_title": "Healing Support",
        "benchmarks": {
            "hp": 30000.0,
            "energy_recharge": 180.0,
        },
    },

    "candace": {
        "element": "hydro",
        "rarity": 4,
        "region": "sumeru",
        "main_scaling": "hp",
        "roles": ["Support", "Buffer"],
        "portrait": "https://enka.network/ui/UI_AvatarIcon_Candace.png",
        "scaling": "hp",
        "high_er_allowed": True,
        "build_title": "Hydro Infusion Support",
        "benchmarks": {
            "hp": 32000.0,
            "energy_recharge": 200.0,
        },
    },

    "childe": {
        "element": "hydro",
        "rarity": 5,
        "region": "snezhnaya",
        "main_scaling": "atk",
        "roles": ["Main DPS"],
        "portrait": "https://enka.network/ui/UI_AvatarIcon_Tartaglia.png",
        "build_title": "On-field Hydro DPS",
        "benchmarks": {
            "atk": 2100.0,
        },
    },

    "furina": {
        "element": "hydro",
        "rarity": 5,
        "region": "fontaine",
        "main_scaling": "hp",
        "roles": ["Sub DPS", "Support", "Buffer"],
        "portrait": "https://enka.network/ui/UI_AvatarIcon_Furina.png",
        "scaling": "hp",
        "high_er_allowed": True,
        "build_title": "Universal Buffer / Off-field Hydro",
        "benchmarks": {
            "hp": 40000.0,
            "energy_recharge": 180.0,
        },
    },

    "kokomi": {
        "element": "hydro",
        "rarity": 5,
        "region": "inazuma",
        "main_scaling": "hp",
        "roles": ["Healer", "Support"],
        "portrait": "https://enka.network/ui/UI_AvatarIcon_Kokomi.png",
        "scaling": "hp",
        "build_title": "Healing Driver",
        "benchmarks": {
            "hp": 40000.0,
            "energy_recharge": 180.0,
        },
    },

    "mona": {
        "element": "hydro",
        "rarity": 5,
        "region": "mondstadt",
        "main_scaling": "atk",
        "roles": ["Support", "Sub DPS"],
        "portrait": "https://enka.network/ui/UI_AvatarIcon_Mona.png",
        "high_er_allowed": True,
        "build_title": "Omen Nuke Support",
        "benchmarks": {
            "energy_recharge": 200.0,
        },
    },

    "mualani": {
        "element": "hydro",
        "rarity": 5,
        "region": "natlan",
        "main_scaling": "hp",
        "roles": ["Main DPS"],
        "portrait": "https://enka.network/ui/UI_AvatarIcon_Mualani.png",
        "scaling": "hp",
        "build_title": "Hydro Hypercarry",
        "benchmarks": {
            "hp": 35000.0,
            "elemental_mastery": 100.0,
        },
    },

    "neuvillette": {
        "element": "hydro",
        "rarity": 5,
        "region": "fontaine",
        "main_scaling": "hp",
        "roles": ["Main DPS"],
        "portrait": "https://enka.network/ui/UI_AvatarIcon_Neuvillette.png",
        "scaling": "hp",
        "crit_ratio_target": 4.2,
        "build_title": "Hypercarry Charged Attacker",
        "benchmarks": {
            "hp": 35000.0,
        },
        "ignore_high_ratio_warning": True,
    },

    "nilou": {
        "element": "hydro",
        "rarity": 5,
        "region": "sumeru",
        "main_scaling": "hp",
        "roles": ["Support", "Sub DPS"],
        "portrait": "https://enka.network/ui/UI_AvatarIcon_Nilou.png",
        "scaling": "hp",
        "build_title": "Bloom Enabler",
        "benchmarks": {
            "hp": 55000.0,
        },
    },

    "sigewinne": {
        "element": "hydro",
        "rarity": 5,
        "region": "fontaine",
        "main_scaling": "hp",
        "roles": ["Healer", "Support"],
        "portrait": "https://enka.network/ui/UI_AvatarIcon_Sigewinne.png",
        "scaling": "hp",
        "build_title": "Healing Support",
        "benchmarks": {
            "hp": 45000.0,
        },
    },

    "xingqiu": {
        "element": "hydro",
        "rarity": 4,
        "region": "liyue",
        "main_scaling": "atk",
        "roles": ["Sub DPS", "Support"],
        "portrait": "https://enka.network/ui/UI_AvatarIcon_Xingqiu.png",
        "high_er_allowed": True,
        "build_title": "Off-field Hydro DPS",
        "benchmarks": {
            "energy_recharge": 220.0,
            "atk": 1600.0,
        },
    },

    "yelan": {
        "element": "hydro",
        "rarity": 5,
        "region": "liyue",
        "main_scaling": "hp",
        "roles": ["Sub DPS", "Support"],
        "portrait": "https://enka.network/ui/UI_AvatarIcon_Yelan.png",
        "scaling": "hp",
        "build_title": "Off-field Hydro DPS / Enabler",
        "benchmarks": {
            "hp": 32000.0,
            "energy_recharge": 180.0,
        },
    },

    "dahlia": {
        "element": "hydro",
        "rarity": 4,
        "region": "snezhnaya",
        "main_scaling": "hp",
        "roles": ["Support", "Shielder"],
        "portrait": "https://enka.network/ui/UI_AvatarIcon_Dahlia.png",
        "scaling": "hp",
        "high_er_allowed": True,
        "build_title": "Hydro Shield Support / ATK SPD Buffer",
        "benchmarks": {
            "hp": 40000.0,
            "energy_recharge": 200.0,
        },
    },

# ==========================================================
# ANEMO
# ==========================================================

    "chasca": {
        "element": "anemo",
        "rarity": 5,
        "region": "natlan",
        "main_scaling": "atk",
        "roles": ["Main DPS"],
        "portrait": "https://enka.network/ui/UI_AvatarIcon_Chasca.png",
        "build_title": "Aerial Hypercarry DPS",
        "benchmarks": {
            "atk": 2100.0,
        },
    },

    "faruzan": {
        "element": "anemo",
        "rarity": 4,
        "region": "sumeru",
        "main_scaling": "atk",
        "roles": ["Support", "Buffer"],
        "portrait": "https://enka.network/ui/UI_AvatarIcon_Faruzan.png",
        "high_er_allowed": True,
        "build_title": "Anemo Dedicated Support",
        "benchmarks": {
            "energy_recharge": 240.0,
        },
    },

    "heizou": {
        "element": "anemo",
        "rarity": 4,
        "region": "inazuma",
        "main_scaling": "atk",
        "roles": ["Main DPS"],
        "portrait": "https://enka.network/ui/UI_AvatarIcon_Heizo.png",
        "build_title": "Catalyst Driver / Burst DPS",
        "benchmarks": {
            "atk": 1900.0,
            "elemental_mastery": 100.0,
        },
    },

    "jean": {
        "element": "anemo",
        "rarity": 5,
        "region": "mondstadt",
        "main_scaling": "atk",
        "roles": ["Healer", "Support", "Sub DPS"],
        "portrait": "https://enka.network/ui/UI_AvatarIcon_Qin.png",
        "build_title": "Healing Support / Anemo Driver",
        "benchmarks": {
            "atk": 2000.0,
            "energy_recharge": 160.0,
        },
    },

    "kazuha": {
        "element": "anemo",
        "rarity": 5,
        "region": "inazuma",
        "main_scaling": "em",
        "roles": ["Support", "Buffer", "Sub DPS"],
        "portrait": "https://enka.network/ui/UI_AvatarIcon_Kazuha.png",
        "scaling": "em",
        "build_title": "VV Swirl Support",
        "benchmarks": {
            "elemental_mastery": 900.0,
        },
    },

    "lanyan": {
        "element": "anemo",
        "rarity": 4,
        "region": "liyue",
        "main_scaling": "atk",
        "roles": ["Support", "Shielder"],
        "portrait": "https://enka.network/ui/UI_AvatarIcon_Lanyan.png",
        "scaling": "atk",
        "build_title": "Anemo Shield Support",
        "benchmarks": {
            "atk": 1800.0,
            "energy_recharge": 180.0,
        },
    },

    "lynette": {
        "element": "anemo",
        "rarity": 4,
        "region": "fontaine",
        "main_scaling": "atk",
        "roles": ["Support", "Sub DPS"],
        "portrait": "https://enka.network/ui/UI_AvatarIcon_Linette.png",
        "build_title": "Quick-Swap Anemo Support",
        "benchmarks": {
            "atk": 1800.0,
            "energy_recharge": 180.0,
        },
    },

    "sayu": {
        "element": "anemo",
        "rarity": 4,
        "region": "inazuma",
        "main_scaling": "em",
        "roles": ["Healer", "Support", "Sub DPS"],
        "portrait": "https://enka.network/ui/UI_AvatarIcon_Sayu.png",
        "scaling": "em",
        "build_title": "Healing Swirl Support",
        "benchmarks": {
            "elemental_mastery": 700.0,
            "energy_recharge": 180.0,
        },
    },

    "sucrose": {
        "element": "anemo",
        "rarity": 4,
        "region": "mondstadt",
        "main_scaling": "em",
        "roles": ["Support", "Buffer"],
        "portrait": "https://enka.network/ui/UI_AvatarIcon_Sucrose.png",
        "scaling": "em",
        "build_title": "EM Buffing Support",
        "benchmarks": {
            "elemental_mastery": 700.0,
        },
    },

    "venti": {
        "element": "anemo",
        "rarity": 5,
        "region": "mondstadt",
        "main_scaling": "em",
        "roles": ["Support", "Sub DPS", "Crowd Control"],
        "portrait": "https://enka.network/ui/UI_AvatarIcon_Venti.png",
        "scaling": "em",
        "high_er_allowed": True,
        "build_title": "Crowd Control Support",
        "benchmarks": {
            "elemental_mastery": 800.0,
            "energy_recharge": 180.0,
        },
    },

    "wanderer": {
        "element": "anemo",
        "rarity": 5,
        "region": "sumeru",
        "main_scaling": "atk",
        "roles": ["Main DPS"],
        "portrait": "https://enka.network/ui/UI_AvatarIcon_Wanderer.png",
        "build_title": "Hypercarry Catalyst DPS",
        "benchmarks": {
            "atk": 2100.0,
        },
    },

    "xianyun": {
        "element": "anemo",
        "rarity": 5,
        "region": "liyue",
        "main_scaling": "atk",
        "roles": ["Support", "Healer", "Buffer"],
        "portrait": "https://enka.network/ui/UI_AvatarIcon_Liuyun.png",
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
        "element": "electro",
        "rarity": 4,
        "region": "liyue",
        "main_scaling": "atk",
        "roles": ["Sub DPS"],
        "portrait": "https://enka.network/ui/UI_AvatarIcon_Beidou.png",
        "high_er_allowed": True,
        "build_title": "Burst Sub DPS",
        "benchmarks": {
            "atk": 1800.0,
            "energy_recharge": 180.0,
        },
    },

    "clorinde": {
        "element": "electro",
        "rarity": 5,
        "region": "fontaine",
        "main_scaling": "atk",
        "roles": ["Main DPS"],
        "portrait": "https://enka.network/ui/UI_AvatarIcon_Clorinde.png",
        "build_title": "Aggravate / Electro DPS",
        "benchmarks": {
            "atk": 2100.0,
            "elemental_mastery": 100.0,
        },
    },

    "cyno": {
        "element": "electro",
        "rarity": 5,
        "region": "sumeru",
        "main_scaling": "atk",
        "roles": ["Main DPS"],
        "portrait": "https://enka.network/ui/UI_AvatarIcon_Cyno.png",
        "build_title": "Quickbloom Hypercarry",
        "benchmarks": {
            "atk": 1800.0,
            "elemental_mastery": 250.0,
        },
    },

    "dori": {
        "element": "electro",
        "rarity": 4,
        "region": "sumeru",
        "main_scaling": "atk",
        "roles": ["Support", "Healer", "Battery"],
        "portrait": "https://enka.network/ui/UI_AvatarIcon_Dori.png",
        "high_er_allowed": True,
        "build_title": "Battery / Healing Support",
        "benchmarks": {
            "energy_recharge": 220.0,
            "hp": 30000.0,
        },
    },

    "fischl": {
        "element": "electro",
        "rarity": 4,
        "region": "mondstadt",
        "main_scaling": "atk",
        "roles": ["Sub DPS"],
        "portrait": "https://enka.network/ui/UI_AvatarIcon_Fischl.png",
        "build_title": "Off-field Electro DPS",
        "benchmarks": {
            "atk": 2000.0,
            "elemental_mastery": 80.0,
        },
    },

    "flins": {
        "element": "electro",
        "rarity": 5,
        "region": "snezhnaya",
        "main_scaling": "atk",
        "roles": ["Main DPS"],
        "portrait": "https://enka.network/ui/UI_AvatarIcon_Flins.png",
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
        "element": "electro",
        "rarity": 5,
        "region": "liyue",
        "main_scaling": "atk",
        "roles": ["Main DPS"],
        "portrait": "https://enka.network/ui/UI_AvatarIcon_Keqing.png",
        "build_title": "Aggravate Main DPS",
        "benchmarks": {
            "atk": 2000.0,
            "elemental_mastery": 150.0,
        },
    },

    "kukishinobu": {
        "element": "electro",
        "rarity": 4,
        "region": "inazuma",
        "main_scaling": "em",
        "roles": ["Support", "Healer", "Sub DPS"],
        "portrait": "https://enka.network/ui/UI_AvatarIcon_Shinobu.png",
        "scaling": "em",
        "build_title": "Hyperbloom Trigger",
        "benchmarks": {
            "elemental_mastery": 1000.0,
        },
    },

    "lisa": {
        "element": "electro",
        "rarity": 4,
        "region": "mondstadt",
        "main_scaling": "atk",
        "roles": ["Support", "Sub DPS"],
        "portrait": "https://enka.network/ui/UI_AvatarIcon_Lisa.png",
        "build_title": "Electro Support / Aggravate",
        "benchmarks": {
            "atk": 1800.0,
            "elemental_mastery": 150.0,
        },
    },

    "ororon": {
        "element": "electro",
        "rarity": 4,
        "region": "natlan",
        "main_scaling": "atk",
        "roles": ["Sub DPS", "Support"],
        "portrait": "https://enka.network/ui/UI_AvatarIcon_Olorun.png",
        "build_title": "Electro Support",
        "benchmarks": {
            "atk": 1800.0,
            "energy_recharge": 180.0,
        },
    },

    "raiden": {
        "element": "electro",
        "rarity": 5,
        "region": "inazuma",
        "main_scaling": "atk",
        "roles": ["Main DPS", "Support", "Sub DPS", "Battery"],
        "portrait": "https://enka.network/ui/UI_AvatarIcon_Shougun.png",
        "high_er_allowed": True,
        "build_title": "Hypercarry / Burst Support",
        "benchmarks": {
            "energy_recharge": 250.0,
            "atk": 1800.0,
        },
    },

    "razor": {
        "element": "electro",
        "rarity": 4,
        "region": "mondstadt",
        "main_scaling": "atk",
        "roles": ["Main DPS"],
        "portrait": "https://enka.network/ui/UI_AvatarIcon_Razor.png",
        "build_title": "Physical / Aggravate DPS",
        "benchmarks": {
            "atk": 2100.0,
        },
    },

    "sara": {
        "element": "electro",
        "rarity": 4,
        "region": "inazuma",
        "main_scaling": "atk",
        "roles": ["Support", "Buffer"],
        "portrait": "https://enka.network/ui/UI_AvatarIcon_Sara.png",
        "high_er_allowed": True,
        "build_title": "ATK Buffer / Burst Support",
        "benchmarks": {
            "energy_recharge": 200.0,
        },
    },

    "sethos": {
        "element": "electro",
        "rarity": 4,
        "region": "sumeru",
        "main_scaling": "atk",
        "roles": ["Main DPS"],
        "portrait": "https://enka.network/ui/UI_AvatarIcon_Sethos.png",
        "build_title": "Charged Shot Electro DPS",
        "benchmarks": {
            "elemental_mastery": 300.0,
        },
    },

    "yaemiko": {
        "element": "electro",
        "rarity": 5,
        "region": "inazuma",
        "main_scaling": "atk",
        "roles": ["Sub DPS"],
        "portrait": "https://enka.network/ui/UI_AvatarIcon_Yae.png",
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
        "element": "dendro",
        "rarity": 5,
        "region": "sumeru",
        "main_scaling": "em",
        "roles": ["Main DPS"],
        "portrait": "https://enka.network/ui/UI_AvatarIcon_Alhatham.png",
        "scaling": "em",
        "build_title": "Spread Hypercarry",
        "benchmarks": {
            "elemental_mastery": 350.0,
            "atk": 1600.0,
        },
    },

    "baizhu": {
        "element": "dendro",
        "rarity": 5,
        "region": "liyue",
        "main_scaling": "hp",
        "roles": ["Healer", "Support"],
        "portrait": "https://enka.network/ui/UI_AvatarIcon_Baizhuer.png",
        "scaling": "hp",
        "high_er_allowed": True,
        "build_title": "Healing Support / Dendro Enabler",
        "benchmarks": {
            "hp": 50000.0,
            "energy_recharge": 180.0,
        },
    },

    "collei": {
        "element": "dendro",
        "rarity": 4,
        "region": "sumeru",
        "main_scaling": "atk",
        "roles": ["Support", "Sub DPS"],
        "portrait": "https://enka.network/ui/UI_AvatarIcon_Collei.png",
        "high_er_allowed": True,
        "build_title": "Off-field Dendro Support",
        "benchmarks": {
            "energy_recharge": 200.0,
        },
    },

    "emilie": {
        "element": "dendro",
        "rarity": 5,
        "region": "fontaine",
        "main_scaling": "atk",
        "roles": ["Sub DPS"],
        "portrait": "https://enka.network/ui/UI_AvatarIcon_Emilie.png",
        "build_title": "Burning Sub DPS",
        "benchmarks": {
            "atk": 2200.0,
        },
    },

    "kaveh": {
        "element": "dendro",
        "rarity": 4,
        "region": "sumeru",
        "main_scaling": "em",
        "roles": ["Main DPS", "Support"],
        "portrait": "https://enka.network/ui/UI_AvatarIcon_Kaveh.png",
        "scaling": "em",
        "build_title": "Bloom Driver",
        "benchmarks": {
            "elemental_mastery": 700.0,
            "energy_recharge": 180.0,
        },
    },

    "kinich": {
        "element": "dendro",
        "rarity": 5,
        "region": "natlan",
        "main_scaling": "atk",
        "roles": ["Main DPS"],
        "portrait": "https://enka.network/ui/UI_AvatarIcon_Kinich.png",
        "build_title": "Burning Hypercarry",
        "benchmarks": {
            "atk": 2200.0,
            "elemental_mastery": 100.0,
        },
    },

    "nahida": {
        "element": "dendro",
        "rarity": 5,
        "region": "sumeru",
        "main_scaling": "em",
        "roles": ["Support", "Sub DPS", "Buffer"],
        "portrait": "https://enka.network/ui/UI_AvatarIcon_Nahida.png",
        "scaling": "em",
        "build_title": "Reaction Driver / Off-field DPS",
        "benchmarks": {
            "elemental_mastery": 800.0,
        },
    },

    "tighnari": {
        "element": "dendro",
        "rarity": 5,
        "region": "sumeru",
        "main_scaling": "em",
        "roles": ["Main DPS"],
        "portrait": "https://enka.network/ui/UI_AvatarIcon_Tighnari.png",
        "scaling": "em",
        "build_title": "Spread Charged Shot DPS",
        "benchmarks": {
            "elemental_mastery": 350.0,
            "atk": 1700.0,
        },
    },

    "yaoyao": {
        "element": "dendro",
        "rarity": 4,
        "region": "liyue",
        "main_scaling": "hp",
        "roles": ["Healer", "Support"],
        "portrait": "https://enka.network/ui/UI_AvatarIcon_Yaoyao.png",
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
        "element": "cryo",
        "rarity": 5,
        "region": "inazuma",
        "main_scaling": "atk",
        "roles": ["Main DPS"],
        "portrait": "https://enka.network/ui/UI_AvatarIcon_Ayaka.png",
        "build_title": "Freeze Premium Main DPS",
        "benchmarks": {
            "atk": 2000.0,
            "energy_recharge": 130.0,
        },
        "freeze_build": True,
        "ignore_high_ratio_warning": True,
    },

    "charlotte": {
        "element": "cryo",
        "rarity": 4,
        "region": "fontaine",
        "main_scaling": "atk",
        "roles": ["Healer", "Support"],
        "portrait": "https://enka.network/ui/UI_AvatarIcon_Charlotte.png",
        "high_er_allowed": True,
        "build_title": "Healing Support",
        "benchmarks": {
            "atk": 1800.0,
            "energy_recharge": 200.0,
        },
    },

    "chongyun": {
        "element": "cryo",
        "rarity": 4,
        "region": "liyue",
        "main_scaling": "atk",
        "roles": ["Sub DPS", "Support"],
        "portrait": "https://enka.network/ui/UI_AvatarIcon_Chongyun.png",
        "build_title": "Cryo Infusion Support",
        "benchmarks": {
            "atk": 1800.0,
            "energy_recharge": 160.0,
        },
    },

    "citlali": {
        "element": "cryo",
        "rarity": 5,
        "region": "natlan",
        "main_scaling": "def",
        "roles": ["Support", "Shielder"],
        "portrait": "https://enka.network/ui/UI_AvatarIcon_Citlali.png",
        "scaling": "def",
        "build_title": "Cryo Reaction Support",
        "benchmarks": {
            "defense": 2200.0,
            "energy_recharge": 180.0,
        },
    },

    "diona": {
        "element": "cryo",
        "rarity": 4,
        "region": "mondstadt",
        "main_scaling": "hp",
        "roles": ["Support", "Healer", "Shielder"],
        "portrait": "https://enka.network/ui/UI_AvatarIcon_Diona.png",
        "scaling": "hp",
        "high_er_allowed": True,
        "build_title": "Shield / Healing Support",
        "benchmarks": {
            "hp": 30000.0,
            "energy_recharge": 200.0,
        },
    },

    "escoffier": {
        "element": "cryo",
        "rarity": 5,
        "region": "fontaine",
        "main_scaling": "atk",
        "roles": ["Support", "Healer", "Sub DPS"],
        "portrait": "https://enka.network/ui/UI_AvatarIcon_Escoffier.png",
        "high_er_allowed": True,
        "build_title": "Off-field Cryo Support / Healer / RES Shred",
        "benchmarks": {
            "atk": 1800.0,
            "energy_recharge": 200.0,
        },
    },

    "eula": {
        "element": "cryo",
        "rarity": 5,
        "region": "mondstadt",
        "main_scaling": "atk",
        "roles": ["Main DPS"],
        "portrait": "https://enka.network/ui/UI_AvatarIcon_Eula.png",
        "build_title": "Physical Hypercarry",
        "benchmarks": {
            "atk": 2200.0,
            "energy_recharge": 140.0,
        },
    },

    "freminet": {
        "element": "cryo",
        "rarity": 4,
        "region": "fontaine",
        "main_scaling": "atk",
        "roles": ["Main DPS"],
        "portrait": "https://enka.network/ui/UI_AvatarIcon_Freminet.png",
        "build_title": "Physical / Cryo DPS",
        "benchmarks": {
            "atk": 2000.0,
        },
    },

    "ganyu": {
        "element": "cryo",
        "rarity": 5,
        "region": "liyue",
        "main_scaling": "atk",
        "roles": ["Main DPS"],
        "portrait": "https://enka.network/ui/UI_AvatarIcon_Ganyu.png",
        "build_title": "Melt / Freeze Archer DPS",
        "benchmarks": {
            "atk": 2100.0,
        },
        "freeze_build": True,
        "ignore_high_ratio_warning": True,
    },

    "kaeya": {
        "element": "cryo",
        "rarity": 4,
        "region": "mondstadt",
        "main_scaling": "atk",
        "roles": ["Sub DPS", "Support"],
        "portrait": "https://enka.network/ui/UI_AvatarIcon_Kaeya.png",
        "build_title": "Cryo Sub DPS",
        "benchmarks": {
            "atk": 1900.0,
            "energy_recharge": 160.0,
        },
    },

    "layla": {
        "element": "cryo",
        "rarity": 4,
        "region": "sumeru",
        "main_scaling": "hp",
        "roles": ["Support", "Shielder"],
        "portrait": "https://enka.network/ui/UI_AvatarIcon_Layla.png",
        "scaling": "hp",
        "build_title": "Shield Support",
        "benchmarks": {
            "hp": 40000.0,
        },
    },

    "mika": {
        "element": "cryo",
        "rarity": 4,
        "region": "mondstadt",
        "main_scaling": "atk",
        "roles": ["Support", "Healer", "Buffer"],
        "portrait": "https://enka.network/ui/UI_AvatarIcon_Mika.png",
        "high_er_allowed": True,
        "build_title": "Physical Support",
        "benchmarks": {
            "energy_recharge": 200.0,
            "hp": 30000.0,
        },
    },

    "qiqi": {
        "element": "cryo",
        "rarity": 5,
        "region": "liyue",
        "main_scaling": "atk",
        "roles": ["Healer", "Support"],
        "portrait": "https://enka.network/ui/UI_AvatarIcon_Qiqi.png",
        "build_title": "Healing Support",
        "benchmarks": {
            "atk": 2000.0,
        },
    },

    "rosaria": {
        "element": "cryo",
        "rarity": 4,
        "region": "mondstadt",
        "main_scaling": "atk",
        "roles": ["Sub DPS", "Support"],
        "portrait": "https://enka.network/ui/UI_AvatarIcon_Rosaria.png",
        "build_title": "Cryo Burst DPS / Crit Support",
        "benchmarks": {
            "atk": 1900.0,
            "energy_recharge": 160.0,
        },
    },

    "shenhe": {
        "element": "cryo",
        "rarity": 5,
        "region": "liyue",
        "main_scaling": "atk",
        "roles": ["Support", "Buffer"],
        "portrait": "https://enka.network/ui/UI_AvatarIcon_Shenhe.png",
        "build_title": "Cryo Dedicated Buffer",
        "benchmarks": {
            "atk": 3500.0,
            "energy_recharge": 180.0,
        },
    },

    "skirk": {
        "element": "cryo",
        "rarity": 5,
        "region": "snezhnaya",
        "main_scaling": "atk",
        "roles": ["Main DPS"],
        "portrait": "https://enka.network/ui/UI_AvatarIcon_SkirkNew.png",
        "build_title": "Flexible Cryo DPS",
        "benchmarks": {
            "atk": 2200.0,
        },
    },

    "wriothesley": {
        "element": "cryo",
        "rarity": 5,
        "region": "fontaine",
        "main_scaling": "atk",
        "roles": ["Main DPS"],
        "portrait": "https://enka.network/ui/UI_AvatarIcon_Wriothesley.png",
        "build_title": "Cryo Catalyst Hypercarry",
        "benchmarks": {
            "atk": 2100.0,
        },
    },

# ==========================================================
# GEO
# ==========================================================

    "albedo": {
        "element": "geo",
        "rarity": 5,
        "region": "mondstadt",
        "main_scaling": "def",
        "roles": ["Sub DPS"],
        "portrait": "https://enka.network/ui/UI_AvatarIcon_Albedo.png",
        "scaling": "def",
        "build_title": "Off-field Geo DPS",
        "benchmarks": {
            "defense": 2000.0,
        },
    },

    "chiori": {
        "element": "geo",
        "rarity": 5,
        "region": "inazuma",
        "main_scaling": "def",
        "roles": ["Sub DPS"],
        "portrait": "https://enka.network/ui/UI_AvatarIcon_Chiori.png",
        "scaling": "def",
        "build_title": "Dual-Sword Off-field DPS",
        "benchmarks": {
            "defense": 2100.0,
        },
    },

    "gorou": {
        "element": "geo",
        "rarity": 4,
        "region": "inazuma",
        "main_scaling": "def",
        "roles": ["Support", "Buffer"],
        "portrait": "https://enka.network/ui/UI_AvatarIcon_Gorou.png",
        "scaling": "def",
        "high_er_allowed": True,
        "build_title": "Geo DEF Buffer",
        "benchmarks": {
            "defense": 1800.0,
            "energy_recharge": 220.0,
        },
    },

    "itto": {
        "element": "geo",
        "rarity": 5,
        "region": "inazuma",
        "main_scaling": "def",
        "roles": ["Main DPS"],
        "portrait": "https://enka.network/ui/UI_AvatarIcon_Itto.png",
        "scaling": "def",
        "crit_ratio_target": 2.2,
        "build_title": "Geo Hypercarry DPS",
        "benchmarks": {
            "defense": 2200.0,
        },
    },

    "kachina": {
        "element": "geo",
        "rarity": 4,
        "region": "natlan",
        "main_scaling": "def",
        "roles": ["Support"],
        "portrait": "https://enka.network/ui/UI_AvatarIcon_Kachina.png",
        "scaling": "def",
        "build_title": "Geo Support",
        "benchmarks": {
            "defense": 2000.0,
            "energy_recharge": 180.0,
        },
    },

    "navia": {
        "element": "geo",
        "rarity": 5,
        "region": "fontaine",
        "main_scaling": "atk",
        "roles": ["Main DPS"],
        "portrait": "https://enka.network/ui/UI_AvatarIcon_Navia.png",
        "build_title": "Crystalize Hypercarry",
        "benchmarks": {
            "atk": 2400.0,
        },
    },

    "ningguang": {
        "element": "geo",
        "rarity": 4,
        "region": "liyue",
        "main_scaling": "atk",
        "roles": ["Main DPS"],
        "portrait": "https://enka.network/ui/UI_AvatarIcon_Ningguang.png",
        "build_title": "Geo Catalyst DPS",
        "benchmarks": {
            "atk": 2000.0,
        },
    },

    "noelle": {
        "element": "geo",
        "rarity": 4,
        "region": "mondstadt",
        "main_scaling": "def",
        "roles": ["Main DPS", "Healer", "Shielder"],
        "portrait": "https://enka.network/ui/UI_AvatarIcon_Noel.png",
        "scaling": "def",
        "build_title": "Main DPS / Shield Support",
        "benchmarks": {
            "defense": 2000.0,
        },
    },

    "xilonen": {
        "element": "geo",
        "rarity": 5,
        "region": "natlan",
        "main_scaling": "def",
        "roles": ["Support"],
        "portrait": "https://enka.network/ui/UI_AvatarIcon_Xilonen.png",
        "scaling": "def",
        "build_title": "Geo Support / RES Shred",
        "benchmarks": {
            "defense": 2600.0,
            "energy_recharge": 180.0,
        },
    },

    "yunjin": {
        "element": "geo",
        "rarity": 4,
        "region": "liyue",
        "main_scaling": "def",
        "roles": ["Support", "Buffer"],
        "portrait": "https://enka.network/ui/UI_AvatarIcon_Yunjin.png",
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
        "element": "adaptive",
        "rarity": 5,
        "region": "outlander",
        "main_scaling": "atk",
        "roles": ["Flexible"],
        "portrait": "https://enka.network/ui/UI_AvatarIcon_PlayerBoy.png",
        "build_title": "Flexible Traveler Build",
        "benchmarks": {
            "atk": 1800.0,
        },
    },

    "anemotraveler": {
        "element": "anemo",
        "rarity": 5,
        "region": "outlander",
        "main_scaling": "em",
        "roles": ["Support", "Sub DPS"],
        "portrait": "https://enka.network/ui/UI_AvatarIcon_PlayerBoy.png",
        "scaling": "em",
        "build_title": "Swirl Traveler",
        "benchmarks": {
            "elemental_mastery": 700.0,
            "energy_recharge": 180.0,
        },
    },

    "geotraveler": {
        "element": "geo",
        "rarity": 5,
        "region": "outlander",
        "main_scaling": "atk",
        "roles": ["Sub DPS", "Support"],
        "portrait": "https://enka.network/ui/UI_AvatarIcon_PlayerBoy.png",
        "build_title": "Geo Burst DPS",
        "benchmarks": {
            "atk": 1900.0,
            "energy_recharge": 160.0,
        },
    },

    "electrotraveler": {
        "element": "electro",
        "rarity": 5,
        "region": "outlander",
        "main_scaling": "atk",
        "roles": ["Support", "Battery"],
        "portrait": "https://enka.network/ui/UI_AvatarIcon_PlayerBoy.png",
        "high_er_allowed": True,
        "build_title": "Battery Support",
        "benchmarks": {
            "energy_recharge": 240.0,
        },
    },

    "dendrotraveler": {
        "element": "dendro",
        "rarity": 5,
        "region": "outlander",
        "main_scaling": "atk",
        "roles": ["Support", "Sub DPS"],
        "portrait": "https://enka.network/ui/UI_AvatarIcon_PlayerBoy.png",
        "high_er_allowed": True,
        "build_title": "Dendro Support",
        "benchmarks": {
            "energy_recharge": 220.0,
        },
    },

    "hydrotraveler": {
        "element": "hydro",
        "rarity": 5,
        "region": "outlander",
        "main_scaling": "atk",
        "roles": ["Main DPS", "Sub DPS"],
        "portrait": "https://enka.network/ui/UI_AvatarIcon_PlayerBoy.png",
        "build_title": "Hydro On-field DPS",
        "benchmarks": {
            "atk": 1900.0,
        },
    },

    "pyrotraveler": {
        "element": "pyro",
        "rarity": 5,
        "region": "outlander",
        "main_scaling": "atk",
        "roles": ["Main DPS"],
        "portrait": "https://enka.network/ui/UI_AvatarIcon_PlayerBoy.png",
        "build_title": "Pyro DPS",
        "benchmarks": {
            "atk": 2000.0,
        },
    },

    "unknown": {
        "element": "unknown",
        "rarity": 4,
        "region": "unknown",
        "main_scaling": "atk",
        "roles": ["Unknown"],
        "portrait": None,  # not yet in Enka's public character data -- verify + fill in once available
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
# NEW CHARACTERS -- researched live (released after the Jan 2026
# knowledge cutoff), appended separately from the original 95-character
# block to avoid any risk of touching already-verified entries above.
# ==========================================================

NEW_CHARACTER_CONFIGS: Dict[str, Dict[str, Any]] = {

# ==========================================================
# ELECTRO
# ==========================================================

    "ineffa": {
        "element": "electro",
        "rarity": 5,
        "region": "snezhnaya",
        "main_scaling": "atk",
        "roles": ["Sub DPS", "Shielder"],
        "portrait": "https://enka.network/ui/UI_AvatarIcon_Ineffa.png",
        "scaling": "atk",
        "build_title": "Lunar-Charged Sub-DPS / Shielder",
        "benchmarks": {"atk": 2000.0, "elemental_mastery": 150.0},
    },

    "illuga": {
        "element": "electro",
        "rarity": 4,
        "region": "snezhnaya",
        "main_scaling": "em",
        "roles": ["Support"],
        "portrait": "https://enka.network/ui/UI_AvatarIcon_Illuga.png",  # INFERRED from naming pattern, not directly verified -- confirm this loads after deploy
        "scaling": "em",
        "high_er_allowed": True,
        "build_title": "Lunar-Crystallize EM Support",
        "benchmarks": {"elemental_mastery": 800.0, "energy_recharge": 190.0},
    },

# ==========================================================
# GEO
# ==========================================================

    "zibai": {
        "element": "geo",
        "rarity": 5,
        "region": "liyue",
        "main_scaling": "def",
        "roles": ["Main DPS"],
        "portrait": "https://enka.network/ui/UI_AvatarIcon_Zibai.png",  # INFERRED from naming pattern, not directly verified -- confirm this loads after deploy
        "scaling": "def",
        "build_title": "Lunar-Crystallize DEF-scaling DPS",
        "benchmarks": {"defense": 2000.0},
    },

# ==========================================================
# CRYO
# ==========================================================

    "columbina": {
        "element": "cryo",
        "rarity": 5,
        "region": "snezhnaya",
        "main_scaling": "hp",
        "roles": ["Sub DPS"],
        "portrait": "https://enka.network/ui/UI_AvatarIcon_Columbina.png",  # INFERRED from naming pattern, not directly verified -- confirm this loads after deploy
        "scaling": "hp",
        "build_title": "Lunar-Reaction HP Sub-DPS",
        "benchmarks": {"hp": 30000.0},
    },

    "lohen": {
        "element": "cryo",
        "rarity": 5,
        "region": "khaenriah",
        "main_scaling": "atk",
        "roles": ["Main DPS"],
        "portrait": "https://enka.network/ui/UI_AvatarIcon_Lohen.png",  # INFERRED from naming pattern, not directly verified -- confirm this loads after deploy
        "scaling": "atk",
        "build_title": "Cryo Main DPS (Hexerei)",
        "benchmarks": {"atk": 2000.0, "elemental_mastery": 150.0, "energy_recharge": 130.0},
    },

# ==========================================================
# GEO
# ==========================================================

    "linnea": {
        "element": "geo",
        "rarity": 5,
        "region": "natlan",
        "main_scaling": "def",
        "roles": ["Support", "Healer"],
        "portrait": "https://enka.network/ui/UI_AvatarIcon_Linnea.png",  # INFERRED from naming pattern, not directly verified -- confirm this loads after deploy
        "scaling": "def",
        "build_title": "Lunar-Crystallize DEF Support / Healer",
        "benchmarks": {"defense": 2000.0},
    },

# ==========================================================
# ANEMO
# ==========================================================

    "varka": {
        "element": "anemo",
        "rarity": 5,
        "region": "mondstadt",
        "main_scaling": "atk",
        "roles": ["Main DPS"],
        "portrait": "https://enka.network/ui/UI_AvatarIcon_Varka.png",  # INFERRED from naming pattern, not directly verified -- confirm this loads after deploy
        "scaling": "atk",
        "high_er_allowed": False,
        "build_title": "Hexerei Hybrid-Element Main DPS",
        "benchmarks": {"atk": 3000.0},
    },

# ==========================================================
# GEO
# ==========================================================

    "nicole": {
        "element": "geo",
        "rarity": 4,
        "region": "fontaine",
        "main_scaling": "atk",
        "roles": ["Support", "Buffer", "Shielder"],
        "portrait": "https://enka.network/ui/UI_AvatarIcon_Nicole.png",  # INFERRED from naming pattern, not directly verified -- confirm this loads after deploy
        "scaling": "atk",
        "build_title": "ATK Buffer / Shielder",
        "benchmarks": {"atk": 4000.0},
    },

# ==========================================================
# ANEMO
# ==========================================================

    "prune": {
        "element": "anemo",
        "rarity": 4,
        "region": "mondstadt",
        "main_scaling": "atk",
        "roles": ["Support", "Buffer"],
        "portrait": "https://enka.network/ui/UI_AvatarIcon_Prune.png",  # INFERRED from naming pattern, not directly verified -- confirm this loads after deploy
        "scaling": "atk",
        "high_er_allowed": True,
        "build_title": "Anemo Swirl Support / Buffer",
        "benchmarks": {"atk": 1800.0, "energy_recharge": 180.0},
    },

    "aloy": {
        "element": "cryo",
        "rarity": 5,
        "region": "outlander",
        "main_scaling": "atk",
        "roles": ["Burst DPS", "Support"],
        "portrait": "https://enka.network/ui/UI_AvatarIcon_Aloy.png",
        "scaling": "atk",
        "high_er_allowed": True,
        "build_title": "Cryo Burst DPS / Battery",
        "benchmarks": {"atk": 1800.0, "energy_recharge": 140.0},
    },

    "durin": {
        "element": "pyro",
        "rarity": 5,
        "region": "mondstadt",
        "main_scaling": "atk",
        "roles": ["Sub DPS", "Support"],
        "portrait": "https://enka.network/ui/UI_AvatarIcon_Durin.png",
        "scaling": "atk",
        "high_er_allowed": True,
        "build_title": "Off-field Pyro Sub-DPS / Support",
        "benchmarks": {"atk": 1800.0, "energy_recharge": 130.0},
    },

    "jahoda": {
        "element": "anemo",
        "rarity": 4,
        "region": "snezhnaya",
        "main_scaling": "atk",
        "roles": ["Support", "Healer"],
        "portrait": "https://enka.network/ui/UI_AvatarIcon_Jahoda.png",
        "scaling": "atk",
        "high_er_allowed": True,
        "build_title": "Swirl Support / Healer",
        "benchmarks": {"atk": 1800.0, "energy_recharge": 200.0},
    },
}

NEW_CHARACTER_ALIASES: Dict[str, str] = {
    "columbina": "columbina",
    "ineffa": "ineffa",
    "illuga": "illuga",
    "zibai": "zibai",
    "lohen": "lohen",
    "linnea": "linnea",
    "varka": "varka",
    "nicole": "nicole",
    "prune": "prune",
    "aloy": "aloy",
    "durin": "durin",
    "jahoda": "jahoda",
}


# ==========================================================
# MISSING CHARACTERS -- found via cross-referencing build_data.py
# against this file: these five were referenced in build_data.py but
# didn't exist anywhere in CHARACTER_CONFIGS or CHARACTER_ALIASES (not
# even as an alias) -- an outright gap in the original character list,
# not a typo. Xiao and Zhongli are long-established; Dahlia, Escoffier,
# and Iansan were verified live since they're newer releases.
# Appended separately, same additive pattern as NEW_CHARACTER_CONFIGS.
# ==========================================================

MISSING_CHARACTER_CONFIGS: Dict[str, Dict[str, Any]] = {

# ==========================================================
# ANEMO
# ==========================================================

    "xiao": {
        "element": "anemo",
        "rarity": 5,
        "region": "liyue",
        "main_scaling": "atk",
        "roles": ["Main DPS"],
        "portrait": "https://enka.network/ui/UI_AvatarIcon_Xiao.png",
        "scaling": "atk",
        "build_title": "Anemo Plunge Hypercarry",
        "benchmarks": {"atk": 2200.0, "energy_recharge": 130.0},
    },

# ==========================================================
# GEO
# ==========================================================

    "zhongli": {
        "element": "geo",
        "rarity": 5,
        "region": "liyue",
        "main_scaling": "hp",
        "roles": ["Support", "Shielder", "Sub DPS"],
        "portrait": "https://enka.network/ui/UI_AvatarIcon_Zhongli.png",
        "scaling": "hp",
        "high_er_allowed": True,
        "build_title": "Geo Shield Support / Off-field Utility",
        "benchmarks": {"hp": 40000.0, "energy_recharge": 200.0},
    },

# ==========================================================
# ELECTRO
# ==========================================================

    "iansan": {
        "element": "electro",
        "rarity": 4,
        "region": "natlan",
        "main_scaling": "atk",
        "roles": ["Support", "Buffer"],
        "portrait": "https://enka.network/ui/UI_AvatarIcon_Iansan.png",
        "scaling": "atk",
        "high_er_allowed": True,
        "build_title": "Off-field ATK Buffer / Support",
        "benchmarks": {"atk": 1800.0, "energy_recharge": 180.0},
    },
}

CHARACTER_CONFIGS.update(MISSING_CHARACTER_CONFIGS)

# ==========================================================
# SECOND MISSING-CHARACTER BATCH -- found via a full roster cross-check
# against Wikipedia's character list plus Enka's live character
# metadata (which additionally surfaced Aino and Lauma, both real
# released characters with full combat kits that the Wikipedia-only
# diff had missed). Every character here was individually researched
# (element/weapon type/scaling confirmed against community build
# guides), not guessed from memory -- five of these (Amber, Ayato,
# Yanfei, Yoimiya, Kirara) are long-established characters that simply
# never made it into this file's original scaffolding.
#
# Portraits: verified against real Enka data for all except Sandrone,
# who released too recently to appear in the Enka snapshot used --
# hers is pattern-inferred the same way as the other 8 gap characters
# (see the main CHARACTER_CONFIGS block), so double-check it loads.
# ==========================================================

SECOND_MISSING_CHARACTER_CONFIGS: Dict[str, Dict[str, Any]] = {
    "amber": {
        "element": "pyro",
        "rarity": 4,
        "region": "mondstadt",
        "main_scaling": "atk",
        "roles": ["Support", "Sub DPS"],
        "portrait": "https://enka.network/ui/UI_AvatarIcon_Ambor.png",
        "scaling": "atk",
        "build_title": "Pyro Support / Melt Sub DPS",
        "benchmarks": {"atk": 1800.0},
    },
    "ayato": {
        "element": "hydro",
        "rarity": 5,
        "region": "inazuma",
        "main_scaling": "atk",
        "roles": ["Main DPS"],
        "portrait": "https://enka.network/ui/UI_AvatarIcon_Ayato.png",
        "scaling": "atk",
        "build_title": "On-field Hydro DPS (Bloodblossom)",
        "benchmarks": {"atk": 2100.0},
    },
    "yanfei": {
        "element": "pyro",
        "rarity": 4,
        "region": "liyue",
        "main_scaling": "atk",
        "roles": ["Main DPS", "Sub DPS"],
        "portrait": "https://enka.network/ui/UI_AvatarIcon_Feiyan.png",
        "scaling": "atk",
        "build_title": "Charged Attack Pyro DPS / Shield Support",
        "benchmarks": {"atk": 1900.0},
    },
    "yoimiya": {
        "element": "pyro",
        "rarity": 5,
        "region": "inazuma",
        "main_scaling": "atk",
        "roles": ["Main DPS"],
        "portrait": "https://enka.network/ui/UI_AvatarIcon_Yoimiya.png",
        "scaling": "atk",
        "build_title": "On-field Pyro DPS (Normal Attack)",
        "benchmarks": {"atk": 2100.0},
    },
    "kirara": {
        "element": "dendro",
        "rarity": 4,
        "region": "inazuma",
        "main_scaling": "hp",
        "roles": ["Support", "Shielder"],
        "portrait": "https://enka.network/ui/UI_AvatarIcon_Momoka.png",
        "scaling": "hp",
        "high_er_allowed": True,
        "build_title": "HP-Scaling Support / Shielder",
        "benchmarks": {"hp": 30000.0},
    },
    "ifa": {
        "element": "anemo",
        "rarity": 4,
        "region": "natlan",
        "main_scaling": "hp",
        "roles": ["Support", "Healer"],
        "portrait": "https://enka.network/ui/UI_AvatarIcon_Ifa.png",
        "scaling": "hp",
        "high_er_allowed": True,
        "build_title": "Healing Support",
        "benchmarks": {"hp": 30000.0, "energy_recharge": 180.0},
    },
    "varesa": {
        "element": "electro",
        "rarity": 5,
        "region": "natlan",
        "main_scaling": "atk",
        "roles": ["Main DPS"],
        "portrait": "https://enka.network/ui/UI_AvatarIcon_Varesa.png",
        "scaling": "atk",
        "build_title": "On-field Electro DPS (Nightsoul)",
        "benchmarks": {"atk": 2100.0},
    },
    "mizuki": {
        "element": "anemo",
        "rarity": 5,
        "region": "inazuma",
        "main_scaling": "em",
        "roles": ["Support", "Sub DPS"],
        "portrait": "https://enka.network/ui/UI_AvatarIcon_Mizuki.png",
        "scaling": "em",
        "high_er_allowed": True,
        "build_title": "Swirl Support / EM Sub DPS",
        "benchmarks": {"elemental_mastery": 800.0, "energy_recharge": 160.0},
    },
    "sandrone": {
        "element": "cryo",
        "rarity": 5,
        "region": "snezhnaya",
        "main_scaling": "atk",
        "roles": ["Main DPS"],
        "portrait": "https://enka.network/ui/UI_AvatarIcon_Sandrone.png",  # INFERRED from naming pattern, not directly verified -- confirm this loads after deploy
        "scaling": "atk",
        "build_title": "On-field Cryo DPS (Superconduct)",
        "benchmarks": {"atk": 2200.0},
    },
    "nefer": {
        "element": "dendro",
        "rarity": 5,
        "region": "sumeru",
        "main_scaling": "em",
        "roles": ["Sub DPS", "Support"],
        "portrait": "https://enka.network/ui/UI_AvatarIcon_Nefer.png",
        "scaling": "em",
        "high_er_allowed": True,
        "build_title": "Lunar-Bloom Sub DPS",
        "benchmarks": {"elemental_mastery": 800.0, "energy_recharge": 160.0},
    },
    "aino": {
        "element": "hydro",
        "rarity": 4,
        "region": "snezhnaya",
        "main_scaling": "em",
        "roles": ["Support"],
        "portrait": "https://enka.network/ui/UI_AvatarIcon_Aino.png",
        "scaling": "em",
        "high_er_allowed": True,
        "build_title": "Off-field Hydro Application / EM Support",
        "benchmarks": {"elemental_mastery": 800.0, "energy_recharge": 160.0},
    },
    "lauma": {
        "element": "dendro",
        "rarity": 5,
        "region": "snezhnaya",
        "main_scaling": "em",
        "roles": ["Support"],
        "portrait": "https://enka.network/ui/UI_AvatarIcon_Lauma.png",
        "scaling": "em",
        "high_er_allowed": True,
        "build_title": "Lunar-Bloom Conversion Support",
        "benchmarks": {"elemental_mastery": 800.0, "energy_recharge": 140.0},
    },
}

CHARACTER_CONFIGS.update(SECOND_MISSING_CHARACTER_CONFIGS)

# A couple of common alternate names worth resolving directly.
CHARACTER_ALIASES.update({
    "kamisatoayato": "ayato",
    "yumemizukimizuki": "mizuki",
})

# Merge new characters into the main lookup tables (append-only, additive).
CHARACTER_CONFIGS.update(NEW_CHARACTER_CONFIGS)
CHARACTER_ALIASES.update(NEW_CHARACTER_ALIASES)

# Merge weapon_type / recommended_weapons data into every character's
# config, for both the original 95 and the 9 new characters above.
try:
    from weapon_data import WEAPON_DATA
    for _char_key, _weapon_info in WEAPON_DATA.items():
        if _char_key in CHARACTER_CONFIGS:
            CHARACTER_CONFIGS[_char_key].update(_weapon_info)
        else:
            # Character has weapon data but no scaling config yet -- still
            # merge it in on top of the default config so it's not lost.
            CHARACTER_CONFIGS[_char_key] = {**DEFAULT_CHARACTER_CONFIG, **_weapon_info}
except ImportError:
    # weapon_data.py missing entirely shouldn't break character lookups --
    # weapon_type/recommended_weapons will just be absent from configs.
    pass

# ==========================================================
# BUILD DATA -- curated BiS/secondary/f2p/niche weapon and artifact
# picks, plus a short team/build archetype guess per character. Lives in
# its own file (build_data.py) and is merged in here the same additive
# way as weapon_data.py above: characters not yet covered are simply
# left without these extra fields (get_character_config().get(...)
# everywhere downstream, so nothing breaks for uncovered characters).
# This is deliberately a SEPARATE file/merge step from weapon_data.py --
# it never touches weapon_data.py's existing entries, so filling in
# element after element here carries zero risk to what's already there.
# ==========================================================
try:
    from build_data import ARTIFACT_DATA, WEAPON_TIERS
    for _char_key, _artifact_info in ARTIFACT_DATA.items():
        if _char_key in CHARACTER_CONFIGS:
            CHARACTER_CONFIGS[_char_key].update(_artifact_info)
        else:
            CHARACTER_CONFIGS[_char_key] = {**DEFAULT_CHARACTER_CONFIG, **_artifact_info}
    for _char_key, _weapon_tier_info in WEAPON_TIERS.items():
        if _char_key in CHARACTER_CONFIGS:
            CHARACTER_CONFIGS[_char_key].update(_weapon_tier_info)
        else:
            CHARACTER_CONFIGS[_char_key] = {**DEFAULT_CHARACTER_CONFIG, **_weapon_tier_info}
except ImportError:
    # build_data.py missing entirely (e.g. not yet added to this repo)
    # shouldn't break character lookups -- BiS/secondary/f2p/niche and
    # team_archetype will just be absent from configs.
    pass


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
