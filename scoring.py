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

def score_weapon_fit(weapon: Optional[dict], recommended_weapons: Optional[List[str]]) -> Tuple[Optional[float], Optional[str]]:
    """
    Scores how well the equipped weapon fits the character, using the
    curated 2-weapon recommended_weapons list from weapons_data.py.

    IMPORTANT FAIRNESS NOTE: our curated list only has ~2 entries per
    character out of dozens of viable weapons in the game. An unmatched
    weapon is NOT penalized -- it receives a neutral score, since it may
    well be a perfectly good (just uncatalogued) choice. This is meant to
    reward known-optimal picks, not punish everything else.
    """
    if not weapon or not weapon.get("name"):
        return None, None

    name = str(weapon["name"]).strip().lower()
    refinement = weapon.get("refinement")
    try:
        refinement = int(refinement) if refinement else 1
    except (TypeError, ValueError):
        refinement = 1
    refinement = max(1, min(5, refinement))
    refinement_bonus = (refinement - 1) * 2  # +0 to +8 across R1-R5

    recommended = [w.lower() for w in (recommended_weapons or [])]

    if name in recommended:
        score = min(98.0, 90.0 + refinement_bonus)
        note = "This is one of CritiCal's curated top weapon picks for this character."
    else:
        score = min(80.0, 65.0 + refinement_bonus)
        note = (
            "This weapon isn't on CritiCal's short curated list for this character (which only covers "
            "~2 options out of many viable weapons), so this isn't a mark against it."
        )

    return round(score, 1), note


def score_artifact_set_fit(artifact_sets: Optional[List[dict]]) -> Tuple[Optional[float], Optional[str], Optional[bool]]:
    """
    Scores artifact set STRUCTURE only (full 4pc bonus vs 2pc+2pc vs
    fragmented) -- deliberately does NOT judge which specific set is
    "best" for a character, since the ideal set is often team-comp
    dependent rather than a single universal answer, unlike weapons.
    """
    if not artifact_sets:
        return None, None, None

    has_four_piece = any(s.get("count", 0) >= 4 for s in artifact_sets)
    two_piece_count = sum(1 for s in artifact_sets if s.get("count", 0) >= 2)

    if has_four_piece:
        score = 90.0
        note = "Running a complete 4-piece artifact set bonus."
    elif two_piece_count >= 2:
        score = 65.0
        note = "Running a 2pc+2pc hybrid setup -- a valid choice for some team comps, though usually lower personal power than a full 4-piece bonus."
    else:
        score = 40.0
        note = "Artifact pieces don't form a coherent 2pc or 4pc set bonus -- consolidating into at least a matching 2pc/2pc setup is usually a straightforward upgrade."

    return score, note, has_four_piece


def compute_overall_score(components: List[Tuple[float, float]]) -> float:
    """
    Weighted average over whichever components are actually present.
    Base weights are chosen so that when only crit+substat are present
    (weapon/artifact_sets omitted), the result is IDENTICAL to the
    original crit*0.55 + substat*0.45 formula -- adding the new optional
    components never changes existing grades when they're not supplied.
    """
    total_weight = sum(w for _, w in components)
    if total_weight <= 0:
        return 0.0
    weighted_sum = sum(s * w for s, w in components)
    return round(weighted_sum / total_weight, 1)


def classify_build_style(ratio: float, target_ratio: float, ignore_high_ratio_warning: bool) -> str:
    """
    Classifies the ACTUAL submitted build (not the character in the
    abstract) based on how its real crit ratio compares to the target.
    This is dynamic per-response, unlike the static build_title.
    """
    if ratio < target_ratio - 0.3:
        return "Crit Rate-Heavy Build"
    elif ratio > target_ratio + 0.4:
        return "Crit DMG-Stacked Build" if ignore_high_ratio_warning else "Crit DMG-Heavy Build"
    else:
        return "Balanced Crit Build"


def generate_build_description(
    character: str,
    build_style: str,
    crit_note: str,
    substat_note: Optional[str],
    ignore_high_ratio_warning: bool,
    freeze_build: bool,
    high_er_allowed: bool,
) -> str:
    """
    Produces a short natural-language summary combining the character,
    their actual stat pattern, and any character-specific context --
    meant to read like a real analysis rather than a static label.
    """
    parts = [f"{character} is running a {build_style.lower()}."]

    if ignore_high_ratio_warning and "Crit DMG" in build_style:
        parts.append("This lean into Crit DMG is expected and BiS-consistent for this character's kit, not a sign of an unbalanced build.")
    elif freeze_build:
        parts.append("As a Freeze-team build, a naturally high Crit Rate from Cryo Resonance / Blizzard Strayer may already be factored in outside of raw panel stats.")
    elif high_er_allowed:
        parts.append("Energy Recharge investment above typical thresholds is normal for this character's role.")

    if substat_note:
        parts.append(substat_note)

    return " ".join(parts)


def describe_equipment(weapon: Optional[dict], artifact_sets: Optional[List[dict]]) -> Tuple[Optional[str], Optional[str], bool]:
    """
    Returns (weapon_sentence, set_sentence, has_active_four_piece).
    has_active_four_piece is None if artifact_sets wasn't provided at all
    (distinct from False, which means it was provided and genuinely has no
    4-piece bonus active).
    """
    weapon_sentence = None
    if weapon and weapon.get("name") and weapon["name"] != "Unknown Weapon":
        refinement = weapon.get("refinement")
        ref_text = f" (Refinement {refinement})" if refinement else ""
        weapon_sentence = f"Equipped with {weapon['name']}{ref_text}."

    set_sentence = None
    has_four_piece = None
    if artifact_sets:
        has_four_piece = any(s.get("count", 0) >= 4 for s in artifact_sets)
        pieces_desc = ", ".join(f"{s['name']} ({s['count']}pc)" for s in artifact_sets if s.get("count", 0) > 0)
        if pieces_desc:
            set_sentence = f"Running {pieces_desc}."

    return weapon_sentence, set_sentence, has_four_piece


def rate_build(
    character: str, crit_rate: Any, crit_dmg: Any, atk: Any, hp: Any, defense: Any, 
    elemental_mastery: Any, energy_recharge: Any, substat_totals: Optional[dict] = None, 
    character_scaling: Optional[str] = None, ideal_crit_ratio: Optional[float] = None,
    include_relative_damage: bool = False, weapon: Optional[dict] = None,
    artifact_sets: Optional[List[dict]] = None
) -> dict:
    """Main build evaluation entry point. Casts types safely to protect runtime performance."""
    
    # Safe structure checking
    # Defensive sanitization: BDFD (and other clients) may send a "present
    # but empty" weapon/artifact_sets when an optional slash option was
    # left blank -- e.g. {"name": "", "refinement": 1} or [{"name": "",
    # "count": 0}]. Without this, an unfilled optional field could
    # accidentally count as "real data" and affect the grade, breaking the
    # fairness guarantee that omitting gear info never changes scoring.
    if weapon is not None and not (isinstance(weapon, dict) and str(weapon.get("name", "")).strip()):
        weapon = None
    if artifact_sets is not None:
        artifact_sets = [
            s for s in artifact_sets
            if isinstance(s, dict) and str(s.get("name", "")).strip() and s.get("count", 0) not in (0, "0", None, "")
        ]
        if not artifact_sets:
            artifact_sets = None

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

    recommended_weapons = char_config.get("recommended_weapons")
    weapon_score, weapon_fit_note = score_weapon_fit(weapon, recommended_weapons)
    artifact_set_score, artifact_set_note, has_four_piece = score_artifact_set_fit(artifact_sets)

    # Base weights sum to 1.0 when all four components are present. Crit
    # and substat keep EXACTLY their original 0.55/0.45 relative ratio
    # (0.4125/0.75 = 0.55, 0.3375/0.75 = 0.45) -- so grades are byte-for-
    # byte identical to before whenever weapon/artifact_sets are omitted.
    components: List[Tuple[float, float]] = [(crit_score, 0.4125)]
    scoring_components_used = ["crit_ratio"]
    if substat_score is not None:
        components.append((substat_score, 0.3375))
        scoring_components_used.append("substat_efficiency")
    if weapon_score is not None:
        components.append((weapon_score, 0.10))
        scoring_components_used.append("weapon")
    if artifact_set_score is not None:
        components.append((artifact_set_score, 0.15))
        scoring_components_used.append("artifact_sets")

    overall = compute_overall_score(components)
    grade, grade_desc, embed_color = grade_from_score(overall)

    # Dynamic build style/description, based on the ACTUAL submitted stats
    # rather than a static per-character label.
    freeze_build = char_config.get("freeze_build", False)
    actual_ratio = round(c_dmg / c_rate, 2) if c_rate > 0 else 0.0
    build_style = classify_build_style(actual_ratio, resolved_ratio_target, ignore_high_ratio)
    build_description = generate_build_description(
        character, build_style, crit_note, substat_note,
        ignore_high_ratio, freeze_build, high_er_allowed,
    )

    weapon_sentence, set_sentence, _ = describe_equipment(weapon, artifact_sets)
    if weapon_sentence:
        build_description += " " + weapon_sentence
    if weapon_fit_note:
        build_description += " " + weapon_fit_note
    if set_sentence:
        build_description += " " + set_sentence
    if artifact_set_note:
        build_description += " " + artifact_set_note

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
    if has_four_piece is False:
        recommendations.append(
            "No 4-piece artifact set bonus is currently active. Most builds benefit significantly "
            "from a full 4-piece set unless intentionally running a 2pc+2pc hybrid for a specific reason."
        )
    if weapon and weapon.get("name") and str(weapon["name"]).strip().lower() in [w.lower() for w in (recommended_weapons or [])]:
        try:
            current_refine = int(weapon.get("refinement") or 1)
        except (TypeError, ValueError):
            current_refine = 1
        if current_refine < 5:
            recommendations.append(
                f"This weapon is a strong pick -- refining it further (currently R{current_refine}) would add incremental extra value if copies are available."
            )
    cv = round((c_rate * 2.0) + c_dmg, 1)

    result = {
        "character": character,
        "build_title": build_title,
        "build_style": build_style,
        "build_description": build_description,
        "grade": grade,
        "grade_description": grade_desc,
        "embed_color": embed_color,
        "overall_score": overall,
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
        },
        # Transparency: exactly which components fed into overall_score,
        # so it's always clear whether weapon/artifact_sets affected the
        # grade for THIS response (they're optional -- never assumed).
        "scoring_components_used": scoring_components_used,
        "weapon_fit_score": weapon_score,
        "artifact_set_fit_score": artifact_set_score,
        # Full nested data, for anything that can traverse it
        "weapon": weapon,
        "artifact_sets": artifact_sets or [],
        "has_four_piece_set_bonus": has_four_piece,
        # Flattened convenience keys -- BDFD's $httpResult can't traverse
        # nested objects/arrays, mirroring the pattern used in status.py.
        "weapon_name": weapon.get("name") if weapon else None,
        "weapon_refinement": weapon.get("refinement") if weapon else None,
        "primary_artifact_set_name": artifact_sets[0]["name"] if artifact_sets else None,
        "primary_artifact_set_count": artifact_sets[0]["count"] if artifact_sets else None,
    }

    # Opt-in only -- not included by default since it duplicates overall_score
    # without adding distinct signal, and "38.5" with no units/context isn't
    # meaningful to display as-is. Pass include_relative_damage=true to get it.
    if include_relative_damage:
        result["estimated_relative_damage"] = estimate_relative_damage(
            crit_score, substat_score, c_atk, c_hp, c_def, c_em, resolved_scaling
        )

    return result
