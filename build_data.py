"""
Curated build recommendations for CritCal -- best-in-slot / secondary /
niche picks for weapons and artifact sets, plus a short guess at the
team/build archetype each character usually runs, per the July 2026
meta (real-play consensus from Game8, Icy Veins, KQM, and genshin-builds.com,
current as of this write-up -- re-verify periodically since meta shifts
with new weapon/set releases).

This is intentionally a SEPARATE file from weapon_data.py and
characters.py:
  - weapon_data.py already holds weapon_type + the older 2-entry
    recommended_weapons list. We never touch or need to know its
    content -- this file only ADDS new fields on top via characters.py's
    merge step, so nothing here can accidentally wipe out existing
    weapon_data.py entries.
  - characters.py stays focused on scaling/benchmarks/aliases.

Schema per character (all fields optional -- a character missing from
either dict just means scoring.py has less to work with for them, same
fairness guarantee used everywhere else in the app: no data != penalty):

  ARTIFACT_DATA[<key>] = {
      "bis_artifact_set": str,             # single best 4pc set
      "secondary_artifact_set": str,       # single strong alternative 4pc set
      "niche_artifact_sets": [str, ...],   # situational / team-comp-dependent 4pc sets
      "team_archetype": str,               # short guess at the team/build this character usually runs
  }

  WEAPON_TIERS[<key>] = {
      "bis_weapon": str,
      "secondary_weapon": str,
      "f2p_weapon": [str, ...],       # free/cheap, reliably obtainable pick
      "niche_weapon": [str, ..]    # situational pick, or a second f2p option
  }

HOW TO EXPAND THIS FILE (adding a new element or new characters):
  1. Add an entry to ARTIFACT_DATA and one to WEAPON_TIERS below, using
     the character's canonical key from characters.py (run
     normalize_character() on the name if unsure -- lowercase, no
     spaces/apostrophes/hyphens).
  2. Keep every weapon within one character's entry the same weapon
     TYPE (sword/claymore/polearm/bow/catalyst) as that character --
     this is the single easiest mistake to make when filling this in
     quickly (verify against the character's actual weapon type).
  3. Re-run the smoke test at the bottom of scoring.py's test suite
     (or just call rate_build() for the character with a 4pc of their
     bis_artifact_set and their bis_weapon and confirm grade is high)
     to catch typos before committing.
  4. Group new characters under a "# ELEMENT" header comment, matching
     the section layout in characters.py, so the two files stay easy
     to cross-reference.
"""

from typing import Dict, Any, List


ARTIFACT_DATA: Dict[str, Dict[str, Any]] = {

# ==========================================================
# PYRO
# ==========================================================

    "arlecchino": {
        "bis_artifact_set": "Fragment of Harmonic Whimsy",
        "secondary_artifact_set": "Gladiator's Finale",
        "niche_artifact_sets": ["Echoes of an Offering", "Desert Pavilion Chronicle"],
        "team_archetype": "Vaporize / Melt / Mono Pyro / Overload flex, via Bond of Life",
    },
    "bennett": {
        "bis_artifact_set": "Noblesse Oblige",
        "secondary_artifact_set": "Tenacity of the Millelith",
        "niche_artifact_sets": ["Gladiator's Finale"],
        "team_archetype": "near-universal support across National, Vaporize, and Mono comps",
    },
    "chevreuse": {
        "bis_artifact_set": "Tenacity of the Millelith",
        "secondary_artifact_set": "Noblesse Oblige",
        "niche_artifact_sets": ["Vourukasha's Glow"],
        "team_archetype": "pairs with an Electro Sub-DPS in Overloaded comps",
    },
    "dehya": {
        "bis_artifact_set": "Emblem of Severed Fate",
        "secondary_artifact_set": "Crimson Witch of Flames",
        "niche_artifact_sets": ["Flower of Paradise Lost", "Tenacity of the Millelith"],
        "team_archetype": "flexible: Main DPS, Burgeon Sub-DPS, or Shield-adjacent Support",
    },
    "diluc": {
        "bis_artifact_set": "Crimson Witch of Flames",
        "secondary_artifact_set": "Marechaussee Hunter",
        "niche_artifact_sets": ["Gladiator's Finale"],
        "team_archetype": "Mono Pyro / Vaporize / Melt teams",
    },
    "gaming": {
        "bis_artifact_set": "Marechaussee Hunter",
        "secondary_artifact_set": "Crimson Witch of Flames",
        "niche_artifact_sets": ["Flower of Paradise Lost"],
        "team_archetype": "pairs with Xianyun; flexible Vaporize/Melt/Burgeon trigger",
    },
    "hutao": {
        "bis_artifact_set": "Crimson Witch of Flames",
        "secondary_artifact_set": "Shimenawa's Reminiscence",
        "niche_artifact_sets": ["Emblem of Severed Fate"],
        "team_archetype": "National / Hyperbloom hybrid comps",
    },
    "klee": {
        "bis_artifact_set": "Crimson Witch of Flames",
        "secondary_artifact_set": "Shimenawa's Reminiscence",
        "niche_artifact_sets": ["Lavawalker"],
        "team_archetype": "Mono Pyro / Vaporize burst comps",
    },
    "lyney": {
        "bis_artifact_set": "Marechaussee Hunter",
        "secondary_artifact_set": "Vermillion Hereafter",
        "niche_artifact_sets": ["Shimenawa's Reminiscence", "Lavawalker"],
        "team_archetype": "Mono Pyro on-field teams",
    },
    "mavuika": {
        "bis_artifact_set": "Obsidian Codex",
        "secondary_artifact_set": "Scroll of the Hero of Cinder City",
        "niche_artifact_sets": ["Gladiator's Finale"],
        "team_archetype": "Melt (with Citlali) or Overloaded (with Chevreuse/Ororon)",
    },
    "thoma": {
        "bis_artifact_set": "Emblem of Severed Fate",
        "secondary_artifact_set": "Tenacity of the Millelith",
        "niche_artifact_sets": ["Ocean-Hued Clam"],
        "team_archetype": "budget-friendly shield support in most Pyro-adjacent comps",
    },
    "xiangling": {
        "bis_artifact_set": "Emblem of Severed Fate",
        "secondary_artifact_set": "Crimson Witch of Flames",
        "niche_artifact_sets": ["Tenacity of the Millelith"],
        "team_archetype": "National / Vaporize enabler -- near-universal support pick",
    },
    "xinyan": {
        "bis_artifact_set": "Crimson Witch of Flames",
        "secondary_artifact_set": "Pale Flame",
        "niche_artifact_sets": ["Retracing Bolide"],
        "team_archetype": "Mono Pyro or Physical-focused teams",
    },
  "gaming": {
    "bis_artifact_set: "Marechaussee Hunter ",
    "secondary_artifact_set": "Crimson Witch Of Flames",
    "niche_artifact_sets": ["Guilden Dreams"],
    "team_archetype": "Main DPS Vaporize / Melt / Plunge Hyper carry",
  },

# ==========================================================
# HYDRO
# ==========================================================

 "barbra": {
  "bis_artifact_set": "Ocean-Hued Clam",
  "secondary_artifact_set": "Song Of Days Passed", 
  "niche_artifact_set": ["Maiden Beloved"],
  "team_archetype": "Healing Support / Hydro Driver",
},
 "candace": {
  "bis_artifact_set": "Scroll Of The Hero Of Cinder City",
  "secondary_artifact_set": "Noblesse Oblige",
  "niche_artifact_set": ["Emblem Of The Severed Fate"],
  "team_archetype": "Hydro Infusion Support",
},
 "tartaglia": {
  "bis_artifact_set": "Nymph's Dream",
  "secondary_artifact_set": "Heart Of Depth",
  "niche_artifact_set": ["Marechaussee Hunter"],
  "team_archetype": "On-field Hydro DPS",
},
 "furina": {
  "bis_artifact_set": "Golden Troupe",
  "secondary_artifact_set": "Tenacity Of The Millelith",
  "niche_artifact_set": ["None"],
  "team_archetype": "Universal Buffer / Off-field Hydro",
},
 "kokomi": {
  "bis_artifact_set": "Ocean-Hued Clam",
  "secondary_artifact_set": "Tenacity Of The Millelith",
  "niche_artifact_set": ["Song Of Days Passed", "Maiden Beloved"],
  "team_archetype": "Healing Support / Hydro Driver",
},
 "mona": {
  "bis_artifact_set": "Noblesse Oblige",
  "secondary_artifact_set": "Emblem Of Severed Fate",
  "niche_artifact_set": ["Scroll Of The Hero Of Cinder City", "Instructor", "Tenacity Of The Millelith"],
  "team_archetype": "Burst Support / Hydro Buffer",
},
 "mualani": {
  "bis_artifact_set": "Obsidian Codex",
  "secondary_artifact_set": "Heart of Depth",
  "niche_artifact_set": ["Marechaussee Hunter", "Nymph's Dream", "Gilded Dreams"],
  "team_archetype": "Hydro Hypercarry",
},
 "neuvillette": {
   "bis_artifact_set": "Marechaussee Hunter",
   "secondary_artifact_set": "Heart Of Depth",
   "niche_artifact_set": ["Nymph's Dream", "Obsidian Codex", "Wonder's Troupe"],
   "team_archetype": "Charged Attack Hyper-carry",
 },
  "nilou": {
  "bis_artifact_set": "Flower Of Paradies Lost",
  "secondary_artifact_set": "Guilded Dreams",
  "niche_artifact_set": ["Deepwood Memories", "Tenacity Of The Millelith", "Varakusha's Glow"],
  "team_archetype": "Bloom Enabler",
},
 "sigewinne": {
   "bis_artifact_set": "Song of Days Past",
   "secondary_artifact_set": "Ocean-Hued Clam",
   "niche_artifact_set": ["Maiden Beloved", "Emblem of Severed Fate", "Noblesse Oblige"],
   "team_archetype": "Healing Support / Skill Buffer",
},
 "xingquio": {
   "bis_artifact_set": "Emblem of Severed Fate",
   "secondary_artifact_set": "Noblesse Oblige",
   "niche_artifact_set": ["Heart of Depth", "Nymph's Dream", "Gilded Dreams"],
},
 "yelan": {
   "bis_artifact_set": "Emblem of Severed Fate",
   "secondary_artifact_set": "Noblesse Oblige",
   "niche_artifact_set": ["Golden Troupe", "Heart of Depth", "Nymph's Dream"],
},
} 

WEAPON_TIERS: Dict[str, Dict[str, str]] = {

# ==========================================================
# PYRO
# ==========================================================

    "arlecchino": {
        "bis_weapon": "Crimson Moon's Semblance",
        "secondary_weapon": "Staff of Homa",
        "f2p_weapon": ["White Tassel"],
        "niche_weapon": ["Deathmatch"],
    },
    "bennett": {
        "bis_weapon": "Aquila Favonia",
        "secondary_weapon": "Sacrificial Sword",
        "f2p_weapon": ["Favonius Sword"],
        "niche_weapon": ["Iron Sting"],
    },
    "chevreuse": {
        "bis_weapon": "Black Tassel",
        "secondary_weapon": "Favonius Lance",
        "f2p_weapon": ["Black Tassel"],
        "niche_weapon": ["Song of Days Past"],
    },
    "dehya": {
        "bis_weapon": "Beacon of the Reed Sea",
        "secondary_weapon": "Serpent Spine",
        "f2p_weapon": ["Prototype Archaic"],
        "niche_weapon": ["Mailed Flower"],
    },
    "diluc": {
        "bis_weapon": "Wolf's Gravestone",
        "secondary_weapon": "Serpent Spine",
        "f2p_weapon": ["Prototype Archaic"],
        "niche_weapon": ["Redhorn Stonethresher"],
    },
    "gaming": {
        "bis_weapon": "Fruitful Hook",
        "secondary_weapon": "Serpent Spine",
        "f2p_weapon": ["Prototype Archaic"],
        "niche_weapon": ["Mailed Flower"],
    },
    "hutao": {
        "bis_weapon": "Staff of Homa",
        "secondary_weapon": "Dragon's Bane",
        "f2p_weapon": ["White Tassel"],
        "niche_weapon": ["Deathmatch"],
    },
    "klee": {
        "bis_weapon": "Lost Prayer to the Sacred Winds",
        "secondary_weapon": "Dodoco Tales",
        "f2p_weapon": ["Prototype Amber"],
        "niche_weapon": ["Solar Pearl"],
    },
    "lyney": {
        "bis_weapon": "The First Great Magic",
        "secondary_weapon": "Aqua Simulacra",
        "f2p_weapon": ["Prototype Crescent"],
        "niche_weapon": ["Song of Stillness"],
    },
    "mavuika": {
        "bis_weapon": "A Thousand Blazing Suns",
        "secondary_weapon": "Serpent Spine",
        "f2p_weapon": ["Mailed Flower"],
        "niche_weapon": ["Tidal Shadows"],
    },
    "thoma": {
        "bis_weapon": "The Catch",
        "secondary_weapon": "Favonius Lance",
        "f2p_weapon": ["Black Tassel"],
        "niche_weapon": ["Dragon's Bane"],
    },
    "xiangling": {
        "bis_weapon": "Staff of Homa",
        "secondary_weapon": "Deathmatch",
        "f2p_weapon": ["Dragon's Bane"],
        "niche_weapon": ["Favonius Lance"],
    },
    "xinyan": {
        "bis_weapon": "Song of Broken Pines",
        "secondary_weapon": "Rainslasher",
        "f2p_weapon": ["Debate Club"],
        "niche_weapon": ["Whiteblind"],
    },
    "gaming": {
        "bis_weapon": "Fang Of The Mountain King",
        "secondary_weapon": "Serpent's Spine",
        "f2p_weapon": ["Dragons Bane"],
        "niche_weapon": ["White Tassel"],
    },
# ==========================================================
# HYDRO
# ==========================================================

 "barbra": {
    "bis_weapon": "Thrilling Tales Of Dragon Slayers",
    "secondary_weapon": "Prototype Amber",
    "f2p_weapon": ["Favonius Codex"],
    "niche_weapon": ["Favonius Codex"],
},
 "candice": {
    "bis_weapon": "Favonius Lance",
    "secondary_weapon": "Dialouge Of The Desert Sages",
    "f2p_weapon": ["Rightful Reward"],
    "niche_weapon": ["Rightful Reward"],
},
 "tartaglia": {
    "bis_weapon": "Polar Star",
    "secondary_weapon": "Aqua Simularca",
    "f2p_weapon": ["The Viridiscent Hunt"],
    "niche_weapon":  ["Hamoyumi"],
},
 "furina": {
    "bis_weapon": "Splendor of Tranquil Waters",
    "secondary_weapon": "Primodial Jade Cutter",
    "f2p_weapon": ["Festering Desire", "Favonius Sword", "Fleuve Cendre Ferryman"],
    "niche_weapon": ["Wolf-Fang", "Key Of Khaj-Nisut",],
 },
  "kokomi": {
     "bis_weapon": "Everlasting Moonglow",
     "secondary_weapon": "Prototype Amber",
     "f2p_weapon": ["Thrilling Tales of Dragon Slayers", "Favonius Codex"],
     "niche_weapon": ["Hokushin Ring", "Favonius Codex"],
},
 "mona": {
    "bis_weapon": "A Thousand Floating Dreams",
    "secondary_weapon": "Skyward Atlas",
    "f2p_weapon": ["Protype Amber", "Favonius Codex", "The widsith", "Thrilling Tales of Dragon Slayers"],
    "niche_weapon": ["None"]
},
 "mualani": {
    "bis_weapon": "Surf's Up",
    "secondary_weapon": "Tome Of The Enternal Flow",
    "niche_weapon": ["Cashflow Supervision", "Lost Prayer to the Sacred Winds", "Sacrifical Jade"],
    "f2p_weapon: ["Ring of Yaxche", "Prototype Amber"],
},
 "neuvillette": {
 "bis_weapon": "Tome of the Eternal Flow",
 "secondary_weapon": "Sacrificial Jade",
 "niche_weapon": ["Cashflow Supervision", "Lost Prayer to the Sacred Winds", "Jadefall's Splendor"],
 "f2p_weapon": ["Prototype Amber", "Ring of Yaxche"],
},
 "nilou": {
 "bis_weapon": "Key of Khaj-Nisut",
 "secondary_weapon": "Freedom-Sworm",
 "niche_weapon": ["Xiphos' Moonlight", "Primodial Jade Cutter", "Favonius Sword"],
 "f2p_weapon": ["Iron Sting", "Sapwood Blade"],
},
 "sigewinne": {
 "bis_weapon": "Silvershower Heartstrings",
 "secondary_weapon": "Sequence of Solitude",
 "niche_weapon": ["Aqua Simularca", "Favonius Warbow", "Elegy for the End"],
 "f2p_weapon": ["Recurve Bow", "Messenger"],
}, 
 "xingquio": {
 "bis_weapon": "Mistsplitter Reforged",
 "secondary_weapon": "Sacrificial Sword",
 "niche_weapon": ["Light of Foilar Incision", "Summit Shaper", "Haran Geppaku Futsu"],
 "f2p_weapon": ["Sacrificial Sword", "Favonius Sword", "Fleuve Cendre Ferryman"],
},
 "yelan": {
 "bis_weapon": "Aqua Simularca",
 "secondary_weapon": "Elgy for the End",
 "niche_weapon": ["Silvershower Heartstring", "Hunter's Path", "Mauun's Moon"],
 "f2p_weapon": ["Favonius Warbow", "Fading Twilight", "Slingshot"],
}, 
}
    
    
