"""
Genshin build scoring engine.

Transparent, tweakable scoring intended to estimate build quality rather
than simulate exact in-game damage. Character-specific quirks (unusual
crit ratios, non-ATK scaling, ER tolerance) are handled via the config/
alias system below rather than a single universal formula, since several
characters have kit mechanics that make the "standard" assumptions wrong
for them specifically.
"""

# Highest possible single-roll value for each substat on a 5-star artifact.
MAX_SUBSTAT_ROLL = {
    "crit_rate": 3.89,
    "crit_dmg": 7.77,
    "atk_percent": 5.83,
    "hp_percent": 5.83,
    "def_percent": 7.29,
    "elemental_mastery": 23.31,
    "energy_recharge": 6.48,
    "atk_flat": 19.45,
}

MAX_ROLLS_PER_PIECE = 9
MAX_PIECES = 5
MAX_TOTAL_ROLLS = MAX_ROLLS_PER_PIECE * MAX_PIECES

# Expected "excellent" number of rolls into one stat across all 5 artifacts.
EXPECTED_MAX_ROLLS_PER_STAT = 10

CRIT_RATIO_TARGET = 2.0

GRADE_THRESHOLDS = [
    (85, "S", "Excellent — near BiS quality"),
    (70, "A", "Great — strong, min-maxed build"),
    (55, "B", "Good — solid and usable"),
    (40, "C", "Needs improvement — noticeable gaps"),
    (0, "D", "Rough — significant reroll/upgrade needed"),
]

DEFAULT_CHARACTER_CONFIG = {
    "scaling": "atk",
    "crit_ratio_target": CRIT_RATIO_TARGET,
    "high_er_allowed": False,
}

CHARACTER_OVERRIDES = {
    # EM scalers
    "nahida": {"scaling": "em"},
    "kazuha": {"scaling": "em"},
    "sucrose": {"scaling": "em"},

    # HP scalers
    "hutao": {"scaling": "hp"},
    "yelan": {"scaling": "hp"},
    "neuvillette": {"scaling": "hp", "crit_ratio_target": 4.2},

    # DEF scalers
    "itto": {"scaling": "def", "crit_ratio_target": 2.2},
    "albedo": {"scaling": "def"},
    "chiori": {"scaling": "def"},
    "noelle": {"scaling": "def"},

    # Burst-reliant characters (high ER is expected/fine, don't flag it)
    "raiden": {"high_er_allowed": True},
    "mona": {"high_er_allowed": True},
    "faruzan": {"high_er_allowed": True},

    # Characters whose kit grants large temporary Crit buffs (set/passive),
    # making their real optimal panel-stat ratio very different from the
    # standard 1:2 assumption. Confirmed against real Akasha leaderboard
    # data (top-97th-percentile Flins build ran ~43.5% CR / 214.8% CD).
    "flins": {"crit_ratio_target": 4.9},
}

CHARACTER_ALIASES = {
    "raiden": "raiden", "raidenshogun": "raiden", "ei": "raiden",
    "hutao": "hutao",
    "wanderer": "wanderer", "scara": "wanderer", "scaramouche": "wanderer",
    "tartaglia": "childe", "childe": "childe",
    "arle": "arlecchino", "father": "arlecchino", "arlecchino": "arlecchino",
    "kazuha": "kazuha", "kaedeharakazuha": "kazuha",
    "ayaka": "ayaka", "kamisatoayaka": "ayaka",
    "ayato": "ayato", "kamisatoayato": "ayato",
    "miko": "yaemiko", "yaemiko": "yaemiko",
    "gaming": "gaming",
    "kuki": "kukishinobu", "shinobu": "kukishinobu", "kukishinobu": "kukishinobu",
    "heizou": "shikanoinheizou", "shikanoinheizou": "shikanoinheizou",
    "lyney": "lyney", "lynette": "lynette",
    "neuvi": "neuvillette", "neuv": "neuvillette", "neuvillette": "neuvillette",
    "cloudretainer": "xianyun", "xianyun": "xianyun",
    "fischl": "fischl", "jean": "jean", "noelle": "noelle",
    "itto": "itto", "aratakiitto": "itto",
    "albedo": "albedo", "chiori": "chiori", "mona": "mona",
    "nahida": "nahida", "sucrose": "sucrose", "yelan": "yelan",
    "faruzan": "faruzan", "flins": "flins",
}


def get_character_config(character):
    """
    Returns a merged configuration for the requested character.
    Unknown characters simply receive the default configuration, so this
    never fails -- it just gets less precise for characters not yet added.
    """
    normalized = (
        character.lower()
        .replace(" ", "")
        .replace("-", "")
        .replace("'", "")
    )
    normalized = CHARACTER_ALIASES.get(normalized, normalized)

    config = DEFAULT_CHARACTER_CONFIG.copy()
    config.update(CHARACTER_OVERRIDES.get(normalized, {}))
    return config


def crit_value(crit_rate, crit_dmg):
    """Standard community Crit Value formula."""
    return crit_rate * 2 + crit_dmg


def score_crit_ratio(crit_rate, crit_dmg, target_ratio=CRIT_RATIO_TARGET):
    """
    Scores how close the Crit Rate : Crit DMG ratio is to the target ratio
    for this character (defaults to the standard 1:2, but characters with
    kit-driven crit mechanics can have a very different real target -- see
    CHARACTER_OVERRIDES).
    """
    if crit_rate < 5.0:
        return 0, "Crit Rate is effectively zero — unable to evaluate a meaningful Crit Ratio."

    ratio = crit_dmg / crit_rate
    diff = abs(ratio - target_ratio)

    # Gentle decay rather than a hard crash to 0 -- an off-ratio build is
    # still a functioning build, just not optimized. Floors at 15.
    score = max(15, 100 - diff * 22)

    if target_ratio <= 2.5 and crit_rate < 50:
        note = f"Crit Rate is low ({crit_rate:.1f}%) — aim for roughly 60-75%."
    elif ratio < target_ratio - 0.3:
        note = f"Crit DMG is under-developed relative to Crit Rate (ratio {ratio:.2f}:1, target {target_ratio:.2f}:1)."
    elif ratio > target_ratio + 0.4:
        note = f"Crit Rate could be increased for better consistency (ratio {ratio:.2f}:1, target {target_ratio:.2f}:1)."
    else:
        note = f"Crit ratio is well balanced ({crit_rate:.1f}% / {crit_dmg:.1f}%, ratio {ratio:.2f}:1, target {target_ratio:.2f}:1)."

    return round(score, 1), note


def score_substat_efficiency(substat_totals):
    """
    Scores how efficiently useful substats have rolled, relative to a
    generous-but-achievable ceiling (70% of a heavily-invested stat's max
    possible value across ~10 rolls), rather than expecting perfect RNG.
    """
    if not substat_totals:
        return None, "No substat data provided."

    achievable_target_ratio = 0.70
    scores = []
    for stat, value in substat_totals.items():
        max_roll = MAX_SUBSTAT_ROLL.get(stat)
        if not max_roll or value <= 0:
            continue
        ceiling = max_roll * EXPECTED_MAX_ROLLS_PER_STAT * achievable_target_ratio
        scores.append(min(100, (value / ceiling) * 100))

    if not scores:
        return None, "Substats provided but none recognized."

    average = sum(scores) / len(scores)
    return round(average, 1), None


def grade_from_score(score):
    for threshold, letter, desc in GRADE_THRESHOLDS:
        if score >= threshold:
            return letter, desc
    return "D", GRADE_THRESHOLDS[-1][2]


def estimate_relative_damage(crit_score, substat_score, atk, hp, defense, em, scaling="atk"):
    """
    Produces a 0-100 relative estimate of build quality vs a theoretical
    BiS build. NOT a true damage calculator -- that requires per-character
    talent multipliers, enemy RES/DEF, and rotation data.
    """
    substat_component = substat_score if substat_score is not None else 0

    if scaling == "em":
        weighted = substat_component * 0.60 + crit_score * 0.20 + min(100, em / 9) * 0.20
    elif scaling == "hp":
        weighted = crit_score * 0.50 + substat_component * 0.35 + min(100, hp / 180) * 0.15
    elif scaling == "def":
        weighted = crit_score * 0.50 + substat_component * 0.35 + min(100, defense / 20) * 0.15
    else:
        weighted = crit_score * 0.50 + substat_component * 0.35 + min(100, atk / 30) * 0.15

    return round(min(100, weighted), 1)


def build_recommendations(character, crit_rate, crit_dmg, substat_totals, energy_recharge,
                           character_scaling, high_er_allowed=False, target_ratio=CRIT_RATIO_TARGET):
    recs = []

    if target_ratio <= 2.5 and crit_rate < 55:
        recs.append("Crit Rate is below the recommended range. Aim for roughly 60-75% before stacking more Crit DMG.")

    if energy_recharge and energy_recharge > 160 and not high_er_allowed:
        recs.append(f"Energy Recharge is quite high ({energy_recharge:.0f}%). You may be able to trade some ER for offensive stats.")

    if energy_recharge and energy_recharge < 100:
        recs.append(f"Energy Recharge is under 100% ({energy_recharge:.0f}%). Your Burst may not be available consistently.")

    em = substat_totals.get("elemental_mastery", 0) if substat_totals else 0
    atk_flat = substat_totals.get("atk_flat", 0) if substat_totals else 0

    if em > 100 and character_scaling != "em":
        recs.append("High Elemental Mastery detected. Make sure this character actually benefits from reaction-based damage.")

    if atk_flat > 50:
        recs.append("Flat ATK substats generally scale worse than ATK% at high investment.")

    if not recs:
        recs.append("Build looks solid overall. Future improvements will mostly come from stronger artifact rolls, better set bonuses, or weapon upgrades.")

    return recs


def rate_build(character, crit_rate, crit_dmg, atk, hp, defense, elemental_mastery,
                energy_recharge, substat_totals=None, character_scaling=None,
                ideal_crit_ratio=None):
    """
    Main build evaluation entry point.

    character_scaling and ideal_crit_ratio are optional manual overrides --
    if omitted, both are auto-derived from the character's config (falling
    back to "atk" scaling / 1:2 ratio for characters not yet in the list).
    Passing them explicitly always takes priority over the config lookup,
    useful for new/unlisted characters until they're added properly.
    """
    substat_totals = substat_totals or {}
    char_config = get_character_config(character)

    resolved_scaling = character_scaling or char_config.get("scaling", "atk")
    resolved_ratio_target = ideal_crit_ratio if ideal_crit_ratio is not None else char_config.get("crit_ratio_target", CRIT_RATIO_TARGET)
    high_er_allowed = char_config.get("high_er_allowed", False)

    crit_score, crit_note = score_crit_ratio(crit_rate, crit_dmg, target_ratio=resolved_ratio_target)
    substat_score, substat_note = score_substat_efficiency(substat_totals)

    if substat_score is not None:
        overall = round(crit_score * 0.55 + substat_score * 0.45, 1)
    else:
        # No usable substat data -- don't punish the build for data we
        # don't have. Score on crit ratio alone instead of treating
        # missing data as zero quality.
        overall = crit_score

    grade, grade_desc = grade_from_score(overall)
    est_damage = estimate_relative_damage(crit_score, substat_score, atk, hp, defense, elemental_mastery, resolved_scaling)
    recommendations = build_recommendations(
        character, crit_rate, crit_dmg, substat_totals, energy_recharge,
        resolved_scaling, high_er_allowed, target_ratio=resolved_ratio_target,
    )
    cv = round(crit_value(crit_rate, crit_dmg), 1)

    return {
        "character": character,
        "grade": grade,
        "grade_description": grade_desc,
        "overall_score": overall,
        "estimated_relative_damage": est_damage,
        "crit_value": cv,
        "crit_rate": crit_rate,
        "crit_dmg": crit_dmg,
        "crit_ratio_score": crit_score,
        "crit_ratio_note": crit_note,
        "substat_efficiency_score": substat_score if substat_score is not None else 0,
        "substat_note": substat_note,
        "recommendations": recommendations,
        "stats_used": {
            "atk": atk,
            "hp": hp,
            "def": defense,
            "elemental_mastery": elemental_mastery,
            "energy_recharge": energy_recharge,
        },
    }
    (40, "C", "Needs improvement — noticeable gaps"),
    (0, "D", "Rough — significant reroll/upgrade needed"),
]

DEFAULT_CHARACTER_CONFIG = {
    "scaling": "atk",
    "crit_ratio_target": CRIT_RATIO_TARGET,
    "high_er_allowed": False,
}

CHARACTER_OVERRIDES = {
    # EM scalers
    "nahida": {"scaling": "em"},
    "kazuha": {"scaling": "em"},
    "sucrose": {"scaling": "em"},

    # HP scalers
    "hutao": {"scaling": "hp"},
    "yelan": {"scaling": "hp"},

    # DEF scalers
    "itto": {"scaling": "def", "crit_ratio_target": 2.2},
    "albedo": {"scaling": "def"},
    "chiori": {"scaling": "def"},
    "noelle": {"scaling": "def"},

    # Burst-reliant characters (high ER is expected/fine, don't flag it)
    "raiden": {"high_er_allowed": True},
    "mona": {"high_er_allowed": True},
    "faruzan": {"high_er_allowed": True},

    # Characters whose kit grants large temporary Crit buffs (set/passive),
    # making their real optimal panel-stat ratio very different from the
    # standard 1:2 assumption. Confirmed against real Akasha leaderboard
    # data (top-97th-percentile Flins build ran ~43.5% CR / 214.8% CD).
    "flins": {"crit_ratio_target": 4.9},
}

CHARACTER_ALIASES = {
    "raiden": "raiden", "raidenshogun": "raiden", "ei": "raiden",
    "hutao": "hutao",
    "wanderer": "wanderer", "scara": "wanderer", "scaramouche": "wanderer",
    "tartaglia": "childe", "childe": "childe",
    "arle": "arlecchino", "father": "arlecchino", "arlecchino": "arlecchino",
    "kazuha": "kazuha", "kaedeharakazuha": "kazuha",
    "ayaka": "ayaka", "kamisatoayaka": "ayaka",
    "ayato": "ayato", "kamisatoayato": "ayato",
    "miko": "yaemiko", "yaemiko": "yaemiko",
    "gaming": "gaming",
    "kuki": "kukishinobu", "shinobu": "kukishinobu", "kukishinobu": "kukishinobu",
    "heizou": "shikanoinheizou", "shikanoinheizou": "shikanoinheizou",
    "lyney": "lyney", "lynette": "lynette",
    "neuvi": "neuvillette", "neuv": "neuvillette", "neuvillette": "neuvillette",
    "cloudretainer": "xianyun", "xianyun": "xianyun",
    "fischl": "fischl", "jean": "jean", "noelle": "noelle",
    "itto": "itto", "aratakiitto": "itto",
    "albedo": "albedo", "chiori": "chiori", "mona": "mona",
    "nahida": "nahida", "sucrose": "sucrose", "yelan": "yelan",
    "faruzan": "faruzan", "flins": "flins",
}


def get_character_config(character):
    """
    Returns a merged configuration for the requested character.
    Unknown characters simply receive the default configuration, so this
    never fails -- it just gets less precise for characters not yet added.
    """
    normalized = (
        character.lower()
        .replace(" ", "")
        .replace("-", "")
        .replace("'", "")
    )
    normalized = CHARACTER_ALIASES.get(normalized, normalized)

    config = DEFAULT_CHARACTER_CONFIG.copy()
    config.update(CHARACTER_OVERRIDES.get(normalized, {}))
    return config


def crit_value(crit_rate, crit_dmg):
    """Standard community Crit Value formula."""
    return crit_rate * 2 + crit_dmg


def score_crit_ratio(crit_rate, crit_dmg, target_ratio=CRIT_RATIO_TARGET):
    """
    Scores how close the Crit Rate : Crit DMG ratio is to the target ratio
    for this character (defaults to the standard 1:2, but characters with
    kit-driven crit mechanics can have a very different real target -- see
    CHARACTER_OVERRIDES).
    """
    if crit_rate < 5.0:
        return 0, "Crit Rate is effectively zero — unable to evaluate a meaningful Crit Ratio."

    ratio = crit_dmg / crit_rate
    diff = abs(ratio - target_ratio)

    # Gentle decay rather than a hard crash to 0 -- an off-ratio build is
    # still a functioning build, just not optimized. Floors at 15.
    score = max(15, 100 - diff * 22)

    if target_ratio <= 2.5 and crit_rate < 50:
        note = f"Crit Rate is low ({crit_rate:.1f}%) — aim for roughly 60-75%."
    elif ratio < target_ratio - 0.3:
        note = f"Crit DMG is under-developed relative to Crit Rate (ratio {ratio:.2f}:1, target {target_ratio:.2f}:1)."
    elif ratio > target_ratio + 0.4:
        note = f"Crit Rate could be increased for better consistency (ratio {ratio:.2f}:1, target {target_ratio:.2f}:1)."
    else:
        note = f"Crit ratio is well balanced ({crit_rate:.1f}% / {crit_dmg:.1f}%, ratio {ratio:.2f}:1, target {target_ratio:.2f}:1)."

    return round(score, 1), note


def score_substat_efficiency(substat_totals):
    """
    Scores how efficiently useful substats have rolled, relative to a
    generous-but-achievable ceiling (70% of a heavily-invested stat's max
    possible value across ~10 rolls), rather than expecting perfect RNG.
    """
    if not substat_totals:
        return None, "No substat data provided."

    achievable_target_ratio = 0.70
    scores = []
    for stat, value in substat_totals.items():
        max_roll = MAX_SUBSTAT_ROLL.get(stat)
        if not max_roll or value <= 0:
            continue
        ceiling = max_roll * EXPECTED_MAX_ROLLS_PER_STAT * achievable_target_ratio
        scores.append(min(100, (value / ceiling) * 100))

    if not scores:
        return None, "Substats provided but none recognized."

    average = sum(scores) / len(scores)
    return round(average, 1), None


def grade_from_score(score):
    for threshold, letter, desc in GRADE_THRESHOLDS:
        if score >= threshold:
            return letter, desc
    return "D", GRADE_THRESHOLDS[-1][2]


def estimate_relative_damage(crit_score, substat_score, atk, hp, defense, em, scaling="atk"):
    """
    Produces a 0-100 relative estimate of build quality vs a theoretical
    BiS build. NOT a true damage calculator -- that requires per-character
    talent multipliers, enemy RES/DEF, and rotation data.
    """
    substat_component = substat_score if substat_score is not None else 0

    if scaling == "em":
        weighted = substat_component * 0.60 + crit_score * 0.20 + min(100, em / 9) * 0.20
    elif scaling == "hp":
        weighted = crit_score * 0.50 + substat_component * 0.35 + min(100, hp / 180) * 0.15
    elif scaling == "def":
        weighted = crit_score * 0.50 + substat_component * 0.35 + min(100, defense / 20) * 0.15
    else:
        weighted = crit_score * 0.50 + substat_component * 0.35 + min(100, atk / 30) * 0.15

    return round(min(100, weighted), 1)


def build_recommendations(character, crit_rate, crit_dmg, substat_totals, energy_recharge,
                           character_scaling, high_er_allowed=False, target_ratio=CRIT_RATIO_TARGET):
    recs = []

    if target_ratio <= 2.5 and crit_rate < 55:
        recs.append("Crit Rate is below the recommended range. Aim for roughly 60-75% before stacking more Crit DMG.")

    if energy_recharge and energy_recharge > 160 and not high_er_allowed:
        recs.append(f"Energy Recharge is quite high ({energy_recharge:.0f}%). You may be able to trade some ER for offensive stats.")

    if energy_recharge and energy_recharge < 100:
        recs.append(f"Energy Recharge is under 100% ({energy_recharge:.0f}%). Your Burst may not be available consistently.")

    em = substat_totals.get("elemental_mastery", 0) if substat_totals else 0
    atk_flat = substat_totals.get("atk_flat", 0) if substat_totals else 0

    if em > 100 and character_scaling != "em":
        recs.append("High Elemental Mastery detected. Make sure this character actually benefits from reaction-based damage.")

    if atk_flat > 50:
        recs.append("Flat ATK substats generally scale worse than ATK% at high investment.")

    if not recs:
        recs.append("Build looks solid overall. Future improvements will mostly come from stronger artifact rolls, better set bonuses, or weapon upgrades.")

    return recs


def rate_build(character, crit_rate, crit_dmg, atk, hp, defense, elemental_mastery,
                energy_recharge, substat_totals=None, character_scaling=None,
                ideal_crit_ratio=None):
    """
    Main build evaluation entry point.

    character_scaling and ideal_crit_ratio are optional manual overrides --
    if omitted, both are auto-derived from the character's config (falling
    back to "atk" scaling / 1:2 ratio for characters not yet in the list).
    Passing them explicitly always takes priority over the config lookup,
    useful for new/unlisted characters until they're added properly.
    """
    substat_totals = substat_totals or {}
    char_config = get_character_config(character)

    resolved_scaling = character_scaling or char_config.get("scaling", "atk")
    resolved_ratio_target = ideal_crit_ratio if ideal_crit_ratio is not None else char_config.get("crit_ratio_target", CRIT_RATIO_TARGET)
    high_er_allowed = char_config.get("high_er_allowed", False)

    crit_score, crit_note = score_crit_ratio(crit_rate, crit_dmg, target_ratio=resolved_ratio_target)
    substat_score, substat_note = score_substat_efficiency(substat_totals)

    if substat_score is not None:
        overall = round(crit_score * 0.55 + substat_score * 0.45, 1)
    else:
        # No usable substat data -- don't punish the build for data we
        # don't have. Score on crit ratio alone instead of treating
        # missing data as zero quality.
        overall = crit_score

    grade, grade_desc = grade_from_score(overall)
    est_damage = estimate_relative_damage(crit_score, substat_score, atk, hp, defense, elemental_mastery, resolved_scaling)
    recommendations = build_recommendations(
        character, crit_rate, crit_dmg, substat_totals, energy_recharge,
        resolved_scaling, high_er_allowed, target_ratio=resolved_ratio_target,
    )
    cv = round(crit_value(crit_rate, crit_dmg), 1)

    return {
        "character": character,
        "grade": grade,
        "grade_description": grade_desc,
        "overall_score": overall,
        "estimated_relative_damage": est_damage,
        "crit_value": cv,
        "crit_rate": crit_rate,
        "crit_dmg": crit_dmg,
        "crit_ratio_score": crit_score,
        "crit_ratio_note": crit_note,
        "substat_efficiency_score": substat_score if substat_score is not None else 0,
        "substat_note": substat_note,
        "recommendations": recommendations,
        "stats_used": {
            "atk": atk,
            "hp": hp,
            "def": defense,
            "elemental_mastery": elemental_mastery,
            "energy_recharge": energy_recharge,
        },
    }
