"""
Genshin build scoring engine.

Transparent, tweakable scoring intended to estimate build quality rather
than simulate exact in-game damage. Optimized for standard library dependencies.
"""
from typing import Dict, Any, List, Tuple, Optional
from characters import CRIT_RATIO_TARGET, get_character_config

# Highest possible single-roll value for each substat on a 5-star artifact.
MAX_SUBSTAT_ROLL: Dict[str, float] = {
    "crit_rate": 3.89,
    "crit_dmg": 7.77,
    "atk_percent": 5.83,
    "hp_percent": 5.83,
    "def_percent": 7.29,
    "elemental_mastery": 23.31,
    "energy_recharge": 6.48,
    "atk_flat": 19.45,
}

EXPECTED_MAX_ROLLS_PER_STAT: int = 10

# Dynamic Grade Thresholds paired with exact target Hex Colors
GRADE_THRESHOLDS: List[Tuple[float, str, str, str]] = [
    (85.0, "S", "Excellent — near BiS quality", "#00FF66"),       
    (70.0, "A", "Great — strong, min-maxed build", "#3498DB"),    
    (55.0, "B", "Good — solid and usable", "#9B59B6"),            
    (40.0, "C", "Needs improvement — noticeable gaps", "#F1C40F"), 
    (0.0, "D", "Rough — significant upgrade needed", "#E74C3C"),   
]

def crit_value(crit_rate: float, crit_dmg: float) -> float:
    """Standard community Crit Value formula."""
    return (float(crit_rate) * 2.0) + float(crit_dmg)

def score_crit_ratio(
    crit_rate: float, 
    crit_dmg: float, 
    target_ratio: float = CRIT_RATIO_TARGET,
    ignore_high_ratio_warning: bool = False
) -> Tuple[float, str]:
    """Scores how close the Crit Rate : Crit DMG ratio is to the target ratio."""
    c_rate = round(float(crit_rate), 2)
    c_dmg = round(float(crit_dmg), 2)
    
    if c_rate < 5.0:
        return 0.0, "Crit Rate is effectively zero — unable to evaluate a meaningful Crit Ratio."

    ratio = round(c_dmg / c_rate, 2)
    diff = abs(ratio - target_ratio)
    score = max(15.0, 100.0 - (diff * 22.0))

    if target_ratio <= 2.5 and c_rate < 50.0:
        note = f"Crit Rate is low ({c_rate:.1f}%) — aim for roughly 60–75%."
    elif ratio < target_ratio - 0.3:
        note = f"Crit DMG is under-developed relative to Crit Rate (ratio {ratio:.2f}:1, target {target_ratio:.2f}:1)."
    elif ratio > target_ratio + 0.4 and not ignore_high_ratio_warning:
        note = f"Crit Rate could be increased for better consistency (ratio {ratio:.2f}:1, target {target_ratio:.2f}:1)."
    else:
        note = f"Crit ratio is well balanced ({c_rate:.1f}% / {c_dmg:.1f}%, ratio {ratio:.2f}:1, target {target_ratio:.2f}:1)."

    return round(score, 1), note

def score_substat_efficiency(substat_totals: dict, primary_scaling: str) -> Tuple[Optional[float], Optional[str], float]:
    """Scores substat efficiency and tracks primary scaling stat roll counts."""
    if not substat_totals:
        return None, "No substat data provided.", 0.0

    achievable_target_ratio = 0.70
    scores: List[float] = []
    primary_stat_rolls = 0.0

    scaling_map = {"atk": "atk_percent", "hp": "hp_percent", "def": "def_percent", "em": "elemental_mastery"}
    target_substat_key = scaling_map.get(primary_scaling, "atk_percent")

    for stat, val in substat_totals.items():
        try:
            value = float(val)
        except (ValueError, TypeError):
            continue

        max_roll = MAX_SUBSTAT_ROLL.get(stat)
        if not max_roll or value <= 0:
            continue

        if stat == target_substat_key:
            primary_stat_rolls = value / max_roll

        ceiling = max_roll * EXPECTED_MAX_ROLLS_PER_STAT * achievable_target_ratio
        scores.append(min(100.0, (value / ceiling) * 100.0))

    if not scores:
        return None, "Substats provided but none recognized.", 0.0

    average = sum(scores) / len(scores)
    return round(average, 1), None, round(primary_stat_rolls, 1)

def grade_from_score(score: float) -> Tuple[str, str, str]:
    """Returns (Grade Letter, Description, Hex Color) based on final score."""
    for threshold, letter, desc, color in GRADE_THRESHOLDS:
        if score >= threshold:
            return letter, desc, color
    return "D", GRADE_THRESHOLDS[-1][2], GRADE_THRESHOLDS[-1][3]

def estimate_relative_damage(crit_score: float, substat_score: Optional[float], atk: float, hp: float, defense: float, em: float, scaling: str = "atk") -> float:
    """Produces a relative (0-100) build quality index score."""
    substat_component = float(substat_score) if substat_score is not None else 0.0
    c_score = float(crit_score)

    if scaling == "em":
        weighted = (substat_component * 0.60) + (c_score * 0.20) + (min(100.0, float(em) / 9.0) * 0.20)
    elif scaling == "hp":
        weighted = (c_score * 0.50) + (substat_component * 0.35) + (min(100.0, float(hp) / 180.0) * 0.15)
    elif scaling == "def":
        weighted = (c_score * 0.50) + (substat_component * 0.35) + (min(100.0, float(defense) / 20.0) * 0.15)
    else:
        weighted = (c_score * 0.50) + (substat_component * 0.35) + (min(100.0, float(atk) / 30.0) * 0.15)

    return round(min(100.0, weighted), 1)

def build_recommendations(
    character: str, 
    crit_rate: float, 
    crit_dmg: float, 
    substat_totals: dict, 
    energy_recharge: float, 
    character_scaling: str, 
    high_er_allowed: bool = False, 
    target_ratio: float = CRIT_RATIO_TARGET,
    char_config: Optional[dict] = None
) -> List[str]:
    """Generates analytical optimization tips tailored to character profiles."""
    recs = []
    c_rate = float(crit_rate)
    er = float(energy_recharge)
    config = char_config or {}

    if target_ratio <= 2.5 and c_rate < 55.0 and not config.get("freeze_build", False):
        recs.append("Crit Rate is below the recommended range. Aim for roughly 60–75% before stacking more Crit DMG.")

    if config.get("freeze_build", False) and c_rate > 45.0:
        recs.append("Crit Rate might be over-capped if you are running 4-Piece Blizzard Strayer with Cryo Resonance.")

    if er > 160.0 and not high_er_allowed:
        recs.append(f"Energy Recharge is quite high ({er:.0f}%). You may be able to trade some ER for offensive stats.")

    if er > 0 and er < 100.0:
        recs.append(f"Energy Recharge is under 100% ({er:.0f}%). Your Burst may not be available consistently.")

    em = float(substat_totals.get("elemental_mastery", 0.0))
    atk_flat = float(substat_totals.get("atk_flat", 0.0))

    if em > 100.0 and character_scaling != "em":
        recs.append("High Elemental Mastery detected. Make sure this character actually benefits from reaction-based damage.")

    if atk_flat > 50.0:
        recs.append("Flat ATK substats generally scale worse than ATK% at high investment.")

    if not recs:
        recs.append("Build looks solid overall. Future improvements will mostly come from stronger artifact rolls, better set bonuses, or weapon upgrades.")

    return recs

def rate_build(
    character: str, crit_rate: Any, crit_dmg: Any, atk: Any, hp: Any, defense: Any, 
    elemental_mastery: Any, energy_recharge: Any, substat_totals: Optional[dict] = None, 
    character_scaling: Optional[str] = None, ideal_crit_ratio: Optional[float] = None
) -> dict:
    """Main build evaluation entry point. Casts types safely to protect runtime performance."""
    
    # Safe structure checking
    clean_substats = {}
    if isinstance(substat_totals, dict):
        for k, v in substat_totals.items():
            try:
                # Filter out garbage input keys like "atkk" or "energy"
                stat_key = str(k).lower().strip()
                if stat_key in MAX_SUBSTAT_ROLL:
                    clean_substats[stat_key] = float(v)
            except (ValueError, TypeError):
                continue

    try:
        c_rate = float(crit_rate)
        c_dmg = float(crit_dmg)
        c_atk = float(atk)
        c_hp = float(hp)
        c_def = float(defense)
        c_em = float(elemental_mastery)
        c_er = float(energy_recharge)
    except (ValueError, TypeError):
        return {"error": "Invalid numerical parameters supplied to rating engine."}

    char_config = get_character_config(character)
    resolved_scaling = character_scaling or char_config.get("scaling", "atk")
    resolved_ratio_target = ideal_crit_ratio if ideal_crit_ratio is not None else char_config.get("crit_ratio_target", CRIT_RATIO_TARGET)
    high_er_allowed = char_config.get("high_er_allowed", False)
    build_title = char_config.get("build_title", "Standard Build Archetype")
    ignore_high_ratio = char_config.get("ignore_high_ratio_warning", False)

    crit_score, crit_note = score_crit_ratio(c_rate, c_dmg, target_ratio=resolved_ratio_target, ignore_high_ratio_warning=ignore_high_ratio)
    substat_score, substat_note, equivalent_rolls = score_substat_efficiency(clean_substats, resolved_scaling)

    overall = round((crit_score * 0.55 + substat_score * 0.45), 1) if substat_score is not None else crit_score
    grade, grade_desc, embed_color = grade_from_score(overall)
    est_damage = estimate_relative_damage(crit_score, substat_score, c_atk, c_hp, c_def, c_em, resolved_scaling)

    # Benchmarking Processor
    benchmark_status: List[str] = []
    stat_lookup = {"atk": c_atk, "hp": c_hp, "defense": c_def, "elemental_mastery": c_em, "energy_recharge": c_er}
    label_lookup = {"atk": "ATK", "hp": "HP", "defense": "DEF", "elemental_mastery": "EM", "energy_recharge": "ER"}
    
    benchmarks: Dict[str, float] = char_config.get("benchmarks", {})
    for target_stat, target_value in benchmarks.items():
        actual_value = stat_lookup.get(target_stat, 0.0)
        label = label_lookup.get(target_stat, target_stat.upper())
        if target_value <= 0:
            continue
        if actual_value >= target_value:
            benchmark_status.append(f"{label}: {actual_value:.0f} / {target_value:.0f} Target Met! 🎉")
        else:
            pct = (actual_value / target_value) * 100.0
            benchmark_status.append(f"{label}: {actual_value:.0f} / {target_value:.0f} ({pct:.1f}% of target)")

    efficiency_tier_note = f"Your substats have accumulated the equivalent of {equivalent_rolls:.1f} perfect high-rolls into your primary scaling stat." if equivalent_rolls > 0 else "No substantial primary rolls mapped."

    recommendations = build_recommendations(character, c_rate, c_dmg, clean_substats, c_er, resolved_scaling, high_er_allowed, target_ratio=resolved_ratio_target, char_config=char_config)
    cv = round((c_rate * 2.0) + c_dmg, 1)

    return {
        "character": character,
        "build_title": build_title,
        "grade": grade,
        "grade_description": grade_desc,
        "embed_color": embed_color,
        "overall_score": overall,
        "estimated_relative_damage": est_damage,
        "crit_value": cv,
        "crit_rate": c_rate,
        "crit_dmg": c_dmg,
        "crit_ratio_score": crit_score,
        "crit_ratio_note": crit_note,
        "substat_efficiency_score": substat_score if substat_score is not None else 0.0,
        "substat_note": substat_note,
        "efficiency_tier_note": efficiency_tier_note,
        "benchmark_status": benchmark_status,
        "recommendations": recommendations,
        "stats_used": {
            "atk": c_atk, "hp": c_hp, "def": c_def,
            "elemental_mastery": c_em, "energy_recharge": c_er
        }
  }
  
