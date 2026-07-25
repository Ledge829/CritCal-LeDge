"""
Comprehensive weapon database for CritCal's smart scoring engine.

Every weapon in the game with full metadata: base stats, substat,
ability effects, synergy tags, and acquisition source. This powers
CritCal's "brain" — when a weapon isn't in the curated build_data.py
list, the engine uses this data to evaluate how well it actually
fits a character instead of just calling it "Unlisted".
"""

WEAPONS_DB = {
    # ALL WEAPONS
    "a teaspoon of transcendence": {
    "type": "claymore", "rarity": 5, "base_atk": 542, "substat": "atk_percent", "substat_val": 41.3,
    "ability": "When a party member triggers a reaction, deal 100% of ATK as True DMG.",
    "tags": ["atk_scaling", "reaction", "dps"],
    },
    "a thousand blazing suns": {
    "type": "claymore", "rarity": 5, "base_atk": 608, "substat": "atk_percent", "substat_val": 41.3,
    "ability": "",
    "tags": [],
    },
    "a thousand floating dreams": {
    "type": "catalyst", "rarity": 5, "base_atk": 542, "substat": "elemental_mastery", "substat_val": 265.4,
    "ability": "Party EM increased. User gains 10% Elemental DMG Bonus per different-element member.",
    "tags": ["em", "support", "team_buffer", "nahida"],
    },
    "absolution": {
    "type": "Sword", "rarity": 5, "base_atk": 674, "substat": "crit_dmg", "substat_val": 88.1,
    "ability": "CRIT DMG increased by 20%. When a character uses their Elemental Skill, they gain a Sigil of Resolution that increases their Normal and Charged Attack DMG by 20% for 8s.",
    "tags": ["crit_dmg", "skill_dmg", "burst_dmg"],
    },
    "akuoumaru": {
    "type": "claymore", "rarity": 4, "base_atk": 510, "substat": "atk_percent", "substat_val": 41.3,
    "ability": "",
    "tags": [],
    },
    "alley hunter": {
    "type": "bow", "rarity": 4, "base_atk": 454, "substat": "atk_percent", "substat_val": 41.3,
    "ability": "Increases DMG dealt by 12% when the character is on-field. Effect removed after 4s off-field.",
    "tags": ["atk_scaling", "dps"],
    },
    "amenoma kageuchi": {
    "type": "Sword", "rarity": 4, "base_atk": 565, "substat": "atk_percent", "substat_val": 51.7,
    "ability": "After using an Elemental Skill, gain 1 Succession Seed every 5s. Max 3 seeds. Using an Elemental Burst consumes all seeds and restores 12 Energy per seed.",
    "tags": ["er", "burst_focus", "f2p", "craftable"],
    },
    "amos' bow": {
    "type": "bow", "rarity": 5, "base_atk": 542, "substat": "atk_percent", "substat_val": 49.6,
    "ability": "Increases Normal and Charged Attack DMG by 12%. After firing, further increases by 8% every 0.1s, up to 5 stacks.",
    "tags": ["atk_scaling", "charged_atk", "ganyu"],
    },
    "apprentice's notes": {
    "type": "catalyst", "rarity": 4, "base_atk": 510, "substat": "atk_percent", "substat_val": 41.3,
    "ability": "",
    "tags": [],
    },
    "aqua simulacra": {
    "type": "bow", "rarity": 5, "base_atk": 542, "substat": "crit_dmg", "substat_val": 88.1,
    "ability": "HP increased by 16%. When opponents are nearby, deal 20% more DMG regardless of whether the character is on-field.",
    "tags": ["crit_dmg", "hp_scaling", "universal"],
    },
    "aquila favonia": {
    "type": "Sword", "rarity": 5, "base_atk": 674, "substat": "atk_percent", "substat_val": 51.7,
    "ability": "ATK increased by 20%. Taking DMG triggers a soul of the West Wind that deals 400% ATK DMG and regenerates 40% of ATK as HP for 15s. Can occur once every 15s.",
    "tags": ["atk_scaling", "physical", "healing"],
    },
    "astral vulture's crimson plumage": {
    "type": "bow", "rarity": 5, "base_atk": 542, "substat": "crit_rate", "substat_val": 33.1,
    "ability": "Skill DMG increased by 24%. When party members trigger reactions, gain 24% ATK for 12s.",
    "tags": ["crit_rate", "skill_dmg", "team_buffer", "natlan"],
    },
    "athame artis": {
    "type": "sword", "rarity": 5, "base_atk": 542, "substat": "crit_dmg", "substat_val": 88.1,
    "ability": "When the wielder triggers a reaction, all party members gain 12% ATK and 6% Elemental DMG Bonus for 12s.",
    "tags": ["crit_dmg", "team_buffer", "reaction"],
    },
    "azurelight": {
    "type": "sword", "rarity": 5, "base_atk": 542, "substat": "crit_rate", "substat_val": 44.1,
    "ability": "ATK increased by 15%. When the wielder's HP changes, deals 24% more DMG for 8s.",
    "tags": ["crit_rate", "atk_scaling", "hp_scaling"],
    },
    "ballad of the boundless blue": {
    "type": "catalyst", "rarity": 4, "base_atk": 454, "substat": "energy_recharge", "substat_val": 45.9,
    "ability": "Normal Attack hits increase ATK by 8% for 8s, max 4 stacks.",
    "tags": ["er", "atk_scaling", "f2p", "event"],
    },
    "ballad of the fjords": {
    "type": "polearm", "rarity": 4, "base_atk": 510, "substat": "atk_percent", "substat_val": 41.3,
    "ability": "",
    "tags": [],
    },
    "beacon of the reed sea": {
    "type": "claymore", "rarity": 5, "base_atk": 608, "substat": "atk_percent", "substat_val": 41.3,
    "ability": "",
    "tags": [],
    },
    "black tassel": {
    "type": "polearm", "rarity": 4, "base_atk": 510, "substat": "atk_percent", "substat_val": 41.3,
    "ability": "",
    "tags": [],
    },
    "blackcliff agate": {
    "type": "catalyst", "rarity": 4, "base_atk": 454, "substat": "crit_dmg", "substat_val": 55.1,
    "ability": "After defeating an opponent, ATK increased by 12% for 30s. Max 3 stacks.",
    "tags": ["crit_dmg", "atk_scaling", "starglitter"],
    },
    "blackcliff longsword": {
    "type": "Sword", "rarity": 4, "base_atk": 565, "substat": "crit_dmg", "substat_val": 51.7,
    "ability": "After defeating an opponent, ATK is increased by 12% for 30s. Max 3 stacks, each stack's duration is independent.",
    "tags": ["crit_dmg", "atk_scaling", "starglitter"],
    },
    "blackcliff pole": {
    "type": "polearm", "rarity": 4, "base_atk": 510, "substat": "atk_percent", "substat_val": 41.3,
    "ability": "",
    "tags": [],
    },
    "blackcliff slasher": {
    "type": "claymore", "rarity": 4, "base_atk": 510, "substat": "atk_percent", "substat_val": 41.3,
    "ability": "",
    "tags": [],
    },
    "blackcliff warbow": {
    "type": "bow", "rarity": 4, "base_atk": 454, "substat": "crit_dmg", "substat_val": 55.1,
    "ability": "After defeating an opponent, ATK increased by 12% for 30s. Max 3 stacks.",
    "tags": ["crit_dmg", "atk_scaling", "starglitter"],
    },
    "blackmarrow lantern": {
    "type": "catalyst", "rarity": 4, "base_atk": 454, "substat": "elemental_mastery", "substat_val": 165.3,
    "ability": "When the wielder triggers a Bloom-related reaction, all party members gain 40 EM for 10s.",
    "tags": ["em", "bloom", "support", "team_buffer"],
    },
    "bloodsoaked ruins": {
    "type": "polearm", "rarity": 5, "base_atk": 542, "substat": "atk_percent", "substat_val": 31.2,
    "ability": "No special effect.",
    "tags": ["f2p", "early_game"],
    },
    "bloodtainted greatsword": {
    "type": "claymore", "rarity": 4, "base_atk": 454, "substat": "elemental_mastery", "substat_val": 99.1,
    "ability": "Increases DMG against enemies affected by Pyro or Electro by 12%.",
    "tags": ["em", "reaction", "f2p"],
    },
    "calamity queller": {
    "type": "polearm", "rarity": 5, "base_atk": 608, "substat": "atk_percent", "substat_val": 41.3,
    "ability": "",
    "tags": [],
    },
    "cashflow supervision": {
    "type": "catalyst", "rarity": 5, "base_atk": 542, "substat": "crit_rate", "substat_val": 33.1,
    "ability": "ATK increased by 16%. When HP changes, Normal Attack DMG increases by 16% and Charged Attack DMG by 14% for 4s.",
    "tags": ["crit_rate", "atk_scaling", "fontaine"],
    },
    "chain breaker": {
    "type": "bow", "rarity": 4, "base_atk": 454, "substat": "atk_percent", "substat_val": 41.3,
    "ability": "For each party member with different element, gain 4.8% ATK. Max 3 stacks.",
    "tags": ["atk_scaling", "natlan", "f2p"],
    },
    "cinnabar spindle": {
    "type": "Sword", "rarity": 4, "base_atk": 565, "substat": "def_percent", "substat_val": 51.7,
    "ability": "Elemental Skill DMG is increased by 40% of DEF. Can occur once every 1.5s.",
    "tags": ["def_scaling", "skill_dmg", "event"],
    },
    "compound bow": {
    "type": "bow", "rarity": 4, "base_atk": 510, "substat": "atk_percent", "substat_val": 41.3,
    "ability": "",
    "tags": [],
    },
    "cool steel": {
    "type": "sword", "rarity": 4, "base_atk": 454, "substat": "atk_percent", "substat_val": 31.2,
    "ability": "Increases DMG against enemies affected by Hydro or Cryo by 12%.",
    "tags": ["atk_scaling", "cryo", "hydro", "f2p"],
    },
    "crane's echoing call": {
    "type": "catalyst", "rarity": 5, "base_atk": 608, "substat": "atk_percent", "substat_val": 41.3,
    "ability": "",
    "tags": [],
    },
    "crescent pike": {
    "type": "polearm", "rarity": 4, "base_atk": 454, "substat": "physical_dmg", "substat_val": 51.7,
    "ability": "After picking up an Elemental Particle, Normal and Charged Attacks deal 20% ATK as extra DMG.",
    "tags": ["physical", "dps", "craftable", "f2p"],
    },
    "crimson moon's semblance": {
    "type": "polearm", "rarity": 5, "base_atk": 608, "substat": "atk_percent", "substat_val": 41.3,
    "ability": "",
    "tags": [],
    },
    "dark iron sword": {
    "type": "Sword", "rarity": 3, "base_atk": 401, "substat": "elemental_mastery", "substat_val": 115.3,
    "ability": "Upon causing an Overloaded, Superconduct, Electro-Charged, Quicken, Aggravate, Hyperbloom, or Electro Swirl reaction, ATK is increased by 20% for 12s.",
    "tags": ["em", "reaction", "f2p"],
    },
    "dawning frost": {
    "type": "catalyst", "rarity": 4, "base_atk": 510, "substat": "atk_percent", "substat_val": 41.3,
    "ability": "",
    "tags": [],
    },
    "deathmatch": {
    "type": "polearm", "rarity": 4, "base_atk": 510, "substat": "atk_percent", "substat_val": 41.3,
    "ability": "",
    "tags": [],
    },
    "debate club": {
    "type": "claymore", "rarity": 4, "base_atk": 454, "substat": "atk_percent", "substat_val": 31.2,
    "ability": "After using skill, on hit deals 60% ATK as AoE DMG.",
    "tags": ["atk_scaling", "f2p"],
    },
    "dialogues of the desert sages": {
    "type": "polearm", "rarity": 4, "base_atk": 510, "substat": "atk_percent", "substat_val": 41.3,
    "ability": "",
    "tags": [],
    },
    "dragon's bane": {
    "type": "polearm", "rarity": 4, "base_atk": 510, "substat": "atk_percent", "substat_val": 41.3,
    "ability": "",
    "tags": [],
    },
    "dragonspine spear": {
    "type": "polearm", "rarity": 4, "base_atk": 454, "substat": "physical_dmg", "substat_val": 51.7,
    "ability": "Hitting an enemy has a 60% chance to form an icicle dealing 80% ATK AoE DMG. If enemy is Cryo, DMG is 200%.",
    "tags": ["physical", "cryo", "craftable"],
    },
    "earth shaker": {
    "type": "claymore", "rarity": 4, "base_atk": 510, "substat": "atk_percent", "substat_val": 41.3,
    "ability": "",
    "tags": [],
    },
    "ebony bow": {
    "type": "bow", "rarity": 4, "base_atk": 510, "substat": "atk_percent", "substat_val": 41.3,
    "ability": "",
    "tags": [],
    },
    "elegy for the end": {
    "type": "bow", "rarity": 5, "base_atk": 542, "substat": "energy_recharge", "substat_val": 55.1,
    "ability": "EM increased by 60. When skill or burst hits, gain Sigils (max 4). Consuming them gives party 100 EM and 20% ATK for 12s.",
    "tags": ["er", "em", "support", "team_buffer"],
    },
    "emerald orb": {
    "type": "catalyst", "rarity": 4, "base_atk": 454, "substat": "elemental_mastery", "substat_val": 99.1,
    "ability": "After causing a Hydro reaction, ATK increased by 20% for 12s.",
    "tags": ["em", "reaction", "f2p"],
    },
    "end of the line": {
    "type": "bow", "rarity": 4, "base_atk": 454, "substat": "energy_recharge", "substat_val": 45.9,
    "ability": "Using a skill triggers a karma effect that deals 80% ATK as AoE DMG. Dealing DMG with karma regenerates 2 Energy.",
    "tags": ["er", "skill_dmg", "f2p"],
    },
    "engulfing lightning": {
    "type": "polearm", "rarity": 5, "base_atk": 608, "substat": "atk_percent", "substat_val": 41.3,
    "ability": "",
    "tags": [],
    },
    "etherlight spindlelute": {
    "type": "catalyst", "rarity": 4, "base_atk": 510, "substat": "atk_percent", "substat_val": 41.3,
    "ability": "",
    "tags": [],
    },
    "everlasting moonglow": {
    "type": "catalyst", "rarity": 5, "base_atk": 542, "substat": "hp_percent", "substat_val": 49.6,
    "ability": "Healing Bonus increased by 10%. Normal Attack DMG increased by 1% of Max HP.",
    "tags": ["hp_scaling", "healing", "kokomi"],
    },
    "eye of perception": {
    "type": "catalyst", "rarity": 4, "base_atk": 510, "substat": "atk_percent", "substat_val": 41.3,
    "ability": "",
    "tags": [],
    },
    "fading twilight": {
    "type": "bow", "rarity": 4, "base_atk": 454, "substat": "energy_recharge", "substat_val": 30.6,
    "ability": "Weapon cycles between 3 states: 6% DMG Bonus, 10% ATK, or 6% Energy Recharge.",
    "tags": ["er", "atk_scaling", "dmg_bonus", "f2p", "event"],
    },
    "fang of the mountain king": {
    "type": "claymore", "rarity": 5, "base_atk": 608, "substat": "atk_percent", "substat_val": 41.3,
    "ability": "",
    "tags": [],
    },
    "favonius codex": {
    "type": "catalyst", "rarity": 4, "base_atk": 454, "substat": "energy_recharge", "substat_val": 61.3,
    "ability": "CRIT hits have a 60% chance to generate a Particle. Can occur once every 12s.",
    "tags": ["er", "support", "battery", "f2p"],
    },
    "favonius greatsword": {
    "type": "claymore", "rarity": 4, "base_atk": 510, "substat": "atk_percent", "substat_val": 41.3,
    "ability": "",
    "tags": [],
    },
    "favonius lance": {
    "type": "polearm", "rarity": 4, "base_atk": 510, "substat": "atk_percent", "substat_val": 41.3,
    "ability": "",
    "tags": [],
    },
    "favonius sword": {
    "type": "Sword", "rarity": 4, "base_atk": 454, "substat": "energy_recharge", "substat_val": 61.3,
    "ability": "CRIT hits have a 60% chance to generate 1 Elemental Particle. Can occur once every 12s.",
    "tags": ["er", "support", "battery", "f2p"],
    },
    "favonius warbow": {
    "type": "bow", "rarity": 4, "base_atk": 510, "substat": "atk_percent", "substat_val": 41.3,
    "ability": "",
    "tags": [],
    },
    "festering desire": {
    "type": "Sword", "rarity": 4, "base_atk": 510, "substat": "energy_recharge", "substat_val": 45.9,
    "ability": "Increases Elemental Skill DMG by 16% and Elemental Skill CRIT Rate by 6%.",
    "tags": ["er", "skill_dmg", "event"],
    },
    "fillet blade": {
    "type": "sword", "rarity": 4, "base_atk": 454, "substat": "atk_percent", "substat_val": 31.2,
    "ability": "On hit, has 50% chance to deal 240% ATK as single-target DMG.",
    "tags": ["atk_scaling", "f2p"],
    },
    "finale of the deep": {
    "type": "Sword", "rarity": 4, "base_atk": 565, "substat": "atk_percent", "substat_val": 51.7,
    "ability": "Using an Elemental Skill increases ATK by 12% for 15s and bonds 25% of Max HP. Bond is removed after 10s or when healed.",
    "tags": ["atk_scaling", "fontaine", "craftable"],
    },
    "flame-forged insight": {
    "type": "claymore", "rarity": 4, "base_atk": 454, "substat": "crit_rate", "substat_val": 27.6,
    "ability": "Skill hits increase ATK by 12% for 10s.",
    "tags": ["crit_rate", "atk_scaling", "skill_dmg"],
    },
    "fleuve cendre ferryman": {
    "type": "Sword", "rarity": 4, "base_atk": 510, "substat": "energy_recharge", "substat_val": 45.9,
    "ability": "Increases Elemental Skill CRIT Rate by 8%. Also increases Energy Recharge by 16% after using an Elemental Skill for 5s.",
    "tags": ["er", "skill_dmg", "f2p", "fontaine"],
    },
    "flowing purity": {
    "type": "catalyst", "rarity": 4, "base_atk": 454, "substat": "atk_percent", "substat_val": 41.3,
    "ability": "Using a skill bonds 24% of Max HP. When the bond is cleared, deal 24% more DMG for 8s.",
    "tags": ["atk_scaling", "bond_of_life", "f2p", "fontaine"],
    },
    "footprint of the rainbow": {
    "type": "polearm", "rarity": 4, "base_atk": 454, "substat": "atk_percent", "substat_val": 31.2,
    "ability": "No special effect.",
    "tags": ["f2p", "early_game"],
    },
    "forest regalia": {
    "type": "claymore", "rarity": 4, "base_atk": 510, "substat": "atk_percent", "substat_val": 41.3,
    "ability": "",
    "tags": [],
    },
    "freedom-sworn": {
    "type": "Sword", "rarity": 5, "base_atk": 608, "substat": "elemental_mastery", "substat_val": 198.2,
    "ability": "Increases DMG dealt by 10%. When the wielder triggers reactions, they gain a Sigil of Rebellion (max 2). Consuming 2 sigils grants nearby party members increased Normal/Charged/Plunging ATK by 20% and ATK by 20% for 12s.",
    "tags": ["em", "support", "team_buffer", "reaction"],
    },
    "frostbearer": {
    "type": "catalyst", "rarity": 4, "base_atk": 510, "substat": "atk_percent", "substat_val": 41.3,
    "ability": "",
    "tags": [],
    },
    "fruit of fulfillment": {
    "type": "catalyst", "rarity": 4, "base_atk": 454, "substat": "energy_recharge", "substat_val": 45.9,
    "ability": "After triggering a reaction, gain +24 EM but lose 5% ATK for 10s.",
    "tags": ["er", "em", "reaction", "f2p", "sumeru"],
    },
    "fruitful hook": {
    "type": "claymore", "rarity": 4, "base_atk": 454, "substat": "atk_percent", "substat_val": 41.3,
    "ability": "On hit, deals extra 80% ATK as physical DMG.",
    "tags": ["atk_scaling", "physical", "f2p"],
    },
    "gest of the mighty wolf": {
    "type": "claymore", "rarity": 5, "base_atk": 608, "substat": "atk_percent", "substat_val": 41.3,
    "ability": "",
    "tags": [],
    },
    "golden frostbound oath": {
    "type": "bow", "rarity": 5, "base_atk": 608, "substat": "atk_percent", "substat_val": 41.3,
    "ability": "",
    "tags": [],
    },
    "hakushin ring": {
    "type": "catalyst", "rarity": 4, "base_atk": 454, "substat": "energy_recharge", "substat_val": 45.9,
    "ability": "After triggering an Electro reaction, party members gain 10% Elemental DMG Bonus for 6s.",
    "tags": ["er", "support", "team_buffer", "craftable"],
    },
    "halberd": {
    "type": "polearm", "rarity": 4, "base_atk": 454, "substat": "atk_percent", "substat_val": 31.2,
    "ability": "Normal Attacks deal an extra 160% ATK as DMG.",
    "tags": ["atk_scaling", "f2p"],
    },
    "hamayumi": {
    "type": "bow", "rarity": 4, "base_atk": 454, "substat": "atk_percent", "substat_val": 41.3,
    "ability": "Normal and Charged ATK increased by 16%. At 100% Energy, increases by 32%.",
    "tags": ["atk_scaling", "normal_atk", "charged_atk", "craftable", "f2p"],
    },
    "haran geppaku futsu": {
    "type": "Sword", "rarity": 5, "base_atk": 608, "substat": "crit_rate", "substat_val": 33.1,
    "ability": "Gain 12% Elemental DMG Bonus for all elements. When other party members use skills, gain a Wavebold stack. Each stack (max 2) increases the wielder's Normal Attack DMG by 20% for 8s.",
    "tags": ["crit_rate", "elemental_dmg", "normal_atk"],
    },
    "harbinger of dawn": {
    "type": "Sword", "rarity": 3, "base_atk": 401, "substat": "crit_dmg", "substat_val": 62.2,
    "ability": "When HP is above 90%, CRIT Rate is increased by 14%.",
    "tags": ["crit_rate", "crit_dmg", "f2p", "low_base_atk"],
    },
    "hunter's path": {
    "type": "bow", "rarity": 5, "base_atk": 542, "substat": "crit_rate", "substat_val": 44.1,
    "ability": "All Elemental DMG Bonus increased by 12%. Charged Attack hits deal 160% of EM as additional DMG.",
    "tags": ["crit_rate", "em_scaling", "charged_atk", "tighnari"],
    },
    "ibis piercer": {
    "type": "bow", "rarity": 4, "base_atk": 454, "substat": "atk_percent", "substat_val": 41.3,
    "ability": "Charged Attack hits increase EM by 40 for 6s. Up to 2 stacks.",
    "tags": ["atk_scaling", "em", "charged_atk", "f2p"],
    },
    "ichor of the nail": {
    "type": "bow", "rarity": 4, "base_atk": 510, "substat": "atk_percent", "substat_val": 41.3,
    "ability": "",
    "tags": [],
    },
    "iron point": {
    "type": "polearm", "rarity": 4, "base_atk": 510, "substat": "atk_percent", "substat_val": 41.3,
    "ability": "",
    "tags": [],
    },
    "iron sting": {
    "type": "Sword", "rarity": 4, "base_atk": 510, "substat": "elemental_mastery", "substat_val": 165.3,
    "ability": "Dealing Elemental DMG increases all DMG by 6% for 6s. Max 2 stacks. Can occur once every 1s.",
    "tags": ["em", "dmg_bonus", "craftable", "f2p"],
    },
    "jadefall's splendor": {
    "type": "catalyst", "rarity": 5, "base_atk": 542, "substat": "atk_percent", "substat_val": 49.6,
    "ability": "Using a burst or creating a shield increases ATK by 6% for 15s (max 4 stacks).",
    "tags": ["atk_scaling", "healing", "baizhu"],
    },
    "kagotsurube isshin": {
    "type": "sword", "rarity": 4, "base_atk": 510, "substat": "atk_percent", "substat_val": 41.3,
    "ability": "",
    "tags": [],
    },
    "kagura's verity": {
    "type": "catalyst", "rarity": 5, "base_atk": 542, "substat": "crit_dmg", "substat_val": 66.2,
    "ability": "Gain 12% Elemental DMG Bonus. Using a skill grants a Kagura Dance stack (max 3) that increases Skill DMG by 12% each.",
    "tags": ["crit_dmg", "skill_dmg", "yae"],
    },
    "katsuragikiri nagamasa": {
    "type": "claymore", "rarity": 4, "base_atk": 510, "substat": "atk_percent", "substat_val": 41.3,
    "ability": "",
    "tags": [],
    },
    "key of khaj-nisut": {
    "type": "Sword", "rarity": 5, "base_atk": 542, "substat": "hp_percent", "substat_val": 66.2,
    "ability": "HP increased by 20%. When an Elemental Skill hits opponents, gain a Grand Hymn stack for 20s (max 3). Each stack increases party EM by 0.12% of the wielder's Max HP.",
    "tags": ["hp_scaling", "em_support", "team_buffer"],
    },
    "kitain cross spear": {
    "type": "polearm", "rarity": 4, "base_atk": 510, "substat": "atk_percent", "substat_val": 41.3,
    "ability": "",
    "tags": [],
    },
    "light of foliar incision": {
    "type": "Sword", "rarity": 5, "base_atk": 542, "substat": "crit_dmg", "substat_val": 88.1,
    "ability": "CRIT Rate increased by 4%. After dealing Elemental DMG, Normal and Charged Attack DMG increases by 120% of Elemental Mastery for 12s. Can occur once every 12s.",
    "tags": ["crit_dmg", "em_scaling", "dendro"],
    },
    "lion's roar": {
    "type": "Sword", "rarity": 4, "base_atk": 510, "substat": "atk_percent", "substat_val": 41.3,
    "ability": "Increases DMG against opponents affected by Pyro or Electro by 20%.",
    "tags": ["atk_scaling", "pyro", "electro", "reaction"],
    },
    "lithic blade": {
    "type": "claymore", "rarity": 4, "base_atk": 510, "substat": "atk_percent", "substat_val": 41.3,
    "ability": "",
    "tags": [],
    },
    "lithic spear": {
    "type": "polearm", "rarity": 4, "base_atk": 510, "substat": "atk_percent", "substat_val": 41.3,
    "ability": "",
    "tags": [],
    },
    "lost prayer to the sacred winds": {
    "type": "catalyst", "rarity": 5, "base_atk": 542, "substat": "crit_rate", "substat_val": 33.1,
    "ability": "Movement SPD increased by 10%. Gain 8% Elemental DMG Bonus every 4s on field (max 4 stacks).",
    "tags": ["crit_rate", "elemental_dmg", "dps"],
    },
    "lumidouce elegy": {
    "type": "polearm", "rarity": 5, "base_atk": 608, "substat": "atk_percent", "substat_val": 41.3,
    "ability": "",
    "tags": [],
    },
    "luxurious sea-lord": {
    "type": "claymore", "rarity": 4, "base_atk": 510, "substat": "atk_percent", "substat_val": 41.3,
    "ability": "",
    "tags": [],
    },
    "magic guide": {
    "type": "catalyst", "rarity": 4, "base_atk": 454, "substat": "elemental_mastery", "substat_val": 115.3,
    "ability": "Increases DMG against enemies affected by Hydro or Electro by 12%.",
    "tags": ["em", "reaction", "f2p"],
    },
    "mailed flower": {
    "type": "claymore", "rarity": 4, "base_atk": 510, "substat": "atk_percent", "substat_val": 41.3,
    "ability": "",
    "tags": [],
    },
    "makhaira aquamarine": {
    "type": "claymore", "rarity": 4, "base_atk": 510, "substat": "atk_percent", "substat_val": 41.3,
    "ability": "",
    "tags": [],
    },
    "mappa mare": {
    "type": "catalyst", "rarity": 4, "base_atk": 454, "substat": "elemental_mastery", "substat_val": 165.3,
    "ability": "Triggering a reaction grants 8% Elemental DMG Bonus for 10s (max 2 stacks).",
    "tags": ["em", "elemental_dmg", "craftable", "f2p"],
    },
    "master key": {
    "type": "claymore", "rarity": 4, "base_atk": 454, "substat": "atk_percent", "substat_val": 41.3,
    "ability": "When the wielder triggers a reaction, gain 6% ATK and 2 Energy.",
    "tags": ["atk_scaling", "er", "reaction", "f2p"],
    },
    "memory of dust": {
    "type": "catalyst", "rarity": 5, "base_atk": 542, "substat": "atk_percent", "substat_val": 49.6,
    "ability": "Increases Shield Strength by 20%. On hit, increases ATK by 4% for 8s (max 5 stacks).",
    "tags": ["atk_scaling", "shield", "liyue"],
    },
    "messenger": {
    "type": "bow", "rarity": 4, "base_atk": 454, "substat": "crit_dmg", "substat_val": 31.2,
    "ability": "Charged Attack hits on weak spots deals 100% ATK as CRIT DMG.",
    "tags": ["crit_dmg", "charged_atk", "f2p"],
    },
    "missive windspear": {
    "type": "polearm", "rarity": 4, "base_atk": 510, "substat": "atk_percent", "substat_val": 41.3,
    "ability": "",
    "tags": [],
    },
    "mistsplitter reforged": {
    "type": "sword", "rarity": 5, "base_atk": 608, "substat": "atk_percent", "substat_val": 41.3,
    "ability": "",
    "tags": [],
    },
    "mitternachts waltz": {
    "type": "bow", "rarity": 4, "base_atk": 510, "substat": "atk_percent", "substat_val": 41.3,
    "ability": "",
    "tags": [],
    },
    "moonpiercer": {
    "type": "polearm", "rarity": 4, "base_atk": 510, "substat": "atk_percent", "substat_val": 41.3,
    "ability": "",
    "tags": [],
    },
    "moonweaver's dawn": {
    "type": "sword", "rarity": 4, "base_atk": 510, "substat": "atk_percent", "substat_val": 41.3,
    "ability": "",
    "tags": [],
    },
    "mountain-bracing bolt": {
    "type": "polearm", "rarity": 4, "base_atk": 454, "substat": "def_percent", "substat_val": 51.7,
    "ability": "DEF increased by 12%. After the wielder's Geo DMG hits, all party members gain 8% Geo DMG Bonus for 10s.",
    "tags": ["def_scaling", "geo", "support", "team_buffer"],
    },
    "nightweaver's looking glass": {
    "type": "catalyst", "rarity": 5, "base_atk": 608, "substat": "atk_percent", "substat_val": 41.3,
    "ability": "",
    "tags": [],
    },
    "nocturne's curtain call": {
    "type": "catalyst", "rarity": 5, "base_atk": 542, "substat": "crit_rate", "substat_val": 27.6,
    "ability": "When HP changes, deal 12% more DMG for 8s. Max 2 stacks.",
    "tags": ["crit_rate", "hp_scaling", "dps"],
    },
    "oathsworn eye": {
    "type": "catalyst", "rarity": 4, "base_atk": 510, "substat": "atk_percent", "substat_val": 41.3,
    "ability": "",
    "tags": [],
    },
    "otherworldly story": {
    "type": "catalyst", "rarity": 4, "base_atk": 510, "substat": "atk_percent", "substat_val": 41.3,
    "ability": "",
    "tags": [],
    },
    "peak patrol song": {
    "type": "sword", "rarity": 5, "base_atk": 542, "substat": "crit_dmg", "substat_val": 88.1,
    "ability": "Movement SPD increased by 12%. When a party member triggers a reaction, all party members gain 16% ATK and 8% Elemental DMG Bonus for 10s.",
    "tags": ["crit_dmg", "team_buffer", "support", "movement_speed"],
    },
    "pocket grimoire": {
    "type": "catalyst", "rarity": 4, "base_atk": 510, "substat": "atk_percent", "substat_val": 41.3,
    "ability": "",
    "tags": [],
    },
    "polar star": {
    "type": "bow", "rarity": 5, "base_atk": 542, "substat": "crit_rate", "substat_val": 33.1,
    "ability": "Elemental Skill and Burst DMG increased by 12%. Normal, Charged, and Plunging Attacks grant Ashen stacks that increase ATK by 10% (max 4).",
    "tags": ["crit_rate", "skill_dmg", "burst_dmg", "childe"],
    },
    "portable power saw": {
    "type": "claymore", "rarity": 4, "base_atk": 454, "substat": "atk_percent", "substat_val": 41.3,
    "ability": "After party members trigger reactions, gain 4% ATK and 4% ER for 10s.",
    "tags": ["atk_scaling", "er", "team_buffer", "f2p"],
    },
    "primordial jade cutter": {
    "type": "sword", "rarity": 5, "base_atk": 608, "substat": "atk_percent", "substat_val": 41.3,
    "ability": "",
    "tags": [],
    },
    "primordial jade winged-spear": {
    "type": "polearm", "rarity": 5, "base_atk": 608, "substat": "atk_percent", "substat_val": 41.3,
    "ability": "",
    "tags": [],
    },
    "prospector's drill": {
    "type": "polearm", "rarity": 4, "base_atk": 510, "substat": "atk_percent", "substat_val": 41.3,
    "ability": "",
    "tags": [],
    },
    "prospector's shovel": {
    "type": "polearm", "rarity": 4, "base_atk": 510, "substat": "atk_percent", "substat_val": 41.3,
    "ability": "",
    "tags": [],
    },
    "prototype amber": {
    "type": "catalyst", "rarity": 4, "base_atk": 454, "substat": "hp_percent", "substat_val": 41.3,
    "ability": "Using a Burst regenerates 4 Energy every 2s for 6s and heals party.",
    "tags": ["hp_scaling", "er", "healing", "support", "craftable", "f2p"],
    },
    "prototype archaic": {
    "type": "claymore", "rarity": 4, "base_atk": 510, "substat": "atk_percent", "substat_val": 41.3,
    "ability": "",
    "tags": [],
    },
    "prototype crescent": {
    "type": "bow", "rarity": 4, "base_atk": 454, "substat": "atk_percent", "substat_val": 41.3,
    "ability": "Charged Attack hits weak spots increases Movement SPD by 10% and ATK by 36% for 10s.",
    "tags": ["atk_scaling", "charged_atk", "craftable", "f2p"],
    },
    "prototype rancour": {
    "type": "sword", "rarity": 4, "base_atk": 510, "substat": "atk_percent", "substat_val": 41.3,
    "ability": "",
    "tags": [],
    },
    "prototype starglitter": {
    "type": "polearm", "rarity": 4, "base_atk": 510, "substat": "atk_percent", "substat_val": 41.3,
    "ability": "",
    "tags": [],
    },
    "rainslasher": {
    "type": "claymore", "rarity": 4, "base_atk": 510, "substat": "atk_percent", "substat_val": 41.3,
    "ability": "",
    "tags": [],
    },
    "raven bow": {
    "type": "bow", "rarity": 4, "base_atk": 454, "substat": "elemental_mastery", "substat_val": 72.6,
    "ability": "Increases DMG against enemies affected by Hydro or Pyro by 12%.",
    "tags": ["em", "reaction", "f2p"],
    },
    "recurve bow": {
    "type": "bow", "rarity": 4, "base_atk": 454, "substat": "hp_percent", "substat_val": 35.2,
    "ability": "Defeating an opponent restores 8% HP.",
    "tags": ["hp_scaling", "healing", "f2p"],
    },
    "redhorn stonethresher": {
    "type": "claymore", "rarity": 5, "base_atk": 608, "substat": "atk_percent", "substat_val": 41.3,
    "ability": "",
    "tags": [],
    },
    "reliquary of truth": {
    "type": "catalyst", "rarity": 5, "base_atk": 542, "substat": "crit_dmg", "substat_val": 66.2,
    "ability": "When the wielder's HP changes, gain 1 Insight stack (max 4). Each stack increases Elemental Skill DMG by 12% and ATK by 8%.",
    "tags": ["crit_dmg", "skill_dmg", "atk_scaling", "hp_scaling"],
    },
    "rightful reward": {
    "type": "polearm", "rarity": 4, "base_atk": 510, "substat": "atk_percent", "substat_val": 41.3,
    "ability": "",
    "tags": [],
    },
    "ring of yaxche": {
    "type": "catalyst", "rarity": 4, "base_atk": 510, "substat": "atk_percent", "substat_val": 41.3,
    "ability": "",
    "tags": [],
    },
    "royal greatsword": {
    "type": "claymore", "rarity": 4, "base_atk": 510, "substat": "atk_percent", "substat_val": 41.3,
    "ability": "",
    "tags": [],
    },
    "royal grimoire": {
    "type": "catalyst", "rarity": 4, "base_atk": 510, "substat": "atk_percent", "substat_val": 41.3,
    "ability": "",
    "tags": [],
    },
    "royal longsword": {
    "type": "sword", "rarity": 4, "base_atk": 454, "substat": "atk_percent", "substat_val": 41.3,
    "ability": "On hit, increases CRIT Rate by 8% (max 5 stacks). On CRIT, removes all stacks.",
    "tags": ["atk_scaling", "crit_rate", "starglitter"],
    },
    "royal spear": {
    "type": "polearm", "rarity": 4, "base_atk": 510, "substat": "atk_percent", "substat_val": 41.3,
    "ability": "",
    "tags": [],
    },
    "rust": {
    "type": "bow", "rarity": 4, "base_atk": 510, "substat": "atk_percent", "substat_val": 41.3,
    "ability": "",
    "tags": [],
    },
    "sacrificer's staff": {
    "type": "polearm", "rarity": 4, "base_atk": 510, "substat": "atk_percent", "substat_val": 41.3,
    "ability": "",
    "tags": [],
    },
    "sacrificial bow": {
    "type": "bow", "rarity": 4, "base_atk": 454, "substat": "energy_recharge", "substat_val": 61.3,
    "ability": "After using Elemental Skill, 40% chance to reset its CD. Can occur once every 30s.",
    "tags": ["er", "skill_reset", "support", "f2p"],
    },
    "sacrificial fragments": {
    "type": "catalyst", "rarity": 4, "base_atk": 454, "substat": "elemental_mastery", "substat_val": 221.5,
    "ability": "After using Elemental Skill, 40% chance to reset its CD. Can occur once every 30s.",
    "tags": ["em", "skill_reset", "support", "f2p"],
    },
    "sacrificial greatsword": {
    "type": "claymore", "rarity": 4, "base_atk": 510, "substat": "atk_percent", "substat_val": 41.3,
    "ability": "",
    "tags": [],
    },
    "sacrificial jade": {
    "type": "catalyst", "rarity": 4, "base_atk": 510, "substat": "atk_percent", "substat_val": 41.3,
    "ability": "",
    "tags": [],
    },
    "sacrificial sword": {
    "type": "sword", "rarity": 4, "base_atk": 510, "substat": "atk_percent", "substat_val": 41.3,
    "ability": "",
    "tags": [],
    },
    "sapwood blade": {
    "type": "sword", "rarity": 4, "base_atk": 510, "substat": "atk_percent", "substat_val": 41.3,
    "ability": "",
    "tags": [],
    },
    "scion of the blazing sun": {
    "type": "bow", "rarity": 4, "base_atk": 510, "substat": "atk_percent", "substat_val": 41.3,
    "ability": "",
    "tags": [],
    },
    "seasoned hunter's bow": {
    "type": "bow", "rarity": 4, "base_atk": 510, "substat": "atk_percent", "substat_val": 41.3,
    "ability": "",
    "tags": [],
    },
    "sequence of solitude": {
    "type": "bow", "rarity": 4, "base_atk": 510, "substat": "atk_percent", "substat_val": 41.3,
    "ability": "",
    "tags": [],
    },
    "serpent spine": {
    "type": "claymore", "rarity": 4, "base_atk": 510, "substat": "atk_percent", "substat_val": 41.3,
    "ability": "",
    "tags": [],
    },
    "seven edicts of dust and light": {
    "type": "catalyst", "rarity": 5, "base_atk": 608, "substat": "atk_percent", "substat_val": 41.3,
    "ability": "",
    "tags": [],
    },
    "sharpshooter's oath": {
    "type": "bow", "rarity": 4, "base_atk": 454, "substat": "crit_dmg", "substat_val": 39.1,
    "ability": "Increases DMG against weak spots by 24%.",
    "tags": ["crit_dmg", "charged_atk", "f2p"],
    },
    "silvershower heartstrings": {
    "type": "bow", "rarity": 5, "base_atk": 608, "substat": "atk_percent", "substat_val": 41.3,
    "ability": "",
    "tags": [],
    },
    "skyrider sword": {
    "type": "sword", "rarity": 4, "base_atk": 510, "substat": "atk_percent", "substat_val": 41.3,
    "ability": "",
    "tags": [],
    },
    "skyward atlas": {
    "type": "catalyst", "rarity": 5, "base_atk": 542, "substat": "atk_percent", "substat_val": 33.1,
    "ability": "Elemental DMG Bonus increased by 12%. Normal attacks have a 50% chance to hit for 160% ATK AoE DMG.",
    "tags": ["atk_scaling", "elemental_dmg", "universal"],
    },
    "skyward blade": {
    "type": "sword", "rarity": 5, "base_atk": 608, "substat": "atk_percent", "substat_val": 41.3,
    "ability": "",
    "tags": [],
    },
    "skyward harp": {
    "type": "bow", "rarity": 5, "base_atk": 542, "substat": "crit_rate", "substat_val": 22.1,
    "ability": "CRIT DMG increased by 20%. Hits have a 60% chance to deal 125% ATK as AoE DMG.",
    "tags": ["crit_rate", "crit_dmg", "universal"],
    },
    "skyward pride": {
    "type": "claymore", "rarity": 5, "base_atk": 608, "substat": "atk_percent", "substat_val": 41.3,
    "ability": "",
    "tags": [],
    },
    "skyward spine": {
    "type": "polearm", "rarity": 5, "base_atk": 608, "substat": "atk_percent", "substat_val": 41.3,
    "ability": "",
    "tags": [],
    },
    "slingshot": {
    "type": "bow", "rarity": 4, "base_atk": 454, "substat": "crit_rate", "substat_val": 18.9,
    "ability": "If Normal or Charged Attack hits within 0.3s, DMG increased by 36%. Otherwise, decreased by 10%.",
    "tags": ["crit_rate", "normal_atk", "f2p"],
    },
    "snow-tombed starsilver": {
    "type": "claymore", "rarity": 4, "base_atk": 510, "substat": "atk_percent", "substat_val": 41.3,
    "ability": "",
    "tags": [],
    },
    "solar pearl": {
    "type": "catalyst", "rarity": 4, "base_atk": 454, "substat": "crit_rate", "substat_val": 27.6,
    "ability": "Normal Attack hits increase Skill and Burst DMG by 20% for 6s.",
    "tags": ["crit_rate", "skill_dmg", "burst_dmg", "battle_pass"],
    },
    "song of broken pines": {
    "type": "claymore", "rarity": 5, "base_atk": 608, "substat": "atk_percent", "substat_val": 41.3,
    "ability": "",
    "tags": [],
    },
    "song of stillness": {
    "type": "bow", "rarity": 4, "base_atk": 454, "substat": "atk_percent", "substat_val": 41.3,
    "ability": "After being healed, deal 16% more DMG for 8s.",
    "tags": ["atk_scaling", "healing_synergy", "f2p", "fontaine"],
    },
    "splendor of tranquil waters": {
    "type": "sword", "rarity": 5, "base_atk": 608, "substat": "atk_percent", "substat_val": 41.3,
    "ability": "",
    "tags": [],
    },
    "staff of homa": {
    "type": "polearm", "rarity": 5, "base_atk": 608, "substat": "atk_percent", "substat_val": 41.3,
    "ability": "",
    "tags": [],
    },
    "staff of the scarlet sands": {
    "type": "polearm", "rarity": 5, "base_atk": 608, "substat": "atk_percent", "substat_val": 41.3,
    "ability": "",
    "tags": [],
    },
    "starcaller's watch": {
    "type": "catalyst", "rarity": 5, "base_atk": 542, "substat": "hp_percent", "substat_val": 49.6,
    "ability": "When the wielder heals or shields, creates a Protective Bubble dealing 120% of Max HP as AoE DMG.",
    "tags": ["hp_scaling", "healing", "shield"],
    },
    "stringless": {
    "type": "bow", "rarity": 4, "base_atk": 510, "substat": "atk_percent", "substat_val": 41.3,
    "ability": "",
    "tags": [],
    },
    "summit shaper": {
    "type": "sword", "rarity": 5, "base_atk": 608, "substat": "atk_percent", "substat_val": 41.3,
    "ability": "",
    "tags": [],
    },
    "sunny morning sleep-in": {
    "type": "catalyst", "rarity": 5, "base_atk": 542, "substat": "crit_rate", "substat_val": 33.1,
    "ability": "When a party member triggers a reaction, all party members gain 10% ATK and 6% Elemental DMG Bonus for 8s.",
    "tags": ["crit_rate", "team_buffer", "reaction"],
    },
    "surf's up": {
    "type": "catalyst", "rarity": 5, "base_atk": 542, "substat": "crit_dmg", "substat_val": 66.2,
    "ability": "Max HP increased by 20%. When HP changes, Normal Attack DMG increases by 18% for 8s.",
    "tags": ["crit_dmg", "hp_scaling", "mualani"],
    },
    "sword of descension": {
    "type": "sword", "rarity": 4, "base_atk": 454, "substat": "atk_percent", "substat_val": 41.3,
    "ability": "On hit, has a 50% chance to deal 200% ATK as AoE DMG.",
    "tags": ["atk_scaling", "dps"],
    },
    "sword of narzissenkreuz": {
    "type": "sword", "rarity": 4, "base_atk": 510, "substat": "atk_percent", "substat_val": 41.3,
    "ability": "",
    "tags": [],
    },
    "symphonist of scents": {
    "type": "polearm", "rarity": 5, "base_atk": 542, "substat": "elemental_mastery", "substat_val": 165.3,
    "ability": "Party members gain 20% Healing Bonus and 32 Elemental DMG Bonus for their element.",
    "tags": ["em", "support", "healing", "team_buffer"],
    },
    "talking stick": {
    "type": "claymore", "rarity": 4, "base_atk": 510, "substat": "atk_percent", "substat_val": 41.3,
    "ability": "",
    "tags": [],
    },
    "tamayuratei no ohanashi": {
    "type": "polearm", "rarity": 4, "base_atk": 454, "substat": "atk_percent", "substat_val": 41.3,
    "ability": "After triggering a reaction, ATK increased by 16% for 8s.",
    "tags": ["atk_scaling", "reaction", "event"],
    },
    "the alley flash": {
    "type": "Sword", "rarity": 4, "base_atk": 595, "substat": "elemental_mastery", "substat_val": 99.1,
    "ability": "Increases DMG taken by the wielder by 20%. When the wielder takes DMG, the effect is removed for 5s.",
    "tags": ["em", "dps"],
    },
    "the bell": {
    "type": "claymore", "rarity": 4, "base_atk": 510, "substat": "atk_percent", "substat_val": 41.3,
    "ability": "",
    "tags": [],
    },
    "the black sword": {
    "type": "sword", "rarity": 4, "base_atk": 510, "substat": "atk_percent", "substat_val": 41.3,
    "ability": "",
    "tags": [],
    },
    "the catch": {
    "type": "polearm", "rarity": 4, "base_atk": 510, "substat": "atk_percent", "substat_val": 41.3,
    "ability": "",
    "tags": [],
    },
    "the daybreak chronicles": {
    "type": "bow", "rarity": 5, "base_atk": 542, "substat": "crit_rate", "substat_val": 33.1,
    "ability": "When a party member triggers a reaction, all party members gain 8% ATK and 12% Normal Attack DMG for 12s.",
    "tags": ["crit_rate", "team_buffer", "reaction"],
    },
    "the dockhand's assistant": {
    "type": "sword", "rarity": 4, "base_atk": 510, "substat": "atk_percent", "substat_val": 41.3,
    "ability": "",
    "tags": [],
    },
    "the first great magic": {
    "type": "bow", "rarity": 5, "base_atk": 542, "substat": "crit_dmg", "substat_val": 66.2,
    "ability": "Charged Attack DMG increased by 16%. For each party member with the same Elemental Type as the user, ATK increases by 16% (max 2 stacks).",
    "tags": ["crit_dmg", "charged_atk", "lyney"],
    },
    "the flute": {
    "type": "sword", "rarity": 4, "base_atk": 510, "substat": "atk_percent", "substat_val": 41.3,
    "ability": "",
    "tags": [],
    },
    "the stringless": {
    "type": "bow", "rarity": 4, "base_atk": 454, "substat": "elemental_mastery", "substat_val": 165.3,
    "ability": "Elemental Skill and Burst DMG increased by 24%.",
    "tags": ["em", "skill_dmg", "burst_dmg", "f2p"],
    },
    "the unforged": {
    "type": "claymore", "rarity": 5, "base_atk": 608, "substat": "atk_percent", "substat_val": 41.3,
    "ability": "",
    "tags": [],
    },
    "the viridescent hunt": {
    "type": "bow", "rarity": 4, "base_atk": 510, "substat": "atk_percent", "substat_val": 41.3,
    "ability": "",
    "tags": [],
    },
    "the widsith": {
    "type": "catalyst", "rarity": 4, "base_atk": 454, "substat": "crit_dmg", "substat_val": 55.1,
    "ability": "When entering the field, gain a random song for 10s: 60% ATK, 48% Elemental DMG, or 240 EM.",
    "tags": ["crit_dmg", "dps"],
    },
    "thrilling tales of dragon slayers": {
    "type": "catalyst", "rarity": 4, "base_atk": 454, "substat": "hp_percent", "substat_val": 35.2,
    "ability": "When switching to another character, increases their ATK by 24% for 10s.",
    "tags": ["hp_scaling", "support", "team_buffer", "f2p"],
    },
    "thundering pulse": {
    "type": "bow", "rarity": 5, "base_atk": 542, "substat": "crit_dmg", "substat_val": 66.2,
    "ability": "ATK increased by 20%. Gain a Thunder Emblem stack that increases Normal Attack DMG by 12% (max 3).",
    "tags": ["crit_dmg", "atk_scaling", "normal_atk", "yoimiya"],
    },
    "tidal shadow": {
    "type": "claymore", "rarity": 4, "base_atk": 510, "substat": "atk_percent", "substat_val": 41.3,
    "ability": "",
    "tags": [],
    },
    "tome of the eternal flow": {
    "type": "catalyst", "rarity": 5, "base_atk": 542, "substat": "crit_dmg", "substat_val": 88.1,
    "ability": "HP increased by 16%. When HP changes, Charged Attack DMG increases by 14% for 4s (max 3 stacks).",
    "tags": ["crit_dmg", "hp_scaling", "neuvillette"],
    },
    "toukabou shigure": {
    "type": "sword", "rarity": 4, "base_atk": 510, "substat": "atk_percent", "substat_val": 41.3,
    "ability": "",
    "tags": [],
    },
    "traveler's handy sword": {
    "type": "sword", "rarity": 4, "base_atk": 454, "substat": "def_percent", "substat_val": 46.9,
    "ability": "Picking up an Elemental Particle or Orb restores 1% HP.",
    "tags": ["def_scaling", "healing", "f2p"],
    },
    "tulaytullah's remembrance": {
    "type": "catalyst", "rarity": 5, "base_atk": 542, "substat": "crit_dmg", "substat_val": 44.1,
    "ability": "Normal ATK SPD increased by 10%. After using a skill, Normal Attack DMG increases by 48% for 12s.",
    "tags": ["crit_dmg", "normal_atk", "wanderer"],
    },
    "twin nephrite": {
    "type": "catalyst", "rarity": 4, "base_atk": 454, "substat": "crit_rate", "substat_val": 28.8,
    "ability": "Defeating an opponent increases Movement SPD and ATK by 12% for 15s.",
    "tags": ["crit_rate", "atk_scaling", "f2p"],
    },
    "ultimate overlord's mega magic sword": {
    "type": "claymore", "rarity": 4, "base_atk": 510, "substat": "atk_percent", "substat_val": 41.3,
    "ability": "",
    "tags": [],
    },
    "uraku misugiri": {
    "type": "sword", "rarity": 5, "base_atk": 608, "substat": "atk_percent", "substat_val": 41.3,
    "ability": "",
    "tags": [],
    },
    "verdict": {
    "type": "claymore", "rarity": 5, "base_atk": 608, "substat": "atk_percent", "substat_val": 41.3,
    "ability": "",
    "tags": [],
    },
    "vivid notions": {
    "type": "catalyst", "rarity": 5, "base_atk": 608, "substat": "atk_percent", "substat_val": 41.3,
    "ability": "",
    "tags": [],
    },
    "vortex vanquisher": {
    "type": "polearm", "rarity": 5, "base_atk": 608, "substat": "atk_percent", "substat_val": 41.3,
    "ability": "",
    "tags": [],
    },
    "waster greatsword": {
    "type": "claymore", "rarity": 4, "base_atk": 454, "substat": "atk_percent", "substat_val": 28.2,
    "ability": "No special effect.",
    "tags": ["f2p", "early_game"],
    },
    "wavebreaker's fin": {
    "type": "polearm", "rarity": 4, "base_atk": 510, "substat": "atk_percent", "substat_val": 41.3,
    "ability": "",
    "tags": [],
    },
    "waveriding whirl": {
    "type": "catalyst", "rarity": 4, "base_atk": 510, "substat": "atk_percent", "substat_val": 41.3,
    "ability": "",
    "tags": [],
    },
    "white iron greatsword": {
    "type": "claymore", "rarity": 4, "base_atk": 454, "substat": "def_percent", "substat_val": 35.2,
    "ability": "Defeating an opponent restores 8% HP.",
    "tags": ["def_scaling", "healing", "f2p"],
    },
    "white tassel": {
    "type": "polearm", "rarity": 4, "base_atk": 454, "substat": "crit_rate", "substat_val": 23.4,
    "ability": "Normal Attacks deal 24% more DMG.",
    "tags": ["crit_rate", "normal_atk", "f2p"],
    },
    "whiteblind": {
    "type": "claymore", "rarity": 4, "base_atk": 510, "substat": "atk_percent", "substat_val": 41.3,
    "ability": "",
    "tags": [],
    },
    "windblume ode": {
    "type": "bow", "rarity": 4, "base_atk": 510, "substat": "atk_percent", "substat_val": 41.3,
    "ability": "",
    "tags": [],
    },
    "wine and song": {
    "type": "catalyst", "rarity": 4, "base_atk": 510, "substat": "atk_percent", "substat_val": 41.3,
    "ability": "",
    "tags": [],
    },
    "wolf's gravestone": {
    "type": "claymore", "rarity": 5, "base_atk": 608, "substat": "atk_percent", "substat_val": 41.3,
    "ability": "",
    "tags": [],
    },
    "wolf-fang": {
    "type": "sword", "rarity": 4, "base_atk": 510, "substat": "atk_percent", "substat_val": 41.3,
    "ability": "",
    "tags": [],
    },
    "xiphos' moonlight": {
    "type": "sword", "rarity": 4, "base_atk": 510, "substat": "atk_percent", "substat_val": 41.3,
    "ability": "",
    "tags": [],
    },
}
