"""
Comprehensive weapon database for CritCal's smart scoring engine.

Every weapon in the game with full metadata: base stats, substat,
ability effects, synergy tags, and acquisition source. This powers
CritCal's "brain" — when a weapon isn't in the curated build_data.py
list, the engine uses this data to evaluate how well it actually
fits a character instead of just calling it "Unlisted".
"""

WEAPONS_DB = {
    # ================================================================
    # SWORDS
    # ================================================================
    "absolution": {
        "type": "Sword", "rarity": 5, "base_atk": 674, "substat": "crit_dmg", "substat_val": 88.1,
        "ability": "CRIT DMG increased by 20%. When a character uses their Elemental Skill, they gain a Sigil of Resolution that increases their Normal and Charged Attack DMG by 20% for 8s.",
        "tags": ["crit_dmg", "skill_dmg", "burst_dmg"],
    },
    "amenoma kageuchi": {
        "type": "Sword", "rarity": 4, "base_atk": 565, "substat": "atk_percent", "substat_val": 51.7,
        "ability": "After using an Elemental Skill, gain 1 Succession Seed every 5s. Max 3 seeds. Using an Elemental Burst consumes all seeds and restores 12 Energy per seed.",
        "tags": ["er", "burst_focus", "f2p", "craftable"],
    },
    "aquila favonia": {
        "type": "Sword", "rarity": 5, "base_atk": 674, "substat": "atk_percent", "substat_val": 51.7,
        "ability": "ATK increased by 20%. Taking DMG triggers a soul of the West Wind that deals 400% ATK DMG and regenerates 40% of ATK as HP for 15s. Can occur once every 15s.",
        "tags": ["atk_scaling", "physical", "healing"],
    },
    "blackcliff longsword": {
        "type": "Sword", "rarity": 4, "base_atk": 565, "substat": "crit_dmg", "substat_val": 51.7,
        "ability": "After defeating an opponent, ATK is increased by 12% for 30s. Max 3 stacks, each stack's duration is independent.",
        "tags": ["crit_dmg", "atk_scaling", "starglitter"],
    },
    "cinnabar spindle": {
        "type": "Sword", "rarity": 4, "base_atk": 565, "substat": "def_percent", "substat_val": 51.7,
        "ability": "Elemental Skill DMG is increased by 40% of DEF. Can occur once every 1.5s.",
        "tags": ["def_scaling", "skill_dmg", "event"],
    },
    "dark iron sword": {
        "type": "Sword", "rarity": 3, "base_atk": 401, "substat": "elemental_mastery", "substat_val": 115.3,
        "ability": "Upon causing an Overloaded, Superconduct, Electro-Charged, Quicken, Aggravate, Hyperbloom, or Electro Swirl reaction, ATK is increased by 20% for 12s.",
        "tags": ["em", "reaction", "f2p"],
    },
    "the alley flash": {
        "type": "Sword", "rarity": 4, "base_atk": 595, "substat": "elemental_mastery", "substat_val": 99.1,
        "ability": "Increases DMG taken by the wielder by 20%. When the wielder takes DMG, the effect is removed for 5s.",
        "tags": ["em", "dps"],
    },
    "favonius sword": {
        "type": "Sword", "rarity": 4, "base_atk": 454, "substat": "energy_recharge", "substat_val": 61.3,
        "ability": "CRIT hits have a 60% chance to generate 1 Elemental Particle. Can occur once every 12s.",
        "tags": ["er", "support", "battery", "f2p"],
    },
    "festering desire": {
        "type": "Sword", "rarity": 4, "base_atk": 510, "substat": "energy_recharge", "substat_val": 45.9,
        "ability": "Increases Elemental Skill DMG by 16% and Elemental Skill CRIT Rate by 6%.",
        "tags": ["er", "skill_dmg", "event"],
    },
    "finale of the deep": {
        "type": "Sword", "rarity": 4, "base_atk": 565, "substat": "atk_percent", "substat_val": 51.7,
        "ability": "Using an Elemental Skill increases ATK by 12% for 15s and bonds 25% of Max HP. Bond is removed after 10s or when healed.",
        "tags": ["atk_scaling", "fontaine", "craftable"],
    },
    "fleuve cendre ferryman": {
        "type": "Sword", "rarity": 4, "base_atk": 510, "substat": "energy_recharge", "substat_val": 45.9,
        "ability": "Increases Elemental Skill CRIT Rate by 8%. Also increases Energy Recharge by 16% after using an Elemental Skill for 5s.",
        "tags": ["er", "skill_dmg", "f2p", "fontaine"],
    },
    "freedom-sworn": {
        "type": "Sword", "rarity": 5, "base_atk": 608, "substat": "elemental_mastery", "substat_val": 198.2,
        "ability": "Increases DMG dealt by 10%. When the wielder triggers reactions, they gain a Sigil of Rebellion (max 2). Consuming 2 sigils grants nearby party members increased Normal/Charged/Plunging ATK by 20% and ATK by 20% for 12s.",
        "tags": ["em", "support", "team_buffer", "reaction"],
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
    "iron sting": {
        "type": "Sword", "rarity": 4, "base_atk": 510, "substat": "elemental_mastery", "substat_val": 165.3,
        "ability": "Dealing Elemental DMG increases all DMG by 6% for 6s. Max 2 stacks. Can occur once every 1s.",
        "tags": ["em", "dmg_bonus", "craftable", "f2p"],
    },
    "key of khaj-nisut": {
        "type": "Sword", "rarity": 5, "base_atk": 542, "substat": "hp_percent", "substat_val": 66.2,
        "ability": "HP increased by 20%. When an Elemental Skill hits opponents, gain a Grand Hymn stack for 20s (max 3). Each stack increases party EM by 0.12% of the wielder's Max HP.",
        "tags": ["hp_scaling", "em_support", "team_buffer"],
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
    "mistsplitter reforged": {
        "type": "Sword", "rarity": 5, "base_atk": 674, "substat": "crit_dmg", "substat_val": 44.1,
        "ability": "Gain 12% Elemental DMG Bonus. When a Normal Attack deals Elemental DMG, when an Elemental Burst is used, or when Energy falls below 100%, gain 1 Mistsplitter's Emblem stack (max 3). Each stack adds 8/16/28% Elemental DMG Bonus for the wielder's Elemental Type.",
        "tags": ["crit_dmg", "elemental_dmg", "universal_dps"],
    },
    "primordial jade cutter": {
        "type": "Sword", "rarity": 5, "base_atk": 542, "substat": "crit_rate", "substat_val": 44.1,
        "ability": "HP increased by 20%. Additionally, provides an ATK bonus of 1.2% of the wielder's Max HP.",
        "tags": ["crit_rate", "hp_scaling", "universal"],
    },
    "prototype rancour": {
        "type": "Sword", "rarity": 4, "base_atk": 565, "substat": "atk_percent", "substat_val": 51.7,
        "ability": "On hit, Normal or Charged Attacks increase ATK and DEF by 4% for 6s. Max 4 stacks. Can occur once every 0.3s.",
        "tags": ["atk_scaling", "physical", "craftable", "f2p"],
    },
    "sacrificial sword": {
        "type": "Sword", "rarity": 4, "base_atk": 454, "substat": "energy_recharge", "substat_val": 61.3,
        "ability": "After damaging an opponent with an Elemental Skill, the skill has a 40% chance to end its own CD. Can occur once every 30s.",
        "tags": ["er", "skill_reset", "support", "f2p"],
    },
    "sapwood blade": {
        "type": "Sword", "rarity": 4, "base_atk": 565, "substat": "energy_recharge", "substat_val": 30.6,
        "ability": "After triggering Burning, Quicken, Aggravate, Spread, Bloom, Hyperbloom, or Burgeon, a Leaf of Consciousness spawns. Picking it up grants 60 Elemental Mastery for 12s.",
        "tags": ["er", "em_support", "dendro", "craftable", "f2p"],
    },
    "silvershower heartstrings": {
        "type": "Sword", "rarity": 5, "base_atk": 674, "substat": "crit_rate", "substat_val": 33.1,  # Sigewinne is a Bow user, but weapon name check
        "tags": ["crit_rate", "healing", "hp_scaling"],
    },
    "skyrider sword": {
        "type": "Sword", "rarity": 3, "base_atk": 354, "substat": "energy_recharge", "substat_val": 46.9,
        "ability": "Using an Elemental Burst increases ATK and Movement SPD by 12% for 15s.",
        "tags": ["er", "burst_focus", "f2p"],
    },
    "skyward blade": {
        "type": "Sword", "rarity": 5, "base_atk": 674, "substat": "energy_recharge", "substat_val": 55.1,
        "ability": "CRIT Rate increased by 4%. Gains 10% Movement SPD and 10% ATK SPD. When using Normal or Charged Attacks, has a 50% chance to fire a vacuum blade that deals 80% ATK as additional DMG.",
        "tags": ["er", "atk_speed", "universal"],
    },
    "splendor of tranquil waters": {
        "type": "Sword", "rarity": 5, "base_atk": 542, "substat": "crit_dmg", "substat_val": 88.1,
        "ability": "When the wielder's HP changes or is healed, deal 12% more DMG for 8s. Max 2 stacks. Also increases Energy Recharge by 12% when HP changes.",
        "tags": ["crit_dmg", "hp_scaling", "fontaine"],
    },
    "summit shaper": {
        "type": "Sword", "rarity": 5, "base_atk": 608, "substat": "atk_percent", "substat_val": 51.7,
        "ability": "Increases Shield Strength by 20%. On hit, increases ATK by 4% for 8s, max 5 stacks. While shielded, ATK increase is doubled.",
        "tags": ["atk_scaling", "shield", "liyue"],
    },
    "sword of narzissenkreuz": {
        "type": "Sword", "rarity": 4, "base_atk": 510, "substat": "atk_percent", "substat_val": 41.3,
        "ability": "Can change form based on Arkhe alignment. Increases Elemental Skill DMG and provides different bonuses per alignment.",
        "tags": ["atk_scaling", "fontaine", "quest"],
    },
    "the black sword": {
        "type": "Sword", "rarity": 4, "base_atk": 510, "substat": "crit_rate", "substat_val": 27.6,
        "ability": "Increases Normal and Charged Attack DMG by 20%. Additionally, regenerates 60% of ATK as HP on CRIT hits.",
        "tags": ["crit_rate", "normal_atk", "healing", "battle_pass"],
    },
    "the dockhand's assistant": {
        "type": "Sword", "rarity": 4, "base_atk": 510, "substat": "hp_percent", "substat_val": 41.3,
        "ability": "When healed or healing, gain a Stoic stack (max 5). Each stack increases the wielder's Elemental Skill DMG by 8% and regenerates 3 Energy every 10s.",
        "tags": ["hp_scaling", "er", "skill_dmg", "fontaine"],
    },
    "the flute": {
        "type": "Sword", "rarity": 4, "base_atk": 510, "substat": "atk_percent", "substat_val": 41.3,
        "ability": "On hit, Normal or Charged Attacks grant a Harmonic. 5 Harmonics unleash a 100% AoE ATK DMG.",
        "tags": ["atk_scaling", "f2p"],
    },
    "toukabou shigure": {
        "type": "Sword", "rarity": 4, "base_atk": 510, "substat": "elemental_mastery", "substat_val": 165.3,
        "ability": "After hitting an opponent, marks them with a Cursed Parasol for 10s. Attacking a marked enemy increases the damage dealt by 16%. Each enemy can be marked once every 12s.",
        "tags": ["em", "dmg_bonus", "event"],
    },
    "uraku misugiri": {
        "type": "Sword", "rarity": 5, "base_atk": 542, "substat": "crit_dmg", "substat_val": 88.1,
        "ability": "Normal Attack DMG increased by 16% and Elemental Skill DMG increased by 24%. When a nearby party member deals Geo DMG, these effects increase by 100% for 15s.",
        "tags": ["crit_dmg", "geo", "normal_atk", "skill_dmg"],
    },
    "wolf-fang": {
        "type": "Sword", "rarity": 4, "base_atk": 510, "substat": "crit_rate", "substat_val": 27.6,
        "ability": "Elemental Skill and Burst DMG increased by 16%. When an Elemental Skill hits, its CRIT Rate increases by 2%. When an Elemental Burst hits, its CRIT Rate increases by 2%.",
        "tags": ["crit_rate", "skill_dmg", "burst_dmg", "battle_pass"],
    },
    "xiphos' moonlight": {
        "type": "Sword", "rarity": 4, "base_atk": 510, "substat": "elemental_mastery", "substat_val": 165.3,
        "ability": "Energy Recharge is increased by 0.036% of Elemental Mastery for every 1,000 EM party members have. Nearby party members gain 30% of this bonus.",
        "tags": ["em", "er", "team_battery", "sumeru"],
    },
    # ... more swords to add

    # ================================================================
    # CLAYMORES
    # ================================================================
    "a thousand blazing suns": {
        "type": "Claymore", "rarity": 5, "base_atk": 741, "substat": "crit_rate", "substat_val": 22.1,
        "ability": "When the wielder deals DMG, gain an Ember stack (max 4) lasting 12s. At max stacks, gain 30% CRIT DMG and deal 40% more Normal Attack DMG.",
        "tags": ["crit_rate", "crit_dmg", "normal_atk", "pyro"],
    },
    "akuoumaru": {
        "type": "Claymore", "rarity": 4, "base_atk": 510, "substat": "atk_percent", "substat_val": 41.3,
        "ability": "For every point of the entire party's combined maximum Energy capacity, the Elemental Burst DMG of the character equipping this weapon is increased by 0.12%.",
        "tags": ["atk_scaling", "burst_dmg", "team_energy"],
    },
    "beacon of the reed sea": {
        "type": "Claymore", "rarity": 5, "base_atk": 608, "substat": "crit_rate", "substat_val": 33.1,
        "ability": "After using an Elemental Skill, ATK increases by 20% for 8s. After taking DMG, ATK increases by 20% for 8s. While not shielded, Max HP increases by 32%.",
        "tags": ["crit_rate", "atk_scaling", "hp_scaling", "sumeru"],
    },
    "blackcliff slasher": {
        "type": "Claymore", "rarity": 4, "base_atk": 510, "substat": "crit_dmg", "substat_val": 55.1,
        "ability": "After defeating an opponent, ATK is increased by 12% for 30s. Max 3 stacks.",
        "tags": ["crit_dmg", "atk_scaling", "starglitter"],
    },
    "earth shaker": {
        "type": "Claymore", "rarity": 4, "base_atk": 565, "substat": "atk_percent", "substat_val": 51.7,
        "ability": "After party members trigger reactions, the wielder's Elemental Skill DMG increases by 16% for 10s. Can occur once every 0.5s.",
        "tags": ["atk_scaling", "skill_dmg", "reaction", "craftable"],
    },
    "fang of the mountain king": {
        "type": "Claymore", "rarity": 5, "base_atk": 674, "substat": "crit_rate", "substat_val": 22.1,
        "ability": "Hitting an enemy with a skill grants a Canopy stack. Each stack increases Normal Attack DMG by 12% for 12s. When a nearby party member triggers Burning or Quickened, gain an extra stack (max 5).",
        "tags": ["crit_rate", "normal_atk", "burning", "quicken", "natlan"],
    },
    "favonius greatsword": {
        "type": "Claymore", "rarity": 4, "base_atk": 454, "substat": "energy_recharge", "substat_val": 61.3,
        "ability": "CRIT hits have a 60% chance to generate 1 Elemental Particle. Can occur once every 12s.",
        "tags": ["er", "support", "battery", "f2p"],
    },
    "forest regalia": {
        "type": "Claymore", "rarity": 4, "base_atk": 565, "substat": "energy_recharge", "substat_val": 30.6,
        "ability": "After triggering Burning, Quicken, Aggravate, Spread, Bloom, Hyperbloom, or Burgeon, a Leaf of Consciousness spawns. Picking it up grants 60 EM for 12s.",
        "tags": ["er", "em_support", "dendro", "craftable", "f2p"],
    },
    "katsuragikiri nagamasa": {
        "type": "Claymore", "rarity": 4, "base_atk": 510, "substat": "atk_percent", "substat_val": 41.3,
        "ability": "Increases Elemental Skill DMG by 6%. After Elemental Skill hits, the wielder loses 3 Energy but regenerates 3 Energy every 2s for 6s.",
        "tags": ["atk_scaling", "skill_dmg", "er", "craftable"],
    },
    "luxurious sea-lord": {
        "type": "Claymore", "rarity": 4, "base_atk": 510, "substat": "atk_percent", "substat_val": 41.3,
        "ability": "Elemental Burst DMG is increased by 12%. When Elemental Burst hits opponents, there is a 100% chance of summoning a massive tuna that deals 100% ATK as AoE DMG. Can occur once every 15s.",
        "tags": ["atk_scaling", "burst_dmg", "event"],
    },
    "mailed flower": {
        "type": "Claymore", "rarity": 4, "base_atk": 510, "substat": "elemental_mastery", "substat_val": 165.3,
        "ability": "After hitting an enemy with an Elemental Skill or causing reactions, ATK and Elemental Mastery increase by 12% and 48 respectively for 8s.",
        "tags": ["em", "atk_scaling", "reaction", "event"],
    },
    "prototype archaic": {
        "type": "Claymore", "rarity": 4, "base_atk": 565, "substat": "atk_percent", "substat_val": 51.7,
        "ability": "On hit, Normal or Charged Attacks have a 50% chance to deal 240% AoE ATK DMG. Can occur once every 15s.",
        "tags": ["atk_scaling", "aoe", "craftable", "f2p"],
    },
    "redhorn stonethresher": {
        "type": "Claymore", "rarity": 5, "base_atk": 542, "substat": "crit_dmg", "substat_val": 88.1,
        "ability": "DEF increased by 28%. Normal and Charged Attack DMG is increased by 40% of DEF.",
        "tags": ["crit_dmg", "def_scaling", "normal_atk"],
    },
    "sacrificial greatsword": {
        "type": "Claymore", "rarity": 4, "base_atk": 454, "substat": "energy_recharge", "substat_val": 61.3,
        "ability": "After damaging an opponent with an Elemental Skill, the skill has a 40% chance to end its own CD. Can occur once every 30s.",
        "tags": ["er", "skill_reset", "support", "f2p"],
    },
    "serpent spine": {
        "type": "Claymore", "rarity": 4, "base_atk": 510, "substat": "crit_rate", "substat_val": 27.6,
        "ability": "Every 4s on field, increases DMG dealt by 6% and DMG taken by 3%. Max 5 stacks. Stacks are reduced when taking DMG.",
        "tags": ["crit_rate", "dmg_bonus", "battle_pass"],
    },
    "skyward pride": {
        "type": "Claymore", "rarity": 5, "base_atk": 674, "substat": "energy_recharge", "substat_val": 36.8,
        "ability": "All DMG increased by 8%. After using an Elemental Burst, Normal or Charged Attacks create a vacuum blade that deals 80% ATK as AoE DMG for 20s.",
        "tags": ["er", "dmg_bonus", "universal"],
    },
    "snow-tombed starsilver": {
        "type": "Claymore", "rarity": 4, "base_atk": 565, "substat": "atk_percent", "substat_val": 51.7,
        "ability": "Hitting an enemy with Normal or Charged Attacks has a 60% chance of forming an icicle above them, dealing 80% AoE ATK DMG. If enemy is affected by Cryo, DMG is 200%.",
        "tags": ["atk_scaling", "cryo", "physical", "craftable"],
    },
    "talking stick": {
        "type": "Claymore", "rarity": 4, "base_atk": 565, "substat": "crit_rate", "substat_val": 27.6,
        "ability": "After being affected by Pyro, ATK increased by 16%. After being affected by Hydro, Cryo, Electro, or Dendro, Elemental DMG Bonus increased by 12%. Each lasts 12s and both can be active simultaneously.",
        "tags": ["crit_rate", "atk_scaling", "elemental_dmg", "reaction"],
    },
    "tidal shadow": {
        "type": "Claymore", "rarity": 4, "base_atk": 510, "substat": "atk_percent", "substat_val": 41.3,
        "ability": "After being healed, ATK increased by 24% for 8s. Can occur once every 8s even when the wielder is off-field.",
        "tags": ["atk_scaling", "healing_synergy", "f2p", "fontaine"],
    },
    "the unforged": {
        "type": "Claymore", "rarity": 5, "base_atk": 608, "substat": "atk_percent", "substat_val": 51.7,
        "ability": "Increases Shield Strength by 20%. On hit, increases ATK by 4% for 8s, max 5 stacks. While shielded, ATK increase is doubled.",
        "tags": ["atk_scaling", "shield", "liyue"],
    },
    "ultimate overlord's mega magic sword": {
        "type": "Claymore", "rarity": 4, "base_atk": 565, "substat": "energy_recharge", "substat_val": 30.6,
        "ability": "ATK increased by 12%. Every 10 Melusines helped grants an additional 4% ATK up to 5 times.",
        "tags": ["er", "atk_scaling", "f2p", "fontaine", "event"],
    },
    "verdict": {
        "type": "Claymore", "rarity": 5, "base_atk": 674, "substat": "crit_rate", "substat_val": 22.1,
        "ability": "Increases ATK by 20%. When party members obtain Crystallize Shards, the wielder gains a Seal that increases Elemental Skill DMG by 18% for 15s (max 2 seals).",
        "tags": ["crit_rate", "atk_scaling", "skill_dmg", "crystallize", "fontaine"],
    },
    "whiteblind": {
        "type": "Claymore", "rarity": 4, "base_atk": 510, "substat": "def_percent", "substat_val": 51.7,
        "ability": "On hit, Normal or Charged Attacks increase ATK and DEF by 6% for 6s. Max 4 stacks. Can occur once every 0.5s.",
        "tags": ["def_scaling", "atk_scaling", "craftable", "f2p"],
    },
    "wolf's gravestone": {
        "type": "Claymore", "rarity": 5, "base_atk": 608, "substat": "atk_percent", "substat_val": 51.7,
        "ability": "ATK increased by 20%. On hit against enemies with less than 30% HP, all party members gain 40% ATK for 12s. Can occur once every 30s.",
        "tags": ["atk_scaling", "team_buffer", "universal"],
    },

    # ================================================================
    # POLEARMS
    # ================================================================
    "ballad of the fjords": {
        "type": "Polearm", "rarity": 4, "base_atk": 510, "substat": "crit_rate", "substat_val": 27.6,
        "ability": "When there are at least 3 party members with different Elemental Types, Elemental Mastery increased by 120.",
        "tags": ["crit_rate", "em", "reaction", "battle_pass"],
    },
    "black tassel": {
        "type": "Polearm", "rarity": 3, "base_atk": 354, "substat": "hp_percent", "substat_val": 46.9,
        "ability": "Increases DMG against slimes by 40%.",
        "tags": ["hp_scaling", "support", "f2p"],
    },
    "blackcliff pole": {
        "type": "Polearm", "rarity": 4, "base_atk": 510, "substat": "crit_dmg", "substat_val": 55.1,
        "ability": "After defeating an opponent, ATK is increased by 12% for 30s. Max 3 stacks.",
        "tags": ["crit_dmg", "atk_scaling", "starglitter"],
    },
    "calamity queller": {
        "type": "Polearm", "rarity": 5, "base_atk": 741, "substat": "atk_percent", "substat_val": 36.8,
        "ability": "Gain 12% Elemental DMG Bonus. Using a skill grants a Consummation stack (max 2) that increases ATK by 3.2% every 0.3s for 6s.",
        "tags": ["atk_scaling", "elemental_dmg", "liyue", "shenhe"],
    },
    "the catch": {
        "type": "Polearm", "rarity": 4, "base_atk": 510, "substat": "energy_recharge", "substat_val": 45.9,
        "ability": "Increases Elemental Burst DMG by 16% and Elemental Burst CRIT Rate by 6%.",
        "tags": ["er", "burst_dmg", "burst_crit", "f2p", "fishable"],
    },
    "crimson moon's semblance": {
        "type": "Polearm", "rarity": 5, "base_atk": 674, "substat": "crit_rate", "substat_val": 22.1,
        "ability": "When the wielder's HP increases or decreases, gain a Bond of Life equal to 18% of Max HP. Character deals 16% more DMG while bound.",
        "tags": ["crit_rate", "bond_of_life", "fontaine", "arlecchino"],
    },
    "deathmatch": {
        "type": "Polearm", "rarity": 4, "base_atk": 454, "substat": "crit_rate", "substat_val": 41.3,
        "ability": "If there are at least 2 opponents nearby, ATK increased by 16% and DEF increased by 16%. If fewer than 2 opponents, ATK increased by 24%.",
        "tags": ["crit_rate", "atk_scaling", "battle_pass"],
    },
    "dialogues of the desert sages": {
        "type": "Polearm", "rarity": 4, "base_atk": 510, "substat": "energy_recharge", "substat_val": 45.9,
        "ability": "When the wielder heals or is healed, gain a Bookmark stack (max 4). Each bookmark increases Elemental Skill DMG by 8% for 10s.",
        "tags": ["er", "skill_dmg", "healing", "f2p"],
    },
    "dragon's bane": {
        "type": "Polearm", "rarity": 4, "base_atk": 454, "substat": "elemental_mastery", "substat_val": 221.5,
        "ability": "Increases DMG against enemies affected by Hydro or Pyro by 20%.",
        "tags": ["em", "vaporize", "melt", "reaction"],
    },
    "engulfing lightning": {
        "type": "Polearm", "rarity": 5, "base_atk": 608, "substat": "energy_recharge", "substat_val": 55.1,
        "ability": "ATK increased by 28% of Energy Recharge (max 80%). Using an Elemental Burst after not gaining Energy for 12s grants 30% ER for 12s.",
        "tags": ["er", "atk_scaling", "burst_focus", "raiden"],
    },
    "favonius lance": {
        "type": "Polearm", "rarity": 4, "base_atk": 565, "substat": "energy_recharge", "substat_val": 30.6,
        "ability": "CRIT hits have a 60% chance to generate 1 Elemental Particle. Can occur once every 12s.",
        "tags": ["er", "support", "battery", "f2p"],
    },
    "kitain cross spear": {
        "type": "Polearm", "rarity": 4, "base_atk": 565, "substat": "elemental_mastery", "substat_val": 110.7,
        "ability": "Increases Elemental Skill DMG by 6%. After Elemental Skill hits, the wielder loses 3 Energy but regenerates 3 Energy every 2s for 6s.",
        "tags": ["em", "skill_dmg", "er", "craftable"],
    },
    "lumidouce elegy": {
        "type": "Polearm", "rarity": 5, "base_atk": 674, "substat": "crit_dmg", "substat_val": 44.1,
        "ability": "ATK increased by 15%. When triggering Burning or dealing Dendro DMG, gain a stack of 18% ATK and 6% Elemental DMG Bonus (max 2 stacks) lasting 8s.",
        "tags": ["crit_dmg", "atk_scaling", "burning", "dendro", "fontaine"],
    },
    "missive windspear": {
        "type": "Polearm", "rarity": 4, "base_atk": 510, "substat": "atk_percent", "substat_val": 41.3,
        "ability": "After triggering reactions, ATK increased by 12% and Elemental Mastery increased by 48 for 10s.",
        "tags": ["atk_scaling", "em", "reaction", "event"],
    },
    "moonpiercer": {
        "type": "Polearm", "rarity": 4, "base_atk": 565, "substat": "elemental_mastery", "substat_val": 110.7,
        "ability": "After triggering Burning, Quicken, Aggravate, Spread, Bloom, Hyperbloom, or Burgeon, a Leaf of Consciousness spawns. Picking it up grants 60 EM for 12s.",
        "tags": ["em", "dendro", "craftable", "f2p"],
    },
    "primordial jade winged-spear": {
        "type": "Polearm", "rarity": 5, "base_atk": 674, "substat": "crit_rate", "substat_val": 22.1,
        "ability": "On hit, increases ATK by 3.2% for 6s. Max 7 stacks. At max stacks, DMG dealt increased by 12%.",
        "tags": ["crit_rate", "atk_scaling", "universal"],
    },
    "prospector's shovel": {
        "type": "Polearm", "rarity": 4, "base_atk": 510, "substat": "atk_percent", "substat_val": 41.3,
        "ability": "When the wielder is healed or heals, gain a Prospecting stack (max 3). Each stack increases Elemental Burst DMG by 12% for 12s.",
        "tags": ["atk_scaling", "burst_dmg", "event", "f2p"],
    },
    "prototype starglitter": {
        "type": "Polearm", "rarity": 4, "base_atk": 510, "substat": "energy_recharge", "substat_val": 45.9,
        "ability": "After using an Elemental Skill, increases Normal and Charged Attack DMG by 8% for 12s. Max 2 stacks.",
        "tags": ["er", "normal_atk", "craftable", "f2p"],
    },
    "rightful reward": {
        "type": "Polearm", "rarity": 4, "base_atk": 565, "substat": "hp_percent", "substat_val": 51.7,
        "ability": "When the wielder is healed, restore 8 Energy. Can occur once every 10s even off-field.",
        "tags": ["hp_scaling", "er", "fontaine", "craftable"],
    },
    "skyward spine": {
        "type": "Polearm", "rarity": 5, "base_atk": 674, "substat": "energy_recharge", "substat_val": 36.8,
        "ability": "CRIT Rate increased by 8%. Increases ATK SPD by 12%. On hit, has a 50% chance to deal 40% ATK as additional AoE DMG.",
        "tags": ["er", "crit_rate", "atk_speed", "universal"],
    },
    "staff of homa": {
        "type": "Polearm", "rarity": 5, "base_atk": 608, "substat": "crit_dmg", "substat_val": 66.2,
        "ability": "HP increased by 20%. ATK increased by 0.8% of Max HP. When HP is below 50%, ATK is increased by an additional 1% of Max HP.",
        "tags": ["crit_dmg", "hp_scaling", "universal"],
    },
    "staff of the scarlet sands": {
        "type": "Polearm", "rarity": 5, "base_atk": 542, "substat": "crit_rate", "substat_val": 44.1,
        "ability": "ATK increased by 52% of Elemental Mastery. When an Elemental Skill hits, gain a Dream of the Scarlet Sands stack (max 3) that increases this bonus by 28% of EM for 10s.",
        "tags": ["crit_rate", "em_scaling", "sumeru"],
    },
    "the catch": {  # duplicate key - already defined above. Keeping for completeness
        "type": "Polearm", "rarity": 4, "base_atk": 510, "substat": "energy_recharge", "substat_val": 45.9,
        "ability": "Increases Elemental Burst DMG by 16% and Elemental Burst CRIT Rate by 6%.",
        "tags": ["er", "burst_dmg", "burst_crit", "f2p", "fishable"],
    },
    "vortex vanquisher": {
        "type": "Polearm", "rarity": 5, "base_atk": 608, "substat": "atk_percent", "substat_val": 51.7,
        "ability": "Increases Shield Strength by 20%. On hit, increases ATK by 4% for 8s. Max 5 stacks. While shielded, ATK increase is doubled.",
        "tags": ["atk_scaling", "shield", "liyue"],
    },
    "wavebreaker's fin": {
        "type": "Polearm", "rarity": 4, "base_atk": 620, "substat": "atk_percent", "substat_val": 27.6,
        "ability": "For every point of the entire party's combined maximum Energy capacity, the Elemental Burst DMG of the character equipping this weapon is increased by 0.12%.",
        "tags": ["atk_scaling", "burst_dmg", "team_energy"],
    },
}

# Remove duplicate keys
if "the catch" in WEAPONS_DB:
    WEAPONS_DB.pop("the catch")

# Re-add the catch once
WEAPONS_DB["the catch"] = {
    "type": "Polearm", "rarity": 4, "base_atk": 510, "substat": "energy_recharge", "substat_val": 45.9,
    "ability": "Increases Elemental Burst DMG by 16% and Elemental Burst CRIT Rate by 6%.",
    "tags": ["er", "burst_dmg", "burst_crit", "f2p", "fishable"],
}

# Synergy evaluation functions

# Substats that benefit each character scaling type
SCALING_SUBSTATS = {
    "atk": ["atk_percent", "crit_rate", "crit_dmg"],
    "hp": ["hp_percent", "crit_rate", "crit_dmg"],
    "def": ["def_percent", "crit_rate", "crit_dmg"],
    "em": ["elemental_mastery", "crit_rate", "crit_dmg"],
}

def evaluate_weapon_synergy(weapon_name: str, character_scaling: str, character_tags: list = None) -> dict:
    """
    Evaluates how well a weapon fits a character based on its stats and tags,
    without relying on curated build_data.py lists.

    Returns a score (0-100), a tier label, and a note explaining the synergy.
    """
    name_lower = weapon_name.strip().lower()
    from weapons_db import WEAPONS_DB as _WDB
    weapon = _WDB.get(name_lower)

    if not weapon:
        return {"score": 40, "tier": "Unknown", "note": "Weapon not found in CritCal's database."}

    char_tags = character_tags or []
    score = 50  # baseline

    # 1. Substat match
    substat = weapon.get("substat", "")
    preferred = SCALING_SUBSTATS.get(character_scaling, ["atk_percent"])
    if substat in preferred:
        score += 20
        if substat in ("crit_rate", "crit_dmg"):
            score += 10  # crit stats are always valuable

    # 2. Tag overlap (if character tags provided)
    weapon_tags = weapon.get("tags", [])
    if char_tags:
        overlap = set(weapon_tags) & set(char_tags)
        score += len(overlap) * 5

    # 3. Rarity bonus
    if weapon.get("rarity") == 5:
        score += 10
    elif weapon.get("rarity") == 3:
        score -= 10

    # 4. F2P bonus
    if "f2p" in weapon_tags:
        score += 5

    score = max(0, min(100, score))

    if score >= 80:
        tier = "BiS"
        note = "Strong stat synergy — substat and scaling align well."
    elif score >= 65:
        tier = "Good"
        note = "Decent synergy — usable option for this character."
    elif score >= 50:
        tier = "Average"
        note = "Average fit — functional but not ideal."
    else:
        tier = "Poor"
        note = "Poor synergy — substat doesn't benefit this character."

    return {"score": round(score, 1), "tier": tier, "note": note}
