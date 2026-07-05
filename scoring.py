"""
Genshin build scoring engine.

Everything here is intentionally transparent and tweakable — the constants
below (max substat rolls, crit value tiers, etc.) are pulled from widely
used community benchmarks (e.g. akasha.cv / genshin-optimizer conventions),
not from an exact in-game combat formula. Treat the "estimated damage %"
as a relative build-quality indicator, not a literal damage number —
doing that properly requires per-character talent multipliers, enemy
RES/DEF, and rotation data that's out of scope for this MVP.
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

# A "perfect" 5-star artifact has 4 initial substats + 5 upgrades = 9 rolls.
# Across 5 pieces, a perfectly rolled set has 45 total substat rolls.
MAX_ROLLS_PER_PIECE = 9
MAX_PIECES = 5
MAX_TOTAL_ROLLS = MAX_ROLLS_PER_PIECE * MAX_PIECES  # 45

# Weighting for how much each stat matters for typical DPS/damage-dealer
# builds. Support/EM-focused builds will naturally score differently on
# "crit value" but that's flagged separately, not penalized silently.
CRIT_RATIO_TARGET = 2.0  # ideal crit_dmg : crit_rate ratio is 2:1

GRADE_THRESHOLDS = [
    (85, "S", "Excellent — near BiS quality"),
    (70, "A", "Great — strong, min-maxed build"),
    (55, "B", "Good — solid and usable"),
    (40, "C", "Needs improvement — noticeable gaps"),
    (0, "D", "Rough — significant reroll/upgrade needed"),
]


def crit_value(crit_rate, crit_dmg):
    """Standard Crit Value formula used across the community."""
    return crit_rate * 2 + crit_dmg


def score_crit_ratio(crit_rate, crit_dmg):
    """
    Returns (score_0_100, note) evaluating how close the crit_rate:crit_dmg
    ratio is to the ideal 1:2. Being crit-rate-starved is heavily penalized
    since it causes inconsistent (swingy) damage; being crit-dmg heavy with
    low crit rate is the most common and costly mistake.
    """
    if crit_rate <= 0:
        return 0, "No Crit Rate detected — damage will be wildly inconsistent."

    ratio = crit_dmg / crit_rate
    diff = abs(ratio - CRIT_RATIO_TARGET)

    # Score decays as the ratio drifts from 2.0. Full marks within +-0.15.
    score = max(0, 100 - diff * 40)

    if crit_rate < 50:
        note = f"Crit Rate is low ({crit_rate:.1f}%) — aim for 60-75% before stacking more Crit DMG."
    elif ratio < 1.7:
        note = f"Crit DMG is under-leveled relative to Crit Rate (ratio {ratio:.2f}:1). Prioritize Crit DMG substats/main stats next."
    elif ratio > 2.4:
        note = f"Crit Rate could come up a bit relative to Crit DMG (ratio {ratio:.2f}:1) for more consistent hits."
    else:
        note = f"Crit ratio is well balanced ({crit_rate:.1f}% / {crit_dmg:.1f}%, ratio {ratio:.2f}:1)."

    return round(score, 1), note


def score_substat_efficiency(substat_totals):
    """
    substat_totals: dict of {stat_key: total_value_across_all_5_pieces}
    Compares the sum of substat value achieved against the theoretical max
    if every roll on every piece hit that same stat at max value — scaled
    down to a realistic "good roll rate" expectation instead of 100% RNG,
    since expecting every piece to roll perfectly into one stat isn't how
    artifacts work. We normalize against a generous-but-achievable target:
    70% of max total roll value, which corresponds to consistently getting
    good (not perfect) rolls.
    """
    if not substat_totals:
        return 0, "No substat data provided."

    achievable_target_ratio = 0.70
    per_stat_scores = []
    for stat, value in substat_totals.items():
        max_roll = MAX_SUBSTAT_ROLL.get(stat)
        if not max_roll or value <= 0:
            continue
        # crude assumption on rolls used: not tracked precisely in manual
        # mode, so we score relative to a "5 rolls into this stat" ceiling
        # which is a reasonable amount for a stat a build is leaning into.
        ceiling = max_roll * 5 * achievable_target_ratio
        per_stat_scores.append(min(100, (value / ceiling) * 100))

    if not per_stat_scores:
        return 0, "Substats provided but none recognized."

    avg = sum(per_stat_scores) / len(per_stat_scores)
    return round(avg, 1), None


def grade_from_score(score):
    for threshold, letter, desc in GRADE_THRESHOLDS:
        if score >= threshold:
            return letter, desc
    return "D", GRADE_THRESHOLDS[-1][2]


def estimate_relative_damage(crit_score, substat_score, atk, em, character_scaling="atk"):
    """
    Produces a 0-100 'build quality vs BiS' relative estimate.
    NOT a literal damage number. Weighted toward crit consistency since
    that's the single biggest lever for most damage dealers.
    """
    if character_scaling == "em":
        # EM-scaling supports/reactions care less about crit, more about EM.
        weighted = substat_score * 0.6 + crit_score * 0.2 + min(100, em / 3) * 0.2
    else:
        weighted = crit_score * 0.5 + substat_score * 0.35 + min(100, atk / 30) * 0.15

    return round(min(100, weighted), 1)


def build_recommendations(crit_rate, crit_dmg, substat_totals, energy_recharge):
    recs = []

    if crit_rate < 55:
        recs.append("Crit Rate is below the 60-75% target for consistent damage — reroll/swap pieces with Crit Rate substats first.")
    if energy_recharge and energy_recharge > 160:
        recs.append(f"Energy Recharge is quite high ({energy_recharge:.0f}%) — you may be able to shift some ER substats into Crit or ATK% for more damage.")
    if energy_recharge and energy_recharge < 100:
        recs.append(f"Energy Recharge is under 100% ({energy_recharge:.0f}%) — check if your rotation is burst-reliant; you may be losing uptime.")

    em = substat_totals.get("elemental_mastery", 0) if substat_totals else 0
    atk_flat = substat_totals.get("atk_flat", 0) if substat_totals else 0
    if em > 100:
        recs.append("Significant Elemental Mastery investment detected — make sure this character's kit actually benefits from EM (reaction-focused), otherwise this is wasted substat value.")
    if atk_flat > 50:
        recs.append("Flat ATK substats present — these scale worse than ATK% for most characters at high investment; consider ATK% instead if available.")

    if not recs:
        recs.append("Build looks solid overall — minor refinements only, focus on artifact set bonus and weapon choice for further gains.")

    return recs


def rate_build(character, crit_rate, crit_dmg, atk, hp, defense, elemental_mastery,
                energy_recharge, substat_totals=None, character_scaling="atk"):
    substat_totals = substat_totals or {}

    crit_score, crit_note = score_crit_ratio(crit_rate, crit_dmg)
    substat_score, substat_note = score_substat_efficiency(substat_totals)
    overall = round(crit_score * 0.55 + substat_score * 0.45, 1)
    grade, grade_desc = grade_from_score(overall)
    est_damage = estimate_relative_damage(crit_score, substat_score, atk, elemental_mastery, character_scaling)
    recommendations = build_recommendations(crit_rate, crit_dmg, substat_totals, energy_recharge)
    cv = round(crit_value(crit_rate, crit_dmg), 1)

    return {
        "character": character,
        "grade": grade,
        "grade_description": grade_desc,
        "overall_score": overall,
        "crit_value": cv,
        "crit_rate": crit_rate,
        "crit_dmg": crit_dmg,
        "crit_ratio_score": crit_score,
        "crit_ratio_note": crit_note,
        "substat_efficiency_score": substat_score,
        "estimated_relative_damage": est_damage,
        "recommendations": recommendations,
        "stats_used": {
            "atk": atk,
            "hp": hp,
            "def": defense,
            "elemental_mastery": elemental_mastery,
            "energy_recharge": energy_recharge,
        },
}
