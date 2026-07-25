"""
Comprehensive artifact set database for CritCal.
"""

ARTIFACTS_DB = {
    "a day carved from rising winds": {
    "bonus_2pc": "Anemo DMG +15%.",
    "bonus_4pc": "After Swirl, party gains 20% Elemental DMG Bonus for 10s.",
    "tags": ["anemo", "swirl", "support"],
    },
    "adventurer": {
    "bonus_2pc": "Max HP +1,000.",
    "bonus_4pc": "Opening a chest regenerates 30% Max HP over 5s.",
    "tags": ["early_game", "exploration"],
    },
    "archaic petra": {
    "bonus_2pc": "Geo DMG Bonus +15%.",
    "bonus_4pc": "Upon obtaining a Crystallize Shard, party members gain 35% Elemental DMG Bonus for that element for 10s. Only one bonus can exist at a time.",
    "tags": ["geo", "support", "crystallize", "team_buffer"],
    },
    "berserker": {
    "bonus_2pc": "CRIT Rate +12%.",
    "bonus_4pc": "When HP is below 70%, CRIT Rate increases by an additional 24%.",
    "tags": ["crit_rate", "early_game"],
    },
    "blizzard strayer": {
    "bonus_2pc": "Cryo DMG Bonus +15%.",
    "bonus_4pc": "CRIT Rate increased by 20% when attacking enemies affected by Cryo. If the enemy is Frozen, CRIT Rate is increased by an additional 20%.",
    "tags": ["cryo", "crit_rate", "freeze", "dps"],
    },
    "bloodstained chivalry": {
    "bonus_2pc": "Physical DMG Bonus +25%.",
    "bonus_4pc": "After defeating an opponent, increases Charged Attack DMG by 50% and reduces its stamina cost to 0 for 10s.",
    "tags": ["physical", "charged_atk"],
    },
    "brave heart": {
    "bonus_2pc": "ATK +18%.",
    "bonus_4pc": "Increases DMG by 30% against enemies with more than 50% HP.",
    "tags": ["atk_scaling", "early_game"],
    },
    "crimson witch of flames": {
    "bonus_2pc": "Pyro DMG Bonus +15%.",
    "bonus_4pc": "Increases Overloaded, Burning, and Burgeon DMG by 40%. Increases Vaporize and Melt DMG by 15%. Using an Elemental Skill increases 2pc effect by 50% for 10s (max 3 stacks).",
    "tags": ["pyro", "reaction", "vaporize", "melt", "overload"],
    },
    "deepwood memories": {
    "bonus_2pc": "Dendro DMG Bonus +15%.",
    "bonus_4pc": "Elemental Skill or Burst hits decrease enemy Dendro RES by 30% for 8s. Effective even when off-field.",
    "tags": ["dendro", "support", "res_shred", "dendro_res_shred"],
    },
    "defender's will": {
    "bonus_2pc": "DEF +30%.",
    "bonus_4pc": "For each party member with a different Elemental Type, increases Elemental RES by 30%.",
    "tags": ["def_scaling", "early_game"],
    },
    "desert pavilion chronicle": {
    "bonus_2pc": "Anemo DMG Bonus +15%.",
    "bonus_4pc": "After a Charged Attack hits, Normal Attack SPD increases by 10% and Normal, Charged, and Plunging Attack DMG increases by 30% for 10s.",
    "tags": ["anemo", "normal_atk", "charged_atk", "plunge", "dps"],
    },
    "disenchantment in deep shadow": {
    "bonus_2pc": "Cryo DMG +15%.",
    "bonus_4pc": "Deal 25% more DMG vs Cryo-affected enemies.",
    "tags": ["cryo", "dps"],
    },
    "echoes of an offering": {
    "bonus_2pc": "ATK +18%.",
    "bonus_4pc": "Normal Attacks have a 36% chance to trigger Valley Rite, increasing Normal Attack DMG by 70% of ATK. Effect removed 0.05s after a Normal Attack deals DMG.",
    "tags": ["atk_scaling", "normal_atk", "dps"],
    },
    "emblem of severed fate": {
    "bonus_2pc": "Energy Recharge +20%.",
    "bonus_4pc": "Increases Elemental Burst DMG by 25% of Energy Recharge (max 75%).",
    "tags": ["er", "burst_dmg", "universal"],
    },
    "finale of the deep (artifact)": {
    "bonus_2pc": "Healing effectiveness +15%.",
    "bonus_4pc": "After the wielder is healed, all party members deal 14% more Elemental Skill DMG for 10s. Can occur once every 10s.",
    "tags": ["healing", "support", "skill_dmg", "team_buffer", "fontaine"],
    },
    "finale of the deep galleries": {
    "bonus_2pc": "ER +20%.",
    "bonus_4pc": "After skill, party gains 10% Elemental DMG Bonus for 10s.",
    "tags": ["er", "support", "team_buffer"],
    },
    "flower of paradise lost": {
    "bonus_2pc": "Elemental Mastery +80.",
    "bonus_4pc": "Bloom, Hyperbloom, and Burgeon DMG increased by 40%. Additionally, triggering any of these reactions increases the bonus by 25% (max 4 stacks). Can occur once per second.",
    "tags": ["em", "bloom", "hyperbloom", "burgeon", "reaction"],
    },
    "fragment of harmonic whimsy": {
    "bonus_2pc": "ATK +18%.",
    "bonus_4pc": "When Bond of Life changes, deal 25% more DMG for 8s (max 3).",
    "tags": ["atk_scaling", "bond_of_life", "dps", "fontaine"],
    },
    "gambler": {
    "bonus_2pc": "Elemental Skill DMG +20%.",
    "bonus_4pc": "Defeating an opponent has a 100% chance to reset Elemental Skill CD. Can occur once every 15s.",
    "tags": ["skill_dmg", "skill_reset", "early_game"],
    },
    "gilded dreams": {
    "bonus_2pc": "Elemental Mastery +80.",
    "bonus_4pc": "For each party member with a different element, the wielder gains 50 ATK and 50 EM. For each same element, gains 50 ATK. Max 4 stacks.",
    "tags": ["em", "atk_scaling", "reaction", "dendro"],
    },
    "gladiator's finale": {
    "bonus_2pc": "ATK +18%.",
    "bonus_4pc": "If the wielder uses a Sword, Claymore, or Polearm, increases Normal Attack DMG by 35%.",
    "tags": ["atk_scaling", "normal_atk", "dps"],
    },
    "golden troupe": {
    "bonus_2pc": "Elemental Skill DMG +20%.",
    "bonus_4pc": "Elemental Skill DMG increases by 25% of the wielder's Total DEF. Additionally, while off-field, Elemental Skill DMG increases by a further 25%.",
    "tags": ["skill_dmg", "off_field", "def_scaling", "fontaine"],
    },
    "heart of depth": {
    "bonus_2pc": "Hydro DMG Bonus +15%.",
    "bonus_4pc": "After using an Elemental Skill, increases Normal and Charged Attack DMG by 30% for 15s.",
    "tags": ["hydro", "normal_atk", "charged_atk", "dps"],
    },
    "husk of opulent dreams": {
    "bonus_2pc": "DEF +30%.",
    "bonus_4pc": "A character gains Curiosity stacks (max 4) when dealing Geo DMG or while off-field for 3s. Each stack increases DEF by 6% and Geo DMG by 6%.",
    "tags": ["def_scaling", "geo", "dps", "support"],
    },
    "initiate": {
    "bonus_2pc": "ATK +10%.",
    "bonus_4pc": "",
    "tags": ["early_game"],
    },
    "instructor's": {
    "bonus_2pc": "Elemental Mastery +80.",
    "bonus_4pc": "After triggering a reaction, increases party EM by 120 for 8s.",
    "tags": ["em", "support", "team_buffer", "early_game"],
    },
    "lavawalker": {
    "bonus_2pc": "Pyro RES +40%.",
    "bonus_4pc": "Increases DMG dealt by 35% against enemies affected by Pyro.",
    "tags": ["pyro", "mono_pyro", "conditional"],
    },
    "long night's oath": {
    "bonus_2pc": "Physical DMG Bonus +25%.",
    "bonus_4pc": "After party members trigger Nightsoul Transmission, the equipping character gains 35% increased Charged Attack DMG and 5% increased CRIT Rate for 6s.",
    "tags": ["physical", "charged_atk", "crit_rate", "natlan"],
    },
    "lucky dog": {
    "bonus_2pc": "DEF +100.",
    "bonus_4pc": "Picking up Mora restores 300 HP.",
    "tags": ["early_game", "exploration"],
    },
    "maiden beloved": {
    "bonus_2pc": "Healing effectiveness +15%.",
    "bonus_4pc": "Using an Elemental Skill or Burst increases party healing received by 20% for 10s.",
    "tags": ["healing", "support", "healer"],
    },
    "marechaussee hunter": {
    "bonus_2pc": "Normal and Charged Attack DMG +15%.",
    "bonus_4pc": "When HP increases or decreases, CRIT Rate increases by 12% for 5s. Max 3 stacks.",
    "tags": ["crit_rate", "normal_atk", "charged_atk", "hp_fluctuation", "fontaine"],
    },
    "martial artist": {
    "bonus_2pc": "Normal and Charged ATK DMG +15%.",
    "bonus_4pc": "After using an Elemental Skill, Normal and Charged Attack DMG increased by 25% for 8s.",
    "tags": ["normal_atk", "early_game"],
    },
    "night of the sky's unveiling": {
    "bonus_2pc": "Elemental Mastery +80.",
    "bonus_4pc": "After a reaction, party gains 60 EM for 12s.",
    "tags": ["em", "support", "team_buffer"],
    },
    "nighttime whispers in the echoing woods": {
    "bonus_2pc": "ATK +18%.",
    "bonus_4pc": "After using an Elemental Skill, gain 20% Geo DMG Bonus for 10s. While shielded, Geo DMG Bonus increases by a further 150%.",
    "tags": ["atk_scaling", "geo", "shield", "dps", "fontaine"],
    },
    "noblesse oblige": {
    "bonus_2pc": "Elemental Burst DMG +20%.",
    "bonus_4pc": "Using an Elemental Burst increases party ATK by 20% for 12s.",
    "tags": ["burst_dmg", "support", "team_buffer", "universal"],
    },
    "nymph's dream": {
    "bonus_2pc": "Hydro DMG Bonus +15%.",
    "bonus_4pc": "After Normal, Charged, or Plunging attacks, Elemental Skills, or Elemental Bursts hit, gain a stack of 25% ATK and 15% Hydro DMG (max 3 stacks).",
    "tags": ["hydro", "atk_scaling", "dps", "normal_atk", "skill_dmg"],
    },
    "obsidian codex": {
    "bonus_2pc": "When the wielder is in Nightsoul's Blessing and on field, all DMG dealt increases by 15%.",
    "bonus_4pc": "After the wielder consumes 20 Nightsoul points, CRIT Rate increases by 25% while in Nightsoul's Blessing for 10s.",
    "tags": ["crit_rate", "nightsoul", "natlan", "dps"],
    },
    "ocean-hued clam": {
    "bonus_2pc": "Healing Bonus +15%.",
    "bonus_4pc": "When the wielder heals, accumulates a Sea-Dyed Foam for 3s. When it expires, deals physical DMG equal to 90% of the accumulated healing (max 30,000 HP).",
    "tags": ["healing", "physical", "sub_dps", "healer"],
    },
    "pale flame": {
    "bonus_2pc": "Physical DMG Bonus +25%.",
    "bonus_4pc": "When an Elemental Skill hits, ATK increases by 9% for 7s (max 2 stacks). At 2 stacks, Physical 2pc bonus doubles.",
    "tags": ["physical", "skill_dmg", "dps"],
    },
    "prayers for destiny": {
    "bonus_2pc": "Hydro RES +40%.",
    "bonus_4pc": "",
    "tags": ["defensive"],
    },
    "prayers for illumination": {
    "bonus_2pc": "Pyro RES +40%.",
    "bonus_4pc": "",
    "tags": ["defensive"],
    },
    "prayers for wisdom": {
    "bonus_2pc": "Electro RES +40%.",
    "bonus_4pc": "",
    "tags": ["defensive"],
    },
    "prayers to springtime": {
    "bonus_2pc": "Cryo RES +40%.",
    "bonus_4pc": "",
    "tags": ["defensive"],
    },
    "resolution of sojourner": {
    "bonus_2pc": "ATK +18%.",
    "bonus_4pc": "Charged Attack CRIT Rate +30%.",
    "tags": ["atk_scaling", "charged_atk", "early_game"],
    },
    "retracing bolide": {
    "bonus_2pc": "Shield Strength +35%.",
    "bonus_4pc": "While shielded, gain 40% additional Normal and Charged Attack DMG.",
    "tags": ["shield", "normal_atk", "charged_atk", "conditional"],
    },
    "scholar": {
    "bonus_2pc": "Energy Recharge +20%.",
    "bonus_4pc": "Gaining Elemental Particles or Orbs regenerates 3 Energy for all party members with a bow or catalyst. Can occur once every 3s.",
    "tags": ["er", "support", "early_game"],
    },
    "scroll of the hero of cinder city": {
    "bonus_2pc": "When a nearby party member triggers a Nightsoul Transmission, the equipping character gains 6 Nightsoul points.",
    "bonus_4pc": "When the wielder triggers a reaction, party members gain 28% Elemental DMG Bonus for the elements involved for 20s.",
    "tags": ["support", "team_buffer", "elemental_dmg", "natlan"],
    },
    "shimenawa's reminiscence": {
    "bonus_2pc": "ATK +18%.",
    "bonus_4pc": "When using an Elemental Skill with 15+ Energy, consume 15 Energy and increase Normal/Charged/Plunging Attack DMG by 50% for 10s.",
    "tags": ["atk_scaling", "normal_atk", "charged_atk", "dps"],
    },
    "silken moon's serenade": {
    "bonus_2pc": "ER +20%.",
    "bonus_4pc": "After Burst, party gains 12% Elemental DMG Bonus for 12s.",
    "tags": ["er", "support", "team_buffer"],
    },
    "song of days past": {
    "bonus_2pc": "Healing Bonus +15%.",
    "bonus_4pc": "When the wielder heals, records healing for 8s. When the record reaches 15,000, creates a 10s field that increases party DMG by 8% of the healing recorded (max 1,200 per trigger).",
    "tags": ["healing", "support", "team_buffer", "fontaine"],
    },
    "tenacity of the millelith": {
    "bonus_2pc": "HP +20%.",
    "bonus_4pc": "When an Elemental Skill hits, party ATK increases by 20% and Shield Strength increases by 30% for 3s.",
    "tags": ["hp_scaling", "support", "team_buffer", "shield"],
    },
    "the exile": {
    "bonus_2pc": "Energy Recharge +20%.",
    "bonus_4pc": "Using an Elemental Burst regenerates 2 Energy for all party members (excluding the wielder) every 2s for 6s.",
    "tags": ["er", "support", "team_battery", "early_game"],
    },
    "thundering fury": {
    "bonus_2pc": "Electro DMG Bonus +15%.",
    "bonus_4pc": "Increases Overloaded, Electro-Charged, Superconduct, Hyperbloom, and Aggravate DMG by 40%. Electro reaction triggers reduce Skill CD by 1s. Can occur once every 0.8s.",
    "tags": ["electro", "reaction", "skill_cd", "aggravate", "hyperbloom"],
    },
    "thundersoother": {
    "bonus_2pc": "Electro RES +40%.",
    "bonus_4pc": "Increases DMG dealt by 35% against enemies affected by Electro.",
    "tags": ["electro", "mono_electro", "conditional"],
    },
    "tiny miracle": {
    "bonus_2pc": "All Elemental RES +20%.",
    "bonus_4pc": "Incoming Elemental DMG increases corresponding Elemental RES by 30% for 10s. Can occur once every 10s.",
    "tags": ["defensive", "early_game"],
    },
    "traveling doctor": {
    "bonus_2pc": "Incoming healing +20%.",
    "bonus_4pc": "Using an Elemental Burst restores 20% HP.",
    "tags": ["healing", "early_game"],
    },
    "unfinished reverie": {
    "bonus_2pc": "ATK +18%.",
    "bonus_4pc": "After leaving combat for more than 3s, gain 50% increased DMG dealt for 10s. While burning, this increases by 25%.",
    "tags": ["atk_scaling", "burning", "dps", "fontaine"],
    },
    "vermillion hereafter": {
    "bonus_2pc": "ATK +18%.",
    "bonus_4pc": "After using an Elemental Burst, gain a Nascent Light effect for 16s, increasing ATK by 8% every second. When the wielder loses HP, ATK increases by a further 10% (max 4 stacks).",
    "tags": ["atk_scaling", "burst_focus", "hp_fluctuation", "xiao"],
    },
    "viridescent venerer": {
    "bonus_2pc": "Anemo DMG Bonus +15%.",
    "bonus_4pc": "Swirl DMG increased by 60%. Decreases opponent's Elemental RES to the infused element by 40% for 10s.",
    "tags": ["anemo", "support", "res_shred", "swirl", "em"],
    },
    "vourukasha's glow": {
    "bonus_2pc": "HP +20%.",
    "bonus_4pc": "Elemental Skill and Burst DMG increased by 10%. When the wielder takes DMG, this effect increases by 80% for 5s. Can occur once every 0.1s. Max 5 stacks.",
    "tags": ["hp_scaling", "skill_dmg", "burst_dmg", "dps", "sumeru"],
    },
    "wanderer's troupe": {
    "bonus_2pc": "Elemental Mastery +80.",
    "bonus_4pc": "If the wielder uses a Catalyst or Bow, Charged Attack DMG increases by 35%.",
    "tags": ["em", "charged_atk", "catalyst", "bow"],
    },
}
