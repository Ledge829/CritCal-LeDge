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
      "niche_artifact_sets": [str, ...],   # situational / team-comp-dependent 4pc sets (can be empty [])
      "team_archetype": str,               # short guess at the team/build this character usually runs
  }

  WEAPON_TIERS[<key>] = {
      "bis_weapon": str,
      "secondary_weapon": str,
      "f2p_weapon": [str, ...],    # free/cheap, reliably obtainable picks (can be empty [])
      "niche_weapon": [str, ...],  # situational picks, or extra f2p options (can be empty [])
  }

IMPORTANT: the "<key>" used in both dicts MUST be the character's
CANONICAL key from characters.py's CHARACTER_CONFIGS -- not an alias.
"tartaglia" or "raidenshogun" will NOT reach Childe/Raiden; use
"childe"/"raiden". If unsure, run normalize_character() on the name and
cross-check CHARACTER_ALIASES in characters.py.

HOW TO EXPAND THIS FILE (adding a new element or new characters):
  1. Add an entry to ARTIFACT_DATA and one to WEAPON_TIERS below, using
     the character's canonical key (see IMPORTANT note above).
  2. Keep every weapon within one character's entry the same weapon
     TYPE (sword/claymore/polearm/bow/catalyst) as that character --
     this is the single easiest mistake to make when filling this in
     quickly (verify against the character's actual weapon type).
  3. Call rate_build() for the character with a 4pc of their
     bis_artifact_set and their bis_weapon and confirm weapon_tier /
     artifact_tier both come back "BiS" -- this catches key typos and
     name mismatches immediately.
  4. Group new characters under a "# ELEMENT" header comment, in the
     same order characters.py lists them, so the two files stay easy
     to cross-reference.
  5. Keep formatting uniform: 4-space indent, one blank line between
     character blocks, Title Case item names (lowercase "of"/"the").
"""

from typing import Dict, Any, List


ARTIFACT_DATA: Dict[str, Dict[str, Any]] = {

# ==========================================================
# PYRO
# ==========================================================

    "arlecchino": {
    "bis_artifact_set": "Fragment of Harmonic Whimsy",
    "secondary_artifact_set": "Gladiator's Finale",
    "niche_artifact_sets": ["Echoes of an Offering", "Marechaussee Hunter", "Vermillion Hereafter", "Nighttime Whispers in the Echoing Woods", "Retracing Bolide"],
    "team_archetype": "Vaporize / Melt / Mono Pyro / Overload flex, via Bond of Life",
    },
    "bennett": {
    "bis_artifact_set": "Noblesse Oblige",
    "secondary_artifact_set": "Scroll of the Hero of Cinder City",
    "niche_artifact_sets": ["Instructor's", "Song of Days Past", "Maiden Beloved", "Ocean-Hued Clam", "Deepwood Memories", "Tenacity of the Millelith"],
    "team_archetype": "Universal ATK Buffer / Healer / Battery",
    },
    "chevreuse": {
    "bis_artifact_set": "Scroll of the Hero of Cinder City",
    "secondary_artifact_set": "Noblesse Oblige",
    "niche_artifact_sets": ["Song of Days Past", "Ocean-Hued Clam", "Maiden Beloved", "Tenacity of the Millelith", "Emblem of Severed Fate"],
    "team_archetype": "Overload Support / ATK Buffer / Healer",
    },
    "dehya": {
    "bis_artifact_set": "Emblem of Severed Fate",
    "secondary_artifact_set": "Vourukasha's Glow",
    "niche_artifact_sets": ["Tenacity of the Millelith", "Golden Troupe", "Crimson Witch of Flames", "Gilded Dreams", "Flower of Paradise Lost", "Deepwood Memories"],
    "team_archetype": "Burst DPS / Off-Field Pyro / Burgeon / Burn-Melt Support",
    },
    "diluc": {
    "bis_artifact_set": "Crimson Witch of Flames",
    "secondary_artifact_set": "Marechaussee Hunter",
    "niche_artifact_sets": ["Gilded Dreams", "Gladiator's Finale", "Lavawalker", "Shimenawa's Reminiscence", "Echoes of an Offering"],
    "team_archetype": "Vaporize / Melt / Mono Pyro / Plunging DPS",
    },
    "gaming": {
    "bis_artifact_set": "Marechaussee Hunter",
    "secondary_artifact_set": "Crimson Witch of Flames",
    "niche_artifact_sets": ["Shimenawa's Reminiscence", "Gilded Dreams", "Gladiator's Finale", "Lavawalker", "Echoes of an Offering"],
    "team_archetype": "Vaporize / Melt / Plunging Hypercarry / Mono Pyro",
    },
    "hutao": {
    "bis_artifact_set": "Crimson Witch of Flames",
    "secondary_artifact_set": "Shimenawa's Reminiscence",
    "niche_artifact_sets": ["Gilded Dreams", "Marechaussee Hunter", "Lavawalker", "Gladiator's Finale", "Wanderer's Troupe"],
    "team_archetype": "Vaporize / Double Hydro / Melt / Burgeon",
    },
    "klee": {
    "bis_artifact_set": "Crimson Witch of Flames",
    "secondary_artifact_set": "Marechaussee Hunter",
    "niche_artifact_sets": ["Lavawalker", "Gilded Dreams", "Shimenawa's Reminiscence", "Wanderer's Troupe", "Echoes of an Offering"],
    "team_archetype": "Vaporize / Mono Pyro / Burgeon Driver / Charged Attack DPS",
    },
    "lyney": {
    "bis_artifact_set": "Marechaussee Hunter",
    "secondary_artifact_set": "Lavawalker",
    "niche_artifact_sets": ["Vermillion Hereafter", "Shimenawa's Reminiscence", "Echoes of an Offering", "Gladiator's Finale", "Crimson Witch of Flames"],
    "team_archetype": "Mono Pyro / Charged Attack Hypercarry",
    },
    "mavuika": {
    "bis_artifact_set": "Obsidian Codex",
    "secondary_artifact_set": "Scroll of the Hero of Cinder City",
    "niche_artifact_sets": ["Crimson Witch of Flames", "Gilded Dreams", "Marechaussee Hunter", "Unfinished Reverie", "Golden Troupe", "Gladiator's Finale"],
    "team_archetype": "Hypercarry / Vaporize / Melt / Mono Pyro / Off-Field Pyro",
    },
    "thoma": {
    "bis_artifact_set": "Flower of Paradise Lost",
    "secondary_artifact_set": "Gilded Dreams",
    "niche_artifact_sets": ["Deepwood Memories", "Noblesse Oblige", "Tenacity of the Millelith", "Instructor's", "2pc HP% + 2pc Emblem of Severed Fate", "Scroll of the Hero of Cinder City"],
    "team_archetype": "Burgeon Trigger / Shield Support / Burning Support",
    },
    "xiangling": {
    "bis_artifact_set": "Emblem of Severed Fate",
    "secondary_artifact_set": "Crimson Witch of Flames",
    "niche_artifact_sets": ["Scroll of the Hero of Cinder City", "Gilded Dreams", "Lavawalker", "Instructor's", "Noblesse Oblige", "Unfinished Reverie"],
    "team_archetype": "Off-Field Pyro DPS / Vaporize / Melt / Mono Pyro / Overload",
    },
    "xinyan": {
    "bis_artifact_set": "Pale Flame",
    "secondary_artifact_set": "Bloodstained Chivalry",
    "niche_artifact_sets": ["Gladiator's Finale", "Emblem of Severed Fate", "Tenacity of the Millelith", "Noblesse Oblige", "Crimson Witch of Flames", "Scroll of the Hero of Cinder City"],
    "team_archetype": "Physical DPS / Burst DPS / Shield Support",
    },

# ==========================================================
# HYDRO
# ==========================================================

    "barbara": {
    "bis_artifact_set": "Ocean-Hued Clam",
    "secondary_artifact_set": "Song of Days Past",
    "niche_artifact_sets": ["Maiden Beloved", "Tenacity of the Millelith", "Instructor's", "Deepwood Memories", "Noblesse Oblige"],
    "team_archetype": "Healer / Bloom Driver / Hydro Support",
    },
    "candace": {
    "bis_artifact_set": "Scroll of the Hero of Cinder City",
    "secondary_artifact_set": "Noblesse Oblige",
    "niche_artifact_sets": ["Emblem of Severed Fate", "Tenacity of the Millelith", "Instructor's", "Scroll of the Hero of Cinder City", "Vourukasha's Glow"],
    "team_archetype": "Hydro Infusion Support / Normal Attack Buffer / Bloom Support",
    },
    "childe": {
    "bis_artifact_set": "Nymph's Dream",
    "secondary_artifact_set": "Heart of Depth",
    "niche_artifact_sets": ["Marechaussee Hunter", "Echoes of an Offering", "Shimenawa's Reminiscence", "Gladiator's Finale", "Desert Pavilion Chronicle"],
    "team_archetype": "On-Field Hydro DPS / Vaporize / International / Electro-Charged",
    },
    "furina": {
    "bis_artifact_set": "Golden Troupe",
    "secondary_artifact_set": "Tenacity of the Millelith",
    "niche_artifact_sets": ["Marechaussee Hunter", "Heart of Depth", "Nymph's Dream", "Vourukasha's Glow", "Noblesse Oblige", "2pc HP% + 2pc Golden Troupe"],
    "team_archetype": "Off-Field Hydro DPS / Universal Buffer / Double Hydro / Hypercarry Support",
    },
    "kokomi": {
    "bis_artifact_set": "Ocean-Hued Clam",
    "secondary_artifact_set": "Tenacity of the Millelith",
    "niche_artifact_sets": ["Song of Days Past", "Deepwood Memories", "Instructor's", "Maiden Beloved", "Heart of Depth", "Nymph's Dream"],
    "team_archetype": "Healer / Bloom Driver / Freeze Support / Mono Hydro Driver",
    },
    "mona": {
    "bis_artifact_set": "Emblem of Severed Fate",
    "secondary_artifact_set": "Noblesse Oblige",
    "niche_artifact_sets": ["Golden Troupe", "Heart of Depth", "Nymph's Dream", "Instructor's", "Scroll of the Hero of Cinder City", "Tenacity of the Millelith"],
    "team_archetype": "Burst Support / Freeze Support / Vaporize Support / Hydro DPS",
    },
    "mualani": {
    "bis_artifact_set": "Obsidian Codex",
    "secondary_artifact_set": "Heart of Depth",
    "niche_artifact_sets": ["Marechaussee Hunter", "Nymph's Dream", "Golden Troupe", "Wanderer's Troupe", "Gilded Dreams", "Scroll of the Hero of Cinder City"],
    "team_archetype": "Vaporize Hypercarry / Forward Vape / Mono Hydro",
    },
    "neuvillette": {
    "bis_artifact_set": "Marechaussee Hunter",
    "secondary_artifact_set": "Heart of Depth",
    "niche_artifact_sets": ["Nymph's Dream", "Golden Troupe", "Wanderer's Troupe", "Blizzard Strayer", "Obsidian Codex", "Scroll of the Hero of Cinder City"],
    "team_archetype": "Charged Attack Hypercarry / Hyperbloom Driver / Mono Hydro",
    },
    "nilou": {
    "bis_artifact_set": "Flower of Paradise Lost",
    "secondary_artifact_set": "Vourukasha's Glow",
    "niche_artifact_sets": ["Gilded Dreams", "Tenacity of the Millelith", "Deepwood Memories", "Heart of Depth", "Nymph's Dream", "Instructor's"],
    "team_archetype": "Bloom Enabler / Super Bloom / HP Support",
    },
    "sigewinne": {
    "bis_artifact_set": "Song of Days Past",
    "secondary_artifact_set": "Ocean-Hued Clam",
    "niche_artifact_sets": ["Tenacity of the Millelith", "Maiden Beloved", "Noblesse Oblige", "Golden Troupe", "Vourukasha's Glow", "Heart of Depth"],
    "team_archetype": "Healer / Off-Field Hydro Support / Furina Support",
    },
    "xingqiu": {
    "bis_artifact_set": "Emblem of Severed Fate",
    "secondary_artifact_set": "Noblesse Oblige",
    "niche_artifact_sets": ["Heart of Depth", "Nymph's Dream", "Golden Troupe", "Scroll of the Hero of Cinder City", "Instructor's", "Tenacity of the Millelith"],
    "team_archetype": "Off-Field Hydro DPS / Vaporize / Hyperbloom / Bloom / Electro-Charged / Freeze",
    },
    "yelan": {
    "bis_artifact_set": "Emblem of Severed Fate",
    "secondary_artifact_set": "Noblesse Oblige",
    "niche_artifact_sets": ["Heart of Depth", "Nymph's Dream", "Tenacity of the Millelith", "Golden Troupe", "Scroll of the Hero of Cinder City", "Vourukasha's Glow"],
    "team_archetype": "Off-Field Hydro DPS / Double Hydro / Vaporize / Hyperbloom / Mono Hydro",
    },

# ==========================================================
# ANEMO
# ==========================================================

    "chasca": {
    "bis_artifact_set": "Obsidian Codex",
    "secondary_artifact_set": "Viridescent Venerer",
    "niche_artifact_sets": ["Marechaussee Hunter", "Desert Pavilion Chronicle", "Scroll of the Hero of Cinder City", "Golden Troupe", "Shimenawa's Reminiscence", "Echoes of an Offering"],
    "team_archetype": "Reaction Hypercarry / Swirl DPS / Multi-Element DPS",
    },
    "faruzan": {
    "bis_artifact_set": "Scroll of the Hero of Cinder City",
    "secondary_artifact_set": "Noblesse Oblige",
    "niche_artifact_sets": ["Viridescent Venerer", "Emblem of Severed Fate", "Tenacity of the Millelith", "Instructor's", "The Exile", "Scroll of the Hero of Cinder City"],
    "team_archetype": "Anemo Buffer / Battery / Crowd Control Support",
    },
    "heizou": {
    "bis_artifact_set": "Viridescent Venerer",
    "secondary_artifact_set": "Desert Pavilion Chronicle",
    "niche_artifact_sets": ["Marechaussee Hunter", "Golden Troupe", "Wanderer's Troupe", "Gilded Dreams", "Shimenawa's Reminiscence", "Echoes of an Offering"],
    "team_archetype": "On-Field Anemo DPS / Swirl Driver / Quickswap DPS",
    },
    "jean": {
    "bis_artifact_set": "Viridescent Venerer",
    "secondary_artifact_set": "Noblesse Oblige",
    "niche_artifact_sets": ["Song of Days Past", "Ocean-Hued Clam", "Gladiator's Finale", "Marechaussee Hunter", "Scroll of the Hero of Cinder City", "Tenacity of the Millelith"],
    "team_archetype": "Healer / Swirl Support / Sunfire / Anemo DPS",
    },
    "kazuha": {
    "bis_artifact_set": "Viridescent Venerer",
    "secondary_artifact_set": "Scroll of the Hero of Cinder City",
    "niche_artifact_sets": ["Noblesse Oblige", "Instructor's", "Gilded Dreams", "Flower of Paradise Lost", "Emblem of Severed Fate", "Tenacity of the Millelith"],
    "team_archetype": "Swirl Support / Elemental DMG Buffer / Crowd Control / Quickswap",
    },
    "lanyan": {
    "bis_artifact_set": "Viridescent Venerer",
    "secondary_artifact_set": "Scroll of the Hero of Cinder City",
    "niche_artifact_sets": ["Noblesse Oblige", "Tenacity of the Millelith", "Instructor's", "Song of Days Past", "Ocean-Hued Clam", "Maiden Beloved"],
    "team_archetype": "Anemo Shielder / Swirl Support / Crowd Control",
    },
    "lynette": {
    "bis_artifact_set": "Viridescent Venerer",
    "secondary_artifact_set": "Golden Troupe",
    "niche_artifact_sets": ["Noblesse Oblige", "Emblem of Severed Fate", "Scroll of the Hero of Cinder City", "Marechaussee Hunter", "Gladiator's Finale", "Tenacity of the Millelith"],
    "team_archetype": "Off-Field Anemo DPS / Swirl Support / Quickswap",
    },
    "sayu": {
    "bis_artifact_set": "Viridescent Venerer",
    "secondary_artifact_set": "Scroll of the Hero of Cinder City",
    "niche_artifact_sets": ["Ocean-Hued Clam", "Song of Days Past", "Noblesse Oblige", "Instructor's", "Maiden Beloved", "Emblem of Severed Fate"],
    "team_archetype": "Healer / Swirl Support / Exploration / Reaction Driver",
    },
    "sucrose": {
    "bis_artifact_set": "Viridescent Venerer",
    "secondary_artifact_set": "Scroll of the Hero of Cinder City",
    "niche_artifact_sets": ["Instructor's", "Gilded Dreams", "Flower of Paradise Lost", "Noblesse Oblige", "Golden Troupe", "Deepwood Memories"],
    "team_archetype": "Swirl Support / EM Buffer / Reaction Driver / Crowd Control",
    },
    "venti": {
    "bis_artifact_set": "Viridescent Venerer",
    "secondary_artifact_set": "Scroll of the Hero of Cinder City",
    "niche_artifact_sets": ["Noblesse Oblige", "Emblem of Severed Fate", "Golden Troupe", "Gilded Dreams", "Instructor's", "Flower of Paradise Lost"],
    "team_archetype": "Crowd Control / Swirl Support / Energy Battery / Off-Field DPS",
    },
    "wanderer": {
    "bis_artifact_set": "Desert Pavilion Chronicle",
    "secondary_artifact_set": "Marechaussee Hunter",
    "niche_artifact_sets": ["Shimenawa's Reminiscence", "Echoes of an Offering", "Viridescent Venerer", "Wanderer's Troupe", "Obsidian Codex", "Golden Troupe"],
    "team_archetype": "Hypercarry / Normal Attack DPS / Charged Attack DPS / Swirl Driver",
    },
    "xiao": {
    "bis_artifact_set": "Vermillion Hereafter",
    "secondary_artifact_set": "Marechaussee Hunter",
    "niche_artifact_sets": ["Desert Pavilion Chronicle", "Echoes of an Offering", "Gladiator's Finale", "Shimenawa's Reminiscence", "Viridescent Venerer", "Obsidian Codex"],
    "team_archetype": "Hypercarry / Plunging DPS / Anemo Main DPS",
    },
    "xianyun": {
    "bis_artifact_set": "Viridescent Venerer",
    "secondary_artifact_set": "Song of Days Past",
    "niche_artifact_sets": ["Scroll of the Hero of Cinder City", "Noblesse Oblige", "Ocean-Hued Clam", "Maiden Beloved", "Golden Troupe", "Tenacity of the Millelith"],
    "team_archetype": "Plunging Support / Healer / Swirl Support / Crowd Control",
    },
# ==========================================================
# ELECTRO
# ==========================================================
    "beidou": {
    "bis_artifact_set": "Emblem of Severed Fate",
    "secondary_artifact_set": "Thundering Fury",
    "niche_artifact_sets": ["Noblesse Oblige", "Golden Troupe", "Gladiator's Finale", "Gilded Dreams", "Scroll of the Hero of Cinder City", "Thundersoother"],
    "team_archetype": "Off-Field Electro DPS / Electro-Charged / Aggravate / Overload",
    },
     "cyno": {
    "bis_artifact_set": "Thundering Fury",
    "secondary_artifact_set": "Fragment of Harmonic Whimsy",
    "niche_artifact_sets": ["Gilded Dreams", "Gladiator's Finale", "Flower of Paradise Lost", "Scroll of the Hero of Cinder City", "Thundersoother", "Obsidian Codex"],
    "team_archetype": "Aggravate Hypercarry / Hyperbloom / Electro-Charged / Stellar-Conduct",
    },
     "clorinde": {
    "bis_artifact_set": "Fragment of Harmonic Whimsy",
    "secondary_artifact_set": "Thundering Fury",
    "niche_artifact_sets": ["Gladiator's Finale", "Marechaussee Hunter", "Echoes of an Offering", "Golden Troupe", "Shimenawa's Reminiscence", "Obsidian Codex"],
    "team_archetype": "Aggravate Hypercarry / Electro-Charged / Overload / Quickswap",
    },
     "dori": {
    "bis_artifact_set": "Scroll of the Hero of Cinder City",
    "secondary_artifact_set": "Ocean-Hued Clam",
    "niche_artifact_sets": ["Noblesse Oblige", "Song of Days Past", "Instructor's", "Tenacity of the Millelith", "Gilded Dreams", "Maiden Beloved"],
    "team_archetype": "Healer / Energy Battery / Electro Support / Hyperbloom",
    },
     "fischl": {
    "bis_artifact_set": "Golden Troupe",
    "secondary_artifact_set": "Thundering Fury",
    "niche_artifact_sets": ["Gilded Dreams", "Thundersoother", "Scroll of the Hero of Cinder City", "Emblem of Severed Fate", "Gladiator's Finale", "Noblesse Oblige"],
    "team_archetype": "Off-Field Electro DPS / Aggravate / Electro-Charged / Overload",
    },
     "iansan": {
    "bis_artifact_set": "Scroll of the Hero of Cinder City",
    "secondary_artifact_set": "Noblesse Oblige",
    "niche_artifact_sets": ["Tenacity of the Millelith", "Emblem of Severed Fate", "Thundering Fury", "Instructor's", "Golden Troupe", "Gilded Dreams"],
    "team_archetype": "Electro Support / ATK Buffer / Quickswap / Overload",
    },
     "keqing": {
    "bis_artifact_set": "Thundering Fury",
    "secondary_artifact_set": "Fragment of Harmonic Whimsy",
    "niche_artifact_sets": ["Thundersoother", "Golden Troupe", "Gladiator's Finale", "Gilded Dreams", "Scroll of the Hero of Cinder City", "Shimenawa's Reminiscence"],
    "team_archetype": "Aggravate Hypercarry / Electro-Charged / Overload / Quickswap",
    },
     "kukishinobu": {
    "bis_artifact_set": "Flower of Paradise Lost",
    "secondary_artifact_set": "Gilded Dreams",
    "niche_artifact_sets": ["Tenacity of the Millelith", "Scroll of the Hero of Cinder City", "Deepwood Memories", "Instructor's", "Golden Troupe", "Thundering Fury"],
    "team_archetype": "Hyperbloom Trigger / Healer / Aggravate Support / Electro-Charged",
    },
     "sara": {
    "bis_artifact_set": "Noblesse Oblige",
    "secondary_artifact_set": "Scroll of the Hero of Cinder City",
    "niche_artifact_sets": ["Emblem of Severed Fate", "Tenacity of the Millelith", "Golden Troupe", "Instructor's", "Thundering Fury", "The Exile"],
    "team_archetype": "Electro Buffer / Burst Support / Raiden Support / Quickswap",
    },
     "lisa": {
    "bis_artifact_set": "Thundering Fury",
    "secondary_artifact_set": "Golden Troupe",
    "niche_artifact_sets": ["Gilded Dreams", "Emblem of Severed Fate", "Scroll of the Hero of Cinder City", "Thundersoother", "Wanderer's Troupe", "Noblesse Oblige"],
    "team_archetype": "Aggravate DPS / Electro Support / Hyperbloom Driver / Electro-Charged",
    },
     "ororon": {
    "bis_artifact_set": "Scroll of the Hero of Cinder City",
    "secondary_artifact_set": "Golden Troupe",
    "niche_artifact_sets": ["Thundering Fury", "Noblesse Oblige", "Emblem of Severed Fate", "Gilded Dreams", "Thundersoother", "Instructor's"],
    "team_archetype": "Off-Field Electro DPS / Electro-Charged Support / Nightsoul Support",
    },
     "raiden": {
    "bis_artifact_set": "Emblem of Severed Fate",
    "secondary_artifact_set": "Scroll of the Hero of Cinder City",
    "niche_artifact_sets": ["Thundering Fury", "Gilded Dreams", "Flower of Paradise Lost", "Noblesse Oblige", "Thundersoother", "Golden Troupe"],
    "team_archetype": "Hypercarry / Burst DPS / Hyperbloom Trigger / Electro-Charged / Overload",
    },
     "razor": {
    "bis_artifact_set": "Pale Flame",
    "secondary_artifact_set": "Thundering Fury",
    "niche_artifact_sets": ["Gladiator's Finale", "Thundersoother", "Gilded Dreams", "Golden Troupe", "Bloodstained Chivalry", "Scroll of the Hero of Cinder City"],
    "team_archetype": "Physical Hypercarry / Aggravate / Electro DPS",
    },
     "sethos": {
    "bis_artifact_set": "Wanderer's Troupe",
    "secondary_artifact_set": "Thundering Fury",
    "niche_artifact_sets": ["Gilded Dreams", "Golden Troupe", "Thundersoother", "Scroll of the Hero of Cinder City", "Shimenawa's Reminiscence", "Obsidian Codex"],
    "team_archetype": "Charged Shot DPS / Aggravate / Electro Hypercarry",
    },
     "yaemiko": {
    "bis_artifact_set": "Golden Troupe",
    "secondary_artifact_set": "Gilded Dreams",
    "niche_artifact_sets": ["Thundering Fury", "Emblem of Severed Fate", "Thundersoother", "Scroll of the Hero of Cinder City", "Flower of Paradise Lost", "Noblesse Oblige"],
    "team_archetype": "Off-Field Electro DPS / Aggravate / Electro-Charged / Quickswap",
    },
# ==========================================================
# DENDRO
# ==========================================================
     "alhaitham": {
    "bis_artifact_set": "Gilded Dreams",
    "secondary_artifact_set": "Deepwood Memories",
    "niche_artifact_sets": ["Golden Troupe", "Flower of Paradise Lost", "Wanderer's Troupe", "Gladiator's Finale", "Shimenawa's Reminiscence", "Obsidian Codex"],
    "team_archetype": "Spread Hypercarry / Quicken DPS / Hyperbloom Driver",
    },
     "baizhu": {
    "bis_artifact_set": "Deepwood Memories",
    "secondary_artifact_set": "Scroll of the Hero of Cinder City",
    "niche_artifact_sets": ["Ocean-Hued Clam", "Song of Days Past", "Noblesse Oblige", "Tenacity of the Millelith", "Instructor's", "Maiden Beloved"],
    "team_archetype": "Healer / Dendro Support / Bloom Support / Quicken Support",
    },
     "collei": {
    "bis_artifact_set": "Deepwood Memories",
    "secondary_artifact_set": "Scroll of the Hero of Cinder City",
    "niche_artifact_sets": ["Noblesse Oblige", "Instructor's", "Emblem of Severed Fate", "Golden Troupe", "Gilded Dreams", "The Exile"],
    "team_archetype": "Off-Field Dendro Support / Bloom / Hyperbloom / Burgeon / Quicken",
    },
     "emilie": {
    "bis_artifact_set": "Unfinished Reverie",
    "secondary_artifact_set": "Deepwood Memories",
    "niche_artifact_sets": ["Golden Troupe", "Scroll of the Hero of Cinder City", "Gilded Dreams", "Noblesse Oblige", "Emblem of Severed Fate", "Flower of Paradise Lost"],
    "team_archetype": "Burning DPS / Off-Field Dendro DPS / Burning Support",
    },
     "kaveh": {
    "bis_artifact_set": "Flower of Paradise Lost",
    "secondary_artifact_set": "Deepwood Memories",
    "niche_artifact_sets": ["Gilded Dreams", "Instructor's", "Ocean-Hued Clam", "Scroll of the Hero of Cinder City", "Emblem of Severed Fate", "Maiden Beloved"],
    "team_archetype": "Bloom Driver / Burgeon / Hyperbloom / Dendro DPS",
    },
     "kinich": {
    "bis_artifact_set": "Obsidian Codex",
    "secondary_artifact_set": "Unfinished Reverie",
    "niche_artifact_sets": ["Deepwood Memories", "Golden Troupe", "Scroll of the Hero of Cinder City", "Gilded Dreams", "Gladiator's Finale", "Shimenawa's Reminiscence"],
    "team_archetype": "Burning Hypercarry / Burgeon DPS / Nightsoul DPS",
    },
     "nahida": {
    "bis_artifact_set": "Deepwood Memories",
    "secondary_artifact_set": "Gilded Dreams",
    "niche_artifact_sets": ["Golden Troupe", "Flower of Paradise Lost", "Scroll of the Hero of Cinder City", "Instructor's", "Wanderer's Troupe", "Emblem of Severed Fate"],
    "team_archetype": "Off-Field Dendro DPS / Quicken Support / Hyperbloom / Bloom / Burgeon",
    },
     "tighnari": {
    "bis_artifact_set": "Wanderer's Troupe",
    "secondary_artifact_set": "Gilded Dreams",
    "niche_artifact_sets": ["Deepwood Memories", "Golden Troupe", "Scroll of the Hero of Cinder City", "Shimenawa's Reminiscence", "Thundering Fury", "Obsidian Codex"],
    "team_archetype": "Spread Hypercarry / Charged Shot DPS / Quicken",
    },
     "yaoyao": {
    "bis_artifact_set": "Deepwood Memories",
    "secondary_artifact_set": "Scroll of the Hero of Cinder City",
    "niche_artifact_sets": ["Tenacity of the Millelith", "Instructor's", "Song of Days Past", "Ocean-Hued Clam", "Noblesse Oblige", "Maiden Beloved"],
    "team_archetype": "Healer / Dendro Support / Bloom / Hyperbloom / Burgeon / Quicken",
    },
     "nefer": {
       "bis_artifact_set": "Night of the Sky's Unveiling",
       "secondary_artifact_set": "Silken Moon's Serenade",
       "niche_artifact_sets": ["Deepwood Memories", "Gilded Dreams", "Flowers of Paradise Lost", "Wanderer's Troupe", "Paradise Lost", "Golden Troupe", "Instructor", "Noblesse Oblige", "Tenacity of the Millelith", "Scroll of the Hero of Cinder City", "Obsidian Codex", "Emblem of Severed Fate"],
       "team_archetype": "Lunar Bloom Hypercarry / Dendro Hypercarry / On-Field DPS",
    },
     
     
# ==========================================================
# CRYO
# ==========================================================
    "ayaka": {
    "bis_artifact_set": "Blizzard Strayer",
    "secondary_artifact_set": "Marechaussee Hunter",
    "niche_artifact_sets": ["Golden Troupe", "Gladiator's Finale", "Shimenawa's Reminiscence", "Echoes of an Offering", "Scroll of the Hero of Cinder City", "Obsidian Codex"],
    "team_archetype": "Freeze Hypercarry / Cryo Hypercarry / Mono Cryo",
    },
     "charlotte": {
    "bis_artifact_set": "Scroll of the Hero of Cinder City",
    "secondary_artifact_set": "Noblesse Oblige",
    "niche_artifact_sets": ["Song of Days Past", "Ocean-Hued Clam", "Tenacity of the Millelith", "Maiden Beloved", "Blizzard Strayer", "Emblem of Severed Fate"],
    "team_archetype": "Healer / Cryo Support / Freeze Support / Quickswap",
    },
     "chongyun": {
    "bis_artifact_set": "Blizzard Strayer",
    "secondary_artifact_set": "Emblem of Severed Fate",
    "niche_artifact_sets": ["Noblesse Oblige", "Gladiator's Finale", "Golden Troupe", "Scroll of the Hero of Cinder City", "Shimenawa's Reminiscence", "Gilded Dreams"],
    "team_archetype": "Cryo Burst DPS / Freeze Support / Melt Support / Cryo Infusion",
    },
     "citlali": {
    "bis_artifact_set": "Scroll of the Hero of Cinder City",
    "secondary_artifact_set": "Gilded Dreams",
    "niche_artifact_sets": ["Tenacity of the Millelith", "Golden Troupe", "Deepwood Memories", "Noblesse Oblige", "Instructor's", "Flower of Paradise Lost"],
    "team_archetype": "Cryo Support / Melt Support / Freeze Support / Shield Support",
    },
     "dahlia": {
    "bis_artifact_set": "Scroll of the Hero of Cinder City",
    "secondary_artifact_set": "Noblesse Oblige",
    "niche_artifact_sets": ["Tenacity of the Millelith", "Song of Days Past", "Ocean-Hued Clam", "Instructor's", "Maiden Beloved", "The Exile"],
    "team_archetype": "Freeze teams with Skirk/Escoffier, or Normal Attack DPS teams like Yoimiya/Wanderer",
    },
     "diona": {
    "bis_artifact_set": "Noblesse Oblige",
    "secondary_artifact_set": "Scroll of the Hero of Cinder City",
    "niche_artifact_sets": ["Tenacity of the Millelith", "Instructor's", "Maiden Beloved", "Song of Days Past", "Ocean-Hued Clam", "The Exile"],
    "team_archetype": "Cryo Healer / Shield Support / Freeze Support / Battery",
    },
     "escoffier": {
    "bis_artifact_set": "Golden Troupe",
    "secondary_artifact_set": "Scroll of the Hero of Cinder City",
    "niche_artifact_sets": ["Blizzard Strayer", "Noblesse Oblige", "Tenacity of the Millelith", "Emblem of Severed Fate", "Gilded Dreams", "Deepwood Memories"],
    "team_archetype": "Off-Field Cryo DPS / Freeze Support / Cryo RES Shred / Quickswap",
    },
     "eula": {
    "bis_artifact_set": "Pale Flame",
    "secondary_artifact_set": "Marechaussee Hunter",
    "niche_artifact_sets": ["Bloodstained Chivalry", "Gladiator's Finale", "Scroll of the Hero of Cinder City", "Golden Troupe", "Shimenawa's Reminiscence", "Blizzard Strayer"],
    "team_archetype": "Physical Hypercarry / Cryo Hypercarry / Superconduct",
    },
     "freminet": {
    "bis_artifact_set": "Pale Flame",
    "secondary_artifact_set": "Blizzard Strayer",
    "niche_artifact_sets": ["Golden Troupe", "Gladiator's Finale", "Bloodstained Chivalry", "Scroll of the Hero of Cinder City", "Shimenawa's Reminiscence", "Marechaussee Hunter"],
    "team_archetype": "Physical DPS / Cryo DPS / Shatter / Freeze",
    },
     "ganyu": {
    "bis_artifact_set": "Blizzard Strayer",
    "secondary_artifact_set": "Wanderer's Troupe",
    "niche_artifact_sets": ["Shimenawa's Reminiscence", "Golden Troupe", "Marechaussee Hunter", "Scroll of the Hero of Cinder City", "Gilded Dreams", "Obsidian Codex"],
    "team_archetype": "Freeze Hypercarry / Melt Hypercarry / Charged Shot DPS",
    },
     "kaeya": {
    "bis_artifact_set": "Blizzard Strayer",
    "secondary_artifact_set": "Emblem of Severed Fate",
    "niche_artifact_sets": ["Noblesse Oblige", "Golden Troupe", "Gladiator's Finale", "Scroll of the Hero of Cinder City", "Shimenawa's Reminiscence", "Marechaussee Hunter"],
    "team_archetype": "Cryo DPS / Freeze Support / Melt DPS / Quickswap",
    },
     "layla": {
    "bis_artifact_set": "Tenacity of the Millelith",
    "secondary_artifact_set": "Scroll of the Hero of Cinder City",
    "niche_artifact_sets": ["Noblesse Oblige", "Blizzard Strayer", "Golden Troupe", "Song of Days Past", "Emblem of Severed Fate", "Ocean-Hued Clam"],
    "team_archetype": "Shield Support / Freeze Support / Cryo Support / Quickswap",
    },
     "mika": {
    "bis_artifact_set": "Noblesse Oblige",
    "secondary_artifact_set": "Scroll of the Hero of Cinder City",
    "niche_artifact_sets": ["Song of Days Past", "Ocean-Hued Clam", "Tenacity of the Millelith", "The Exile", "Instructor's", "Maiden Beloved"],
    "team_archetype": "Physical Support / Healer / ATK Speed Support / Cryo Battery",
    },
     "qiqi": {
    "bis_artifact_set": "Ocean-Hued Clam",
    "secondary_artifact_set": "Song of Days Past",
    "niche_artifact_sets": ["Tenacity of the Millelith", "Noblesse Oblige", "Maiden Beloved", "Scroll of the Hero of Cinder City", "Instructor's", "The Exile"],
    "team_archetype": "Healer / Cryo Support / Physical Support / Freeze Support",
    },
     "rosaria": {
    "bis_artifact_set": "Blizzard Strayer",
    "secondary_artifact_set": "Emblem of Severed Fate",
    "niche_artifact_sets": ["Noblesse Oblige", "Golden Troupe", "Scroll of the Hero of Cinder City", "Gladiator's Finale", "Gilded Dreams", "Marechaussee Hunter"],
    "team_archetype": "Cryo DPS / Freeze Support / Melt Support / Physical Support",
    },
     "shenhe": {
    "bis_artifact_set": "Noblesse Oblige",
    "secondary_artifact_set": "Scroll of the Hero of Cinder City",
    "niche_artifact_sets": ["Blizzard Strayer", "Tenacity of the Millelith", "Emblem of Severed Fate", "Golden Troupe", "The Exile", "Instructor's"],
    "team_archetype": "Cryo Buffer / Cryo Support / Freeze Support / Mono Cryo",
    },
     "skirk": {
    "bis_artifact_set": "Finale of the Deep Galleries",
    "secondary_artifact_set": "Marechaussee Hunter",
    "niche_artifact_sets": ["Blizzard Strayer", "Golden Troupe", "Gladiator's Finale", "Shimenawa's Reminiscence", "Obsidian Codex", "Scroll of the Hero of Cinder City"],
    "team_archetype": "Cryo Hypercarry / Freeze DPS / Cryo Quickswap",
    },
     "wriothesley": {
    "bis_artifact_set": "Marechaussee Hunter",
    "secondary_artifact_set": "Blizzard Strayer",
    "niche_artifact_sets": ["Shimenawa's Reminiscence", "Golden Troupe", "Echoes of an Offering", "Scroll of the Hero of Cinder City", "Desert Pavilion Chronicle", "Obsidian Codex"],
    "team_archetype": "Cryo Hypercarry / Melt DPS / Freeze DPS",
    },
     "sandrone": {
       "bis_artifact_set": "Disenchantment in Deep Shadow",
       "secondary_artifact_set": "A Day Carved From Rising Winds",
       "niche_artifact_sets": ["Gladiator's Finale", "Shimenawa Reminiscence", "Gilded Dreams"],
       "team_archetype": "Cryo Hypercarry",
     },
# ==========================================================
# GEO  
# ==========================================================
    "albedo": {
    "bis_artifact_set": "Golden Troupe",
    "secondary_artifact_set": "Husk of Opulent Dreams",
    "niche_artifact_sets": ["Scroll of the Hero of Cinder City", "Archaic Petra", "Noblesse Oblige", "Tenacity of the Millelith", "Emblem of Severed Fate", "Obsidian Codex"],
    "team_archetype": "Off-Field Geo DPS / Mono Geo / Geo Support / Quickswap",
    }, 
     "chiori": {
    "bis_artifact_set": "Golden Troupe",
    "secondary_artifact_set": "Husk of Opulent Dreams",
    "niche_artifact_sets": ["Scroll of the Hero of Cinder City", "Archaic Petra", "Gladiator's Finale", "Marechaussee Hunter", "Obsidian Codex", "Shimenawa's Reminiscence"],
    "team_archetype": "Off-Field Geo DPS / Mono Geo / Geo Hypercarry / Quickswap",
    },
     "gorou": {
    "bis_artifact_set": "Scroll of the Hero of Cinder City",
    "secondary_artifact_set": "Noblesse Oblige",
    "niche_artifact_sets": ["The Exile", "Husk of Opulent Dreams", "Emblem of Severed Fate", "Archaic Petra", "Instructor's", "Tenacity of the Millelith"],
    "team_archetype": "Geo Buffer / Mono Geo Support / DEF Buffer / Battery",
    },
     "itto": {
    "bis_artifact_set": "Husk of Opulent Dreams",
    "secondary_artifact_set": "Nighttime Whispers in the Echoing Woods",
    "niche_artifact_sets": ["Golden Troupe", "Gladiator's Finale", "Scroll of the Hero of Cinder City", "Archaic Petra", "Marechaussee Hunter", "Obsidian Codex"],
    "team_archetype": "Geo Hypercarry / Mono Geo / DEF Scaling DPS",
    },
     "kachina": {
    "bis_artifact_set": "Scroll of the Hero of Cinder City",
    "secondary_artifact_set": "Scroll of the Hero of Cinder City",
    "niche_artifact_sets": ["Noblesse Oblige", "Archaic Petra", "Husk of Opulent Dreams", "Golden Troupe", "Instructor's", "Tenacity of the Millelith"],
    "team_archetype": "Geo Support / Nightsoul Support / Crystalize Support / Quickswap",
    },
     "navia": {
    "bis_artifact_set": "Nighttime Whispers in the Echoing Woods",
    "secondary_artifact_set": "Golden Troupe",
    "niche_artifact_sets": ["Gladiator's Finale", "Husk of Opulent Dreams", "Scroll of the Hero of Cinder City", "Archaic Petra", "Marechaussee Hunter", "Obsidian Codex"],
    "team_archetype": "Geo Hypercarry / Crystalize DPS / Quickswap",
    },
     "ningguang": {
    "bis_artifact_set": "Nighttime Whispers in the Echoing Woods",
    "secondary_artifact_set": "Archaic Petra",
    "niche_artifact_sets": ["Golden Troupe", "Scroll of the Hero of Cinder City", "Gladiator's Finale", "Marechaussee Hunter", "Shimenawa's Reminiscence", "Obsidian Codex"],
    "team_archetype": "Geo Hypercarry / Geo DPS / Crystalize DPS / Quickswap",
    },
     "noelle": {
    "bis_artifact_set": "Husk of Opulent Dreams",
    "secondary_artifact_set": "Nighttime Whispers in the Echoing Woods",
    "niche_artifact_sets": ["Gladiator's Finale", "Golden Troupe", "Archaic Petra", "Scroll of the Hero of Cinder City", "Marechaussee Hunter", "Obsidian Codex"],
    "team_archetype": "Geo Hypercarry / DEF Scaling DPS / Healer / Mono Geo",
    },
     "xilonen": {
    "bis_artifact_set": "Scroll of the Hero of Cinder City",
    "secondary_artifact_set": "Archaic Petra",
    "niche_artifact_sets": ["Noblesse Oblige", "Golden Troupe", "Tenacity of the Millelith", "Instructor's", "Husk of Opulent Dreams", "Song of Days Past"],
    "team_archetype": "Geo Support / RES Shred Support / Crystalize Support / Quickswap",
    },
     "yunjin": {
    "bis_artifact_set": "Husk of Opulent Dreams",
    "secondary_artifact_set": "Scroll of the Hero of Cinder City",
    "niche_artifact_sets": ["Noblesse Oblige", "Archaic Petra", "Emblem of Severed Fate", "The Exile", "Instructor's", "Tenacity of the Millelith"],
    "team_archetype": "Normal Attack Buffer / Geo Support / DEF Support / Quickswap",
    },
     "zhongli": {
    "bis_artifact_set": "Scroll of the Hero of Cinder City",
    "secondary_artifact_set": "Tenacity of the Millelith",
    "niche_artifact_sets": ["Archaic Petra", "Noblesse Oblige", "Deepwood Memories", "Instructor's", "Golden Troupe", "Emblem of Severed Fate"],
    "team_archetype": "Universal Shield Support / Geo Support / Burst Support / RES Shred",
    },
    "aloy": {
    "bis_artifact_set": "Noblesse Oblige",
    "secondary_artifact_set": "Blizzard Strayer",
    "niche_artifact_sets": ["Gilded Dreams", "Emblem of Severed Fate", "Gladiator's Finale"],
    "team_archetype": "Quick-Swap Cryo Battery & Burst DPS",
    },
    "durin": {
    "bis_artifact_set": "Crimson Witch of Flames",
    "secondary_artifact_set": "Emblem of Severed Fate",
    "niche_artifact_sets": ["Noblesse Oblige", "Gilded Dreams", "Vourukasha's Glow"],
    "team_archetype": "Off-field Pyro Sub-DPS & Burst Support",
    },
    "jahoda": {
    "bis_artifact_set": "Viridescent Venerer",
    "secondary_artifact_set": "Noblesse Oblige",
    "niche_artifact_sets": ["Emblem of Severed Fate", "Instructor's", "Wanderer's Troupe"],
    "team_archetype": "Off-field Swirl Support, Healer & EM Buffer",
    },
}


WEAPON_TIERS: Dict[str, Dict[str, Any]] = {

# ==========================================================
# PYRO
# ==========================================================

    "arlecchino": {
    "bis_weapon": "Crimson Moon's Semblance",
    "secondary_weapon": "Staff of Homa",
    "f2p_weapon": ["White Tassel", "Missive Windspear", "Blackcliff Pole", "Deathmatch", "Ballad of the Fjords", "Prototype Starglitter"],
    "niche_weapon": ["Primordial Jade Winged-Spear", "Calamity Queller", "Lumidouce Elegy", "Vortex Vanquisher", "Lithic Spear"],
    },
    "bennett": {
    "bis_weapon": "Mistsplitter Reforged",
    "secondary_weapon": "Aquila Favonia",
    "f2p_weapon": ["Sapwood Blade", "Favonius Sword", "Sacrificial Sword", "Prototype Rancour", "Amenoma Kageuchi", "Fleuve Cendre Ferryman", "The Alley Flash"],
    "niche_weapon": ["Skyward Blade", "Freedom-Sworn", "Summit Shaper", "Absolution", "Haran Geppaku Futsu", "Light of Foliar Incision"],
    },
    "chevreuse": {
    "bis_weapon": "Symphonist of Scents",
    "secondary_weapon": "Favonius Lance",
    "f2p_weapon": ["Dialogues of the Desert Sages", "Rightful Reward", "Black Tassel", "Prototype Starglitter", "Tamayuratei no Ohanashi", "Missive Windspear"],
    "niche_weapon": ["Engulfing Lightning", "Skyward Spine", "Calamity Queller", "Vortex Vanquisher", "Staff of Homa", "Lumidouce Elegy"],
    },
    "dehya": {
    "bis_weapon": "Beacon of the Reed Sea",
    "secondary_weapon": "Wolf's Gravestone",
    "f2p_weapon": ["Ultimate Overlord's Mega Magic Sword", "Mailed Flower", "Tidal Shadow", "Prototype Archaic", "Rainslasher", "Favonius Greatsword", "Sacrificial Greatsword"],
    "niche_weapon": ["Redhorn Stonethresher", "Serpent Spine", "The Unforged", "Skyward Pride", "Earth Shaker", "Talking Stick", "Makhaira Aquamarine"],
    },
    "diluc": {
    "bis_weapon": "Beacon of the Reed Sea",
    "secondary_weapon": "Redhorn Stonethresher",
    "f2p_weapon": ["Prototype Archaic", "Tidal Shadow", "Mailed Flower", "Ultimate Overlord's Mega Magic Sword", "Blackcliff Slasher", "Rainslasher"],
    "niche_weapon": ["Wolf's Gravestone", "Serpent Spine", "Verdict", "The Unforged", "Skyward Pride", "Akuoumaru", "Makhaira Aquamarine", "Talking Stick"],
    },
    "gaming": {
    "bis_weapon": "Serpent Spine",
    "secondary_weapon": "Beacon of the Reed Sea",
    "f2p_weapon": ["Mailed Flower", "Prototype Archaic", "Tidal Shadow", "Ultimate Overlord's Mega Magic Sword", "Rainslasher", "Blackcliff Slasher"],
    "niche_weapon": ["Redhorn Stonethresher", "Wolf's Gravestone", "Skyward Pride", "Verdict", "The Unforged", "Talking Stick", "Makhaira Aquamarine"],
    },
    "hutao": {
    "bis_weapon": "Staff of Homa",
    "secondary_weapon": "Staff of the Scarlet Sands",
    "f2p_weapon": ["Dragon's Bane", "Ballad of the Fjords", "Deathmatch", "Blackcliff Pole", "Missive Windspear", "White Tassel", "Kitain Cross Spear"],
    "niche_weapon": ["Primordial Jade Winged-Spear", "Calamity Queller", "Lumidouce Elegy", "Vortex Vanquisher", "Skyward Spine"],
    },
    "klee": {
    "bis_weapon": "Sunny Morning Sleep-In",
    "secondary_weapon": "Lost Prayer to the Sacred Winds",
    "f2p_weapon": ["The Widsith", "Flowing Purity", "Mappa Mare", "Ballad of the Boundless Blue", "Blackcliff Agate", "Solar Pearl", "Twin Nephrite"],
    "niche_weapon": ["Cashflow Supervision", "Kagura's Verity", "Skyward Atlas", "Memory of Dust", "Tulaytullah's Remembrance", "Surf's Up"],
    },
    "lyney": {
    "bis_weapon": "The First Great Magic",
    "secondary_weapon": "Aqua Simulacra",
    "f2p_weapon": ["Scion of the Blazing Sun", "Song of Stillness", "Prototype Crescent", "Hamayumi", "Blackcliff Warbow", "Ibis Piercer", "Chain Breaker"],
    "niche_weapon": ["Polar Star", "Skyward Harp", "Hunter's Path", "Elegy for the End", "Thundering Pulse", "Amos' Bow"],
    },
    "mavuika": {
    "bis_weapon": "A Thousand Blazing Suns",
    "secondary_weapon": "Beacon of the Reed Sea",
    "f2p_weapon": ["Mailed Flower", "Tidal Shadow", "Prototype Archaic", "Ultimate Overlord's Mega Magic Sword", "Earth Shaker", "Rainslasher"],
    "niche_weapon": ["Verdict", "Redhorn Stonethresher", "Serpent Spine", "Wolf's Gravestone", "The Unforged", "Skyward Pride", "Fang of the Mountain King", "Talking Stick"],
    },
    "thoma": {
    "bis_weapon": "Kitain Cross Spear",
    "secondary_weapon": "Favonius Lance",
    "f2p_weapon": ["Black Tassel", "Rightful Reward", "Dialogues of the Desert Sages", "Prototype Starglitter", "Missive Windspear", "Tamayuratei no Ohanashi"],
    "niche_weapon": ["Engulfing Lightning", "Skyward Spine", "Staff of Homa", "Calamity Queller", "Vortex Vanquisher", "Lumidouce Elegy"],
    },
    "xiangling": {
    "bis_weapon": "Engulfing Lightning",
    "secondary_weapon": "Staff of the Scarlet Sands",
    "f2p_weapon": ["The Catch", "Dragon's Bane", "Favonius Lance", "Kitain Cross Spear", "Missive Windspear", "Prototype Starglitter", "Tamayuratei no Ohanashi", "Dialogues of the Desert Sages"],
    "niche_weapon": ["Staff of Homa", "Calamity Queller", "Lumidouce Elegy", "Skyward Spine", "Primordial Jade Winged-Spear", "Vortex Vanquisher"],
    },
    "xinyan": {
    "bis_weapon": "Redhorn Stonethresher",
    "secondary_weapon": "Beacon of the Reed Sea",
    "f2p_weapon": ["Prototype Archaic", "Snow-Tombed Starsilver", "Blackcliff Slasher", "Tidal Shadow", "Ultimate Overlord's Mega Magic Sword", "Favonius Greatsword", "Sacrificial Greatsword", "Whiteblind"],
    "niche_weapon": ["Wolf's Gravestone", "Serpent Spine", "Skyward Pride", "The Unforged", "Verdict", "Akuoumaru", "Talking Stick", "Earth Shaker"],
    },

# ==========================================================
# HYDRO
# ==========================================================

    "barbara": {
    "bis_weapon": "Thrilling Tales of Dragon Slayers",
    "secondary_weapon": "Prototype Amber",
    "f2p_weapon": ["Prototype Amber", "Thrilling Tales of Dragon Slayers", "Favonius Codex", "Fruit of Fulfillment", "Magic Guide", "Otherworldly Story", "Emerald Orb"],
    "niche_weapon": ["Everlasting Moonglow", "Jadefall's Splendor", "Hakushin Ring", "A Thousand Floating Dreams", "Sacrificial Fragments", "Mappa Mare"],
    },
    "candace": {
    "bis_weapon": "Favonius Lance",
    "secondary_weapon": "Black Tassel",
    "f2p_weapon": ["Favonius Lance", "Black Tassel", "Rightful Reward", "Prototype Starglitter", "Dialogues of the Desert Sages", "Missive Windspear", "Tamayuratei no Ohanashi"],
    "niche_weapon": ["Staff of Homa", "Engulfing Lightning", "Skyward Spine", "Calamity Queller", "Lumidouce Elegy", "Staff of the Scarlet Sands"],
    },
    "childe": {
    "bis_weapon": "Polar Star",
    "secondary_weapon": "Aqua Simulacra",
    "f2p_weapon": ["The Viridescent Hunt", "Blackcliff Warbow", "Prototype Crescent", "Chain Breaker", "Song of Stillness", "Ibis Piercer", "Hamayumi"],
    "niche_weapon": ["Skyward Harp", "Hunter's Path", "Thundering Pulse", "Elegy for the End", "The First Great Magic", "Amos' Bow"],
    },
    "furina": {
    "bis_weapon": "Splendor of Tranquil Waters",
    "secondary_weapon": "Uraku Misugiri",
    "f2p_weapon": ["Festering Desire", "Fleuve Cendre Ferryman", "Favonius Sword", "Sacrificial Sword", "Wolf-Fang", "The Dockhand's Assistant"],
    "niche_weapon": ["Key of Khaj-Nisut", "Freedom-Sworn", "Skyward Blade", "Primordial Jade Cutter", "Haran Geppaku Futsu", "Light of Foliar Incision", "Absolution"],
    },
    "kokomi": {
    "bis_weapon": "Everlasting Moonglow",
    "secondary_weapon": "Prototype Amber",
    "f2p_weapon": ["Prototype Amber", "Thrilling Tales of Dragon Slayers", "Hakushin Ring", "Fruit of Fulfillment", "Favonius Codex", "Magic Guide", "Otherworldly Story"],
    "niche_weapon": ["Jadefall's Splendor", "A Thousand Floating Dreams", "Sacrificial Fragments", "Mappa Mare", "Sunny Morning Sleep-In", "Starcaller's Watch"],
    },
    "mona": {
    "bis_weapon": "A Thousand Floating Dreams",
    "secondary_weapon": "Favonius Codex",
    "f2p_weapon": ["Thrilling Tales of Dragon Slayers", "Favonius Codex", "Prototype Amber", "Fruit of Fulfillment", "Flowing Purity", "Mappa Mare", "Ballad of the Boundless Blue"],
    "niche_weapon": ["Skyward Atlas", "Lost Prayer to the Sacred Winds", "Kagura's Verity", "Cashflow Supervision", "Memory of Dust", "Starcaller's Watch"],
    },
    "mualani": {
    "bis_weapon": "Surf's Up",
    "secondary_weapon": "Tome of the Eternal Flow",
    "f2p_weapon": ["Ring of Yaxche", "The Widsith", "Flowing Purity", "Mappa Mare", "Ballad of the Boundless Blue", "Prototype Amber", "Blackcliff Agate", "Twin Nephrite"],
    "niche_weapon": ["Cashflow Supervision", "Lost Prayer to the Sacred Winds", "Skyward Atlas", "Memory of Dust", "Kagura's Verity", "Starcaller's Watch", "Sunny Morning Sleep-In"],
    },
    "neuvillette": {
    "bis_weapon": "Tome of the Eternal Flow",
    "secondary_weapon": "Sacrificial Jade",
    "f2p_weapon": ["Prototype Amber", "The Widsith", "Ring of Yaxche", "Flowing Purity", "Ballad of the Boundless Blue", "Favonius Codex", "Magic Guide", "Twin Nephrite"],
    "niche_weapon": ["Cashflow Supervision", "Lost Prayer to the Sacred Winds", "Skyward Atlas", "Memory of Dust", "Jadefall's Splendor", "Surf's Up", "Kagura's Verity", "Starcaller's Watch", "Everlasting Moonglow"],
    },
    "nilou": {
    "bis_weapon": "Key of Khaj-Nisut",
    "secondary_weapon": "Primordial Jade Cutter",
    "f2p_weapon": ["Favonius Sword", "Sacrificial Sword", "Fleuve Cendre Ferryman", "Sapwood Blade", "The Dockhand's Assistant", "Wolf-Fang"],
    "niche_weapon": ["Freedom-Sworn", "Skyward Blade", "Absolution", "Haran Geppaku Futsu", "Light of Foliar Incision", "Splendor of Tranquil Waters"],
    },
    "sigewinne": {
    "bis_weapon": "Silvershower Heartstrings",
    "secondary_weapon": "Elegy for the End",
    "f2p_weapon": ["Recurve Bow", "Favonius Warbow", "Sacrificial Bow", "End of the Line", "Messenger", "Slingshot"],
    "niche_weapon": ["Aqua Simulacra", "Polar Star", "Skyward Harp", "Hunter's Path", "The First Great Magic", "Elegy for the End"],
    },
    "xingqiu": {
    "bis_weapon": "Sacrificial Sword",
    "secondary_weapon": "Favonius Sword",
    "f2p_weapon": ["Favonius Sword", "Fleuve Cendre Ferryman", "Sapwood Blade", "Amenoma Kageuchi", "Skyrider Sword", "Harbinger of Dawn", "The Dockhand's Assistant", "Wolf-Fang"],
    "niche_weapon": ["Freedom-Sworn", "Skyward Blade", "Primordial Jade Cutter", "Light of Foliar Incision", "Absolution", "Mistsplitter Reforged", "Haran Geppaku Futsu"],
    },
    "yelan": {
    "bis_weapon": "Aqua Simulacra",
    "secondary_weapon": "Elegy for the End",
    "f2p_weapon": ["Favonius Warbow", "Sacrificial Bow", "Slingshot", "Recurve Bow", "End of the Line", "Messenger", "Chain Breaker"],
    "niche_weapon": ["Polar Star", "Skyward Harp", "Hunter's Path", "The First Great Magic", "Thundering Pulse", "Silvershower Heartstrings", "Elegy for the End"],
    },

# ==========================================================
# ANEMO
# ==========================================================

    "chasca": {
    "bis_weapon": "Astral Vulture's Crimson Plumage",
    "secondary_weapon": "The First Great Magic",
    "f2p_weapon": ["Chain Breaker", "Song of Stillness", "Prototype Crescent", "Ibis Piercer", "Hamayumi", "Blackcliff Warbow", "Slingshot"],
    "niche_weapon": ["Aqua Simulacra", "Polar Star", "Skyward Harp", "Hunter's Path", "Thundering Pulse", "Elegy for the End", "Amos' Bow"],
    },
    "faruzan": {
    "bis_weapon": "Elegy for the End",
    "secondary_weapon": "Favonius Warbow",
    "f2p_weapon": ["Favonius Warbow", "Sacrificial Bow", "End of the Line", "Prototype Crescent", "Messenger", "Recurve Bow"],
    "niche_weapon": ["Skyward Harp", "Polar Star", "Aqua Simulacra", "The First Great Magic", "Hunter's Path", "Thundering Pulse"],
    },
    "heizou": {
    "bis_weapon": "Tulaytullah's Remembrance",
    "secondary_weapon": "Lost Prayer to the Sacred Winds",
    "f2p_weapon": ["The Widsith", "Solar Pearl", "Flowing Purity", "Mappa Mare", "Ballad of the Boundless Blue", "Blackcliff Agate", "Twin Nephrite", "Magic Guide"],
    "niche_weapon": ["Skyward Atlas", "Cashflow Supervision", "Kagura's Verity", "Memory of Dust", "Surf's Up", "Starcaller's Watch", "Sunny Morning Sleep-In"],
    },
    "jean": {
    "bis_weapon": "Freedom-Sworn",
    "secondary_weapon": "Favonius Sword",
    "f2p_weapon": ["Favonius Sword", "Amenoma Kageuchi", "Sapwood Blade", "Fleuve Cendre Ferryman", "Sacrificial Sword", "Prototype Rancour", "Skyrider Sword"],
    "niche_weapon": ["Skyward Blade", "Primordial Jade Cutter", "Mistsplitter Reforged", "Light of Foliar Incision", "Absolution", "Haran Geppaku Futsu", "Aquila Favonia"],
    },
    "kazuha": {
    "bis_weapon": "Freedom-Sworn",
    "secondary_weapon": "Xiphos' Moonlight",
    "f2p_weapon": ["Iron Sting", "Favonius Sword", "Sacrificial Sword", "Sapwood Blade", "Fleuve Cendre Ferryman", "Dark Iron Sword", "Skyrider Sword"],
    "niche_weapon": ["Skyward Blade", "Primordial Jade Cutter", "Light of Foliar Incision", "Mistsplitter Reforged", "Absolution", "Haran Geppaku Futsu", "Uraku Misugiri"],
    },
    "lanyan": {
    "bis_weapon": "Sunny Morning Sleep-In",
    "secondary_weapon": "Sacrificial Fragments",
    "f2p_weapon": ["Thrilling Tales of Dragon Slayers", "Favonius Codex", "Prototype Amber", "Mappa Mare", "Fruit of Fulfillment", "Magic Guide", "Emerald Orb"],
    "niche_weapon": ["A Thousand Floating Dreams", "Starcaller's Watch", "Jadefall's Splendor", "Lost Prayer to the Sacred Winds", "Skyward Atlas", "Kagura's Verity"],
    },
    "lynette": {
    "bis_weapon": "Freedom-Sworn",
    "secondary_weapon": "Favonius Sword",
    "f2p_weapon": ["Favonius Sword", "Fleuve Cendre Ferryman", "Sacrificial Sword", "Amenoma Kageuchi", "Sapwood Blade", "Harbinger of Dawn", "Skyrider Sword"],
    "niche_weapon": ["Skyward Blade", "Primordial Jade Cutter", "Mistsplitter Reforged", "Light of Foliar Incision", "Absolution", "Haran Geppaku Futsu", "Uraku Misugiri"],
    },
    "sayu": {
    "bis_weapon": "Favonius Greatsword",
    "secondary_weapon": "Katsuragikiri Nagamasa",
    "f2p_weapon": ["Katsuragikiri Nagamasa", "Favonius Greatsword", "Sacrificial Greatsword", "Forest Regalia", "Prototype Archaic", "Ultimate Overlord's Mega Magic Sword", "Mailed Flower"],
    "niche_weapon": ["Skyward Pride", "Wolf's Gravestone", "Beacon of the Reed Sea", "Redhorn Stonethresher", "The Unforged", "Serpent Spine", "Talking Stick"],
    },
    "sucrose": {
    "bis_weapon": "Sacrificial Fragments",
    "secondary_weapon": "A Thousand Floating Dreams",
    "f2p_weapon": ["Thrilling Tales of Dragon Slayers", "Magic Guide", "Mappa Mare", "Fruit of Fulfillment", "Prototype Amber", "Favonius Codex", "Ballad of the Boundless Blue"],
    "niche_weapon": ["Sunny Morning Sleep-In", "Starcaller's Watch", "Lost Prayer to the Sacred Winds", "Skyward Atlas", "Kagura's Verity", "Hakushin Ring", "Jadefall's Splendor"],
    },
    "venti": {
    "bis_weapon": "Elegy for the End",
    "secondary_weapon": "The Stringless",
    "f2p_weapon": ["Favonius Warbow", "The Stringless", "End of the Line", "Prototype Crescent", "Chain Breaker", "Messenger", "Slingshot"],
    "niche_weapon": ["Polar Star", "Skyward Harp", "Aqua Simulacra", "Hunter's Path", "The First Great Magic", "Thundering Pulse", "Amos' Bow"],
    },
    "wanderer": {
    "bis_weapon": "Tulaytullah's Remembrance",
    "secondary_weapon": "Cashflow Supervision",
    "f2p_weapon": ["The Widsith", "Flowing Purity", "Blackcliff Agate", "Ballad of the Boundless Blue", "Mappa Mare", "Twin Nephrite", "Magic Guide", "Solar Pearl"],
    "niche_weapon": ["Lost Prayer to the Sacred Winds", "Skyward Atlas", "Memory of Dust", "Surf's Up", "Starcaller's Watch", "Sunny Morning Sleep-In", "Kagura's Verity", "A Thousand Floating Dreams"],
    },
    "xiao": {
    "bis_weapon": "Primordial Jade Winged-Spear",
    "secondary_weapon": "Staff of Homa",
    "f2p_weapon": ["Blackcliff Pole", "Deathmatch", "Ballad of the Fjords", "Missive Windspear", "Favonius Lance", "Prototype Starglitter", "Rightful Reward"],
    "niche_weapon": ["Calamity Queller", "Lumidouce Elegy", "Vortex Vanquisher", "Skyward Spine", "Staff of the Scarlet Sands", "Engulfing Lightning", "Crimson Moon's Semblance"],
    },
    "xianyun": {
    "bis_weapon": "Crane's Echoing Call",
    "secondary_weapon": "Skyward Atlas",
    "f2p_weapon": ["Oathsworn Eye", "Favonius Codex", "Prototype Amber", "Fruit of Fulfillment", "Flowing Purity", "Thrilling Tales of Dragon Slayers", "Ballad of the Boundless Blue"],
    "niche_weapon": ["Lost Prayer to the Sacred Winds", "Starcaller's Watch", "Sunny Morning Sleep-In", "Memory of Dust", "Cashflow Supervision", "Jadefall's Splendor", "A Thousand Floating Dreams"],
    },
# ==========================================================
# ELECTRO
# ==========================================================
    "beidou": {
    "bis_weapon": "Wolf's Gravestone",
    "secondary_weapon": "Beacon of the Reed Sea",
    "f2p_weapon": ["Ultimate Overlord's Mega Magic Sword", "Prototype Archaic", "Tidal Shadow", "Akuoumaru", "Mailed Flower", "Favonius Greatsword", "Sacrificial Greatsword"],
    "niche_weapon": ["Serpent Spine", "Redhorn Stonethresher", "Skyward Pride", "Verdict", "The Unforged", "Talking Stick", "Earth Shaker"],
    }, 
     "clorinde": {
    "bis_weapon": "Absolution",
    "secondary_weapon": "Mistsplitter Reforged",
    "f2p_weapon": ["Finale of the Deep", "The Black Sword", "Lion's Roar", "Amenoma Kageuchi", "Harbinger of Dawn", "Sapwood Blade", "Fleuve Cendre Ferryman"],
    "niche_weapon": ["Primordial Jade Cutter", "Light of Foliar Incision", "Haran Geppaku Futsu", "Uraku Misugiri", "Freedom-Sworn", "Skyward Blade"],
    },
     "cyno": {
    "bis_weapon": "Staff of the Scarlet Sands",
    "secondary_weapon": "Lumidouce Elegy",
    "f2p_weapon": ["Ballad of the Fjords", "Deathmatch", "Missive Windspear", "Kitain Cross Spear", "Dragon's Bane", "White Tassel", "Rightful Reward"],
    "niche_weapon": ["Primordial Jade Winged-Spear", "Staff of Homa", "Calamity Queller", "Engulfing Lightning", "Crimson Moon's Semblance", "Skyward Spine", "Vortex Vanquisher"],
    },
     "dori": {
    "bis_weapon": "Favonius Greatsword",
    "secondary_weapon": "Skyward Pride",
    "f2p_weapon": ["Forest Regalia", "Sacrificial Greatsword", "Prototype Archaic", "Ultimate Overlord's Mega Magic Sword", "Mailed Flower", "Earth Shaker", "Katsuragikiri Nagamasa"],
    "niche_weapon": ["Wolf's Gravestone", "Beacon of the Reed Sea", "The Unforged", "Verdict", "Redhorn Stonethresher", "Serpent Spine", "Talking Stick"],
    },
     "fischl": {
    "bis_weapon": "The Daybreak Chronicles",
    "secondary_weapon": "Polar Star",
    "f2p_weapon": ["Song of Stillness", "Chain Breaker", "The Stringless", "Fading Twilight", "Prototype Crescent", "Slingshot", "Messenger"],
    "niche_weapon": ["Aqua Simulacra", "Skyward Harp", "Hunter's Path", "The First Great Magic", "Thundering Pulse", "Astral Vulture's Crimson Plumage", "Amos' Bow"],
    },
     "iansan": {
    "bis_weapon": "Symphonist of Scents",
    "secondary_weapon": "Engulfing Lightning",
    "f2p_weapon": ["Favonius Lance", "Rightful Reward", "Prototype Starglitter", "Dialogues of the Desert Sages", "Missive Windspear", "Tamayuratei no Ohanashi", "Black Tassel"],
    "niche_weapon": ["Skyward Spine", "Staff of Homa", "Calamity Queller", "Staff of the Scarlet Sands", "Lumidouce Elegy", "Vortex Vanquisher", "Crimson Moon's Semblance"],
    },
     "keqing": {
    "bis_weapon": "Mistsplitter Reforged",
    "secondary_weapon": "Absolution",
    "f2p_weapon": ["Lion's Roar", "Finale of the Deep", "Amenoma Kageuchi", "Harbinger of Dawn", "Sapwood Blade", "Fleuve Cendre Ferryman", "The Black Sword"],
    "niche_weapon": ["Primordial Jade Cutter", "Light of Foliar Incision", "Haran Geppaku Futsu", "Uraku Misugiri", "Skyward Blade", "Freedom-Sworn"],
    },
     "kukishinobu": {
    "bis_weapon": "Freedom-Sworn",
    "secondary_weapon": "Xiphos' Moonlight",
    "f2p_weapon": ["Iron Sting", "Dark Iron Sword", "Sapwood Blade", "Favonius Sword", "Sacrificial Sword", "Fleuve Cendre Ferryman", "Skyrider Sword"],
    "niche_weapon": ["Key of Khaj-Nisut", "Skyward Blade", "Primordial Jade Cutter", "Light of Foliar Incision", "Absolution", "Haran Geppaku Futsu"],
    },
     "sara": {
    "bis_weapon": "Elegy for the End",
    "secondary_weapon": "Skyward Harp",
    "f2p_weapon": ["Fading Twilight", "Sacrificial Bow", "Favonius Warbow", "End of the Line", "Prototype Crescent", "Messenger", "Recurve Bow"],
    "niche_weapon": ["Polar Star", "Aqua Simulacra", "The First Great Magic", "Hunter's Path", "Thundering Pulse", "Astral Vulture's Crimson Plumage"],
    },
     "lisa": {
    "bis_weapon": "Reliquary of Truth",
    "secondary_weapon": "Kagura's Verity",
    "f2p_weapon": ["The Widsith", "Flowing Purity", "Mappa Mare", "Fruit of Fulfillment", "Magic Guide", "Ballad of the Boundless Blue", "Favonius Codex"],
    "niche_weapon": ["Lost Prayer to the Sacred Winds", "Skyward Atlas", "Memory of Dust", "Cashflow Supervision", "Starcaller's Watch", "Sunny Morning Sleep-In"],
    },
     "ororon": {
    "bis_weapon": "Elegy for the End",
    "secondary_weapon": "The Stringless",
    "f2p_weapon": ["Fading Twilight", "Chain Breaker", "Song of Stillness", "Prototype Crescent", "End of the Line", "Messenger", "Slingshot"],
    "niche_weapon": ["Polar Star", "Skyward Harp", "Aqua Simulacra", "Hunter's Path", "The First Great Magic", "Thundering Pulse", "Astral Vulture's Crimson Plumage"],
    },
     "raiden": {
    "bis_weapon": "Engulfing Lightning",
    "secondary_weapon": "Staff of the Scarlet Sands",
    "f2p_weapon": ["The Catch", "Missive Windspear", "Prototype Starglitter", "Dialogues of the Desert Sages", "Kitain Cross Spear", "Rightful Reward", "Favonius Lance"],
    "niche_weapon": ["Staff of Homa", "Calamity Queller", "Primordial Jade Winged-Spear", "Lumidouce Elegy", "Skyward Spine", "Crimson Moon's Semblance", "Vortex Vanquisher"],
    },
     "razor": {
    "bis_weapon": "Beacon of the Reed Sea",
    "secondary_weapon": "Redhorn Stonethresher",
    "f2p_weapon": ["Prototype Archaic", "Snow-Tombed Starsilver", "Tidal Shadow", "Ultimate Overlord's Mega Magic Sword", "Mailed Flower", "Favonius Greatsword", "Earth Shaker"],
    "niche_weapon": ["Wolf's Gravestone", "Serpent Spine", "Skyward Pride", "Verdict", "The Unforged", "Talking Stick", "Akuoumaru"],
    },
     "sethos": {
    "bis_weapon": "Hunter's Path",
    "secondary_weapon": "The First Great Magic",
    "f2p_weapon": ["Slingshot", "Chain Breaker", "Prototype Crescent", "Hamayumi", "Song of Stillness", "Ibis Piercer", "Messenger"],
    "niche_weapon": ["Polar Star", "Skyward Harp", "Aqua Simulacra", "Thundering Pulse", "Astral Vulture's Crimson Plumage", "Amos' Bow", "Elegy for the End"],
    },
     "yaemiko": {
    "bis_weapon": "Kagura's Verity",
    "secondary_weapon": "A Thousand Floating Dreams",
    "f2p_weapon": ["The Widsith", "Mappa Mare", "Flowing Purity", "Ballad of the Boundless Blue", "Fruit of Fulfillment", "Magic Guide", "Favonius Codex"],
    "niche_weapon": ["Lost Prayer to the Sacred Winds", "Skyward Atlas", "Cashflow Supervision", "Memory of Dust", "Surf's Up", "Starcaller's Watch", "Sunny Morning Sleep-In"],
    },
# ==========================================================
# DENDRO
# ==========================================================
    "alhaitham": {
    "bis_weapon": "Light of Foliar Incision",
    "secondary_weapon": "Primordial Jade Cutter",
    "f2p_weapon": ["Iron Sting", "Toukabou Shigure", "Sapwood Blade", "Harbinger of Dawn", "Dark Iron Sword", "Amenoma Kageuchi", "Finale of the Deep"],
    "niche_weapon": ["Mistsplitter Reforged", "Haran Geppaku Futsu", "Absolution", "Freedom-Sworn", "Uraku Misugiri", "Skyward Blade", "Key of Khaj-Nisut"],
    },
     "baizhu": {
    "bis_weapon": "Jadefall's Splendor",
    "secondary_weapon": "Prototype Amber",
    "f2p_weapon": ["Prototype Amber", "Favonius Codex", "Fruit of Fulfillment", "Thrilling Tales of Dragon Slayers", "Magic Guide", "Ballad of the Boundless Blue", "Flowing Purity"],
    "niche_weapon": ["A Thousand Floating Dreams", "Starcaller's Watch", "Everlasting Moonglow", "Lost Prayer to the Sacred Winds", "Skyward Atlas", "Memory of Dust", "Sunny Morning Sleep-In"],
    },
     "collei": {
    "bis_weapon": "Elegy for the End",
    "secondary_weapon": "Favonius Warbow",
    "f2p_weapon": ["Favonius Warbow", "Sacrificial Bow", "End of the Line", "Fading Twilight", "Prototype Crescent", "Messenger", "Recurve Bow"],
    "niche_weapon": ["Polar Star", "Skyward Harp", "The Stringless", "Aqua Simulacra", "Hunter's Path", "The First Great Magic", "Astral Vulture's Crimson Plumage"],
    },
     "emilie": {
    "bis_weapon": "Lumidouce Elegy",
    "secondary_weapon": "Staff of Homa",
    "f2p_weapon": ["Missive Windspear", "Rightful Reward", "Kitain Cross Spear", "Favonius Lance", "Dialogues of the Desert Sages", "Prototype Starglitter", "Black Tassel"],
    "niche_weapon": ["Calamity Queller", "Staff of the Scarlet Sands", "Engulfing Lightning", "Primordial Jade Winged-Spear", "Skyward Spine", "Vortex Vanquisher", "Crimson Moon's Semblance"],
    },
     "kaveh": {
    "bis_weapon": "Beacon of the Reed Sea",
    "secondary_weapon": "Mailed Flower",
    "f2p_weapon": ["Mailed Flower", "Forest Regalia", "Favonius Greatsword", "Sacrificial Greatsword", "Ultimate Overlord's Mega Magic Sword", "Prototype Archaic", "Earth Shaker"],
    "niche_weapon": ["Wolf's Gravestone", "Skyward Pride", "Serpent Spine", "Redhorn Stonethresher", "Verdict", "The Unforged", "Talking Stick"],
    },
     "kinich": {
    "bis_weapon": "Fang of the Mountain King",
    "secondary_weapon": "Beacon of the Reed Sea",
    "f2p_weapon": ["Earth Shaker", "Prototype Archaic", "Ultimate Overlord's Mega Magic Sword", "Mailed Flower", "Forest Regalia", "Tidal Shadow", "Favonius Greatsword"],
    "niche_weapon": ["Wolf's Gravestone", "Serpent Spine", "Skyward Pride", "Verdict", "Redhorn Stonethresher", "The Unforged", "Talking Stick"],
    },
     "nahida": {
    "bis_weapon": "A Thousand Floating Dreams",
    "secondary_weapon": "Sunny Morning Sleep-In",
    "f2p_weapon": ["Magic Guide", "Sacrificial Fragments", "Mappa Mare", "Fruit of Fulfillment", "Prototype Amber", "Favonius Codex", "Ballad of the Boundless Blue"],
    "niche_weapon": ["Kagura's Verity", "Lost Prayer to the Sacred Winds", "Starcaller's Watch", "Skyward Atlas", "The Widsith", "Surf's Up", "Memory of Dust"],
    },
     "tighnari": {
    "bis_weapon": "Hunter's Path",
    "secondary_weapon": "The First Great Magic",
    "f2p_weapon": ["Slingshot", "Prototype Crescent", "Chain Breaker", "Song of Stillness", "Ibis Piercer", "Hamayumi", "Messenger"],
    "niche_weapon": ["Polar Star", "Skyward Harp", "Aqua Simulacra", "Amos' Bow", "Astral Vulture's Crimson Plumage", "Elegy for the End", "Thundering Pulse"],
    },
     "yaoyao": {
    "bis_weapon": "Favonius Lance",
    "secondary_weapon": "Dialogues of the Desert Sages",
    "f2p_weapon": ["Rightful Reward", "Kitain Cross Spear", "Black Tassel", "Prototype Starglitter", "Missive Windspear", "Moonpiercer", "Dragon's Bane"],
    "niche_weapon": ["Staff of Homa", "Engulfing Lightning", "Skyward Spine", "Calamity Queller", "Staff of the Scarlet Sands", "Lumidouce Elegy", "Vortex Vanquisher"],
    },
     "nefer": {
       "bis_weapon": "Reliquary of Truth",
       "secondary_weapon": "Nocturne's Curtain Call",
       "f2p_weapon": ["Blackmarrow Lantern", "The Widsith", "Mappa Mare", "Flowing Purity", "Ballad of the Boundless blue", "Fruit of Fulfillment", "Magic Guide", "Twin Nephrite"],
       "niche_weapon": ["A Thousand Floating Dreams", "Tome of the Eternal Flow", "Sunny Morning Sleep-In", "Starcaller's Watch", "Surf's Up", "Lost Prayer to the Sacred Winds", "Kagura's Verity", "Skyward Atlas", "Memory of Dust", "Cashflow Supervision"],
     },
  
     
# ==========================================================
# CRYO  
# ==========================================================
    "ayaka": {
    "bis_weapon": "Mistsplitter Reforged",
    "secondary_weapon": "Haran Geppaku Futsu",
    "f2p_weapon": ["Amenoma Kageuchi", "Finale of the Deep", "Fleuve Cendre Ferryman", "The Black Sword", "Harbinger of Dawn", "Sapwood Blade", "Skyrider Sword"],
    "niche_weapon": ["Absolution", "Primordial Jade Cutter", "Light of Foliar Incision", "Uraku Misugiri", "Skyward Blade", "Summit Shaper", "Freedom-Sworn"],
    },
     "charlotte": {
    "bis_weapon": "Favonius Codex",
    "secondary_weapon": "Prototype Amber",
    "f2p_weapon": ["Prototype Amber", "Fruit of Fulfillment", "Thrilling Tales of Dragon Slayers", "Ballad of the Boundless Blue", "Flowing Purity", "Magic Guide", "Favonius Codex"],
    "niche_weapon": ["Skyward Atlas", "Starcaller's Watch", "Sunny Morning Sleep-In", "Everlasting Moonglow", "Jadefall's Splendor", "Lost Prayer to the Sacred Winds", "Memory of Dust"],
    },
     "chongyun": {
    "bis_weapon": "Beacon of the Reed Sea",
    "secondary_weapon": "Wolf's Gravestone",
    "f2p_weapon": ["Prototype Archaic", "Tidal Shadow", "Ultimate Overlord's Mega Magic Sword", "Earth Shaker", "Mailed Flower", "Favonius Greatsword", "Sacrificial Greatsword"],
    "niche_weapon": ["Serpent Spine", "Skyward Pride", "Redhorn Stonethresher", "Verdict", "The Unforged", "Talking Stick", "Akuoumaru"],
    },
     "citlali": {
    "bis_weapon": "Starcaller's Watch",
    "secondary_weapon": "A Thousand Floating Dreams",
    "f2p_weapon": ["Sacrificial Fragments", "Mappa Mare", "Fruit of Fulfillment", "Thrilling Tales of Dragon Slayers", "Prototype Amber", "Magic Guide", "Favonius Codex"],
    "niche_weapon": ["Sunny Morning Sleep-In", "Lost Prayer to the Sacred Winds", "Skyward Atlas", "Surf's Up", "Kagura's Verity", "Memory of Dust", "Jadefall's Splendor"],
    },
     "dahlia": {
    "bis_weapon": "Favonius Sword",
    "secondary_weapon": "Freedom-Sworn",
    "f2p_weapon": ["Favonius Sword", "Sacrificial Sword", "Fleuve Cendre Ferryman", "Sapwood Blade", "Amenoma Kageuchi", "Skyrider Sword", "Harbinger of Dawn"],
    "niche_weapon": ["Skyward Blade", "Primordial Jade Cutter", "Key of Khaj-Nisut", "Absolution", "Mistsplitter Reforged", "Light of Foliar Incision", "Uraku Misugiri"],
    },
     "diona": {
    "bis_weapon": "Elegy for the End",
    "secondary_weapon": "Favonius Warbow",
    "f2p_weapon": ["Favonius Warbow", "Sacrificial Bow", "End of the Line", "Recurve Bow", "Messenger", "Prototype Crescent", "Fading Twilight"],
    "niche_weapon": ["Skyward Harp", "Polar Star", "The Stringless", "Aqua Simulacra", "Hunter's Path", "The First Great Magic", "Astral Vulture's Crimson Plumage"],
    },
     "escoffier": {
    "bis_weapon": "Symphonist of Scents",
    "secondary_weapon": "Staff of Homa",
    "f2p_weapon": ["Favonius Lance", "Rightful Reward", "Dialogues of the Desert Sages", "Missive Windspear", "Prototype Starglitter", "Black Tassel", "Kitain Cross Spear"],
    "niche_weapon": ["Lumidouce Elegy", "Calamity Queller", "Engulfing Lightning", "Skyward Spine", "Staff of the Scarlet Sands", "Vortex Vanquisher", "Primordial Jade Winged-Spear"],
    },
     "eula": {
    "bis_weapon": "Song of Broken Pines",
    "secondary_weapon": "Beacon of the Reed Sea",
    "f2p_weapon": ["Tidal Shadow", "Prototype Archaic", "Snow-Tombed Starsilver", "Ultimate Overlord's Mega Magic Sword", "Earth Shaker", "Mailed Flower", "Luxurious Sea-Lord"],
    "niche_weapon": ["Wolf's Gravestone", "Redhorn Stonethresher", "Skyward Pride", "Verdict", "The Unforged", "Serpent Spine", "Talking Stick"],
    },
     "freminet": {
    "bis_weapon": "Beacon of the Reed Sea",
    "secondary_weapon": "Serpent Spine",
    "f2p_weapon": ["Prototype Archaic", "Tidal Shadow", "Snow-Tombed Starsilver", "Ultimate Overlord's Mega Magic Sword", "Earth Shaker", "Mailed Flower", "Favonius Greatsword"],
    "niche_weapon": ["Wolf's Gravestone", "Redhorn Stonethresher", "Skyward Pride", "Verdict", "The Unforged", "Talking Stick", "Akuoumaru"],
    },
     "ganyu": {
    "bis_weapon": "Hunter's Path",
    "secondary_weapon": "The First Great Magic",
    "f2p_weapon": ["Prototype Crescent", "Hamayumi", "Song of Stillness", "Chain Breaker", "Slingshot", "Messenger", "Ibis Piercer"],
    "niche_weapon": ["Aqua Simulacra", "Polar Star", "Skyward Harp", "Amos' Bow", "Astral Vulture's Crimson Plumage", "Thundering Pulse", "Elegy for the End"],
    },
     "kaeya": {
    "bis_weapon": "Mistsplitter Reforged",
    "secondary_weapon": "Primordial Jade Cutter",
    "f2p_weapon": ["Amenoma Kageuchi", "Finale of the Deep", "Harbinger of Dawn", "Fleuve Cendre Ferryman", "Sapwood Blade", "Skyrider Sword", "Dark Iron Sword"],
    "niche_weapon": ["Light of Foliar Incision", "Absolution", "Uraku Misugiri", "Skyward Blade", "Haran Geppaku Futsu", "Freedom-Sworn", "Key of Khaj-Nisut"],
    },
     "layla": {
    "bis_weapon": "Key of Khaj-Nisut",
    "secondary_weapon": "Freedom-Sworn",
    "f2p_weapon": ["Favonius Sword", "Sacrificial Sword", "Fleuve Cendre Ferryman", "Sapwood Blade", "Amenoma Kageuchi", "Harbinger of Dawn", "Skyrider Sword"],
    "niche_weapon": ["Skyward Blade", "Primordial Jade Cutter", "Absolution", "Mistsplitter Reforged", "Light of Foliar Incision", "Uraku Misugiri", "Summit Shaper"],
    },
     "mika": {
    "bis_weapon": "Favonius Lance",
    "secondary_weapon": "Dialogues of the Desert Sages",
    "f2p_weapon": ["Rightful Reward", "Prototype Starglitter", "Black Tassel", "Missive Windspear", "Kitain Cross Spear", "Moonpiercer", "Dragon's Bane"],
    "niche_weapon": ["Skyward Spine", "Engulfing Lightning", "Staff of Homa", "Calamity Queller", "Lumidouce Elegy", "Vortex Vanquisher", "Staff of the Scarlet Sands"],
    },
     "qiqi": {
    "bis_weapon": "Skyward Blade",
    "secondary_weapon": "Favonius Sword",
    "f2p_weapon": ["Amenoma Kageuchi", "Sacrificial Sword", "Fleuve Cendre Ferryman", "Sapwood Blade", "Skyrider Sword", "Harbinger of Dawn", "Prototype Rancour"],
    "niche_weapon": ["Freedom-Sworn", "Key of Khaj-Nisut", "Primordial Jade Cutter", "Mistsplitter Reforged", "Absolution", "Light of Foliar Incision", "Uraku Misugiri"],
    },
     "rosaria": {
    "bis_weapon": "Staff of Homa",
    "secondary_weapon": "Calamity Queller",
    "f2p_weapon": ["Favonius Lance", "Missive Windspear", "Prototype Starglitter", "Rightful Reward", "Dragon's Bane", "Black Tassel", "Kitain Cross Spear"],
    "niche_weapon": ["Primordial Jade Winged-Spear", "Lumidouce Elegy", "Skyward Spine", "Engulfing Lightning", "Staff of the Scarlet Sands", "Vortex Vanquisher", "Deathmatch"],
    },
     "shenhe": {
    "bis_weapon": "Calamity Queller",
    "secondary_weapon": "Engulfing Lightning",
    "f2p_weapon": ["Favonius Lance", "Rightful Reward", "Prototype Starglitter", "Missive Windspear", "Dialogues of the Desert Sages", "Black Tassel", "Kitain Cross Spear"],
    "niche_weapon": ["Skyward Spine", "Staff of Homa", "Lumidouce Elegy", "Primordial Jade Winged-Spear", "Vortex Vanquisher", "Staff of the Scarlet Sands", "Deathmatch"],
    },
     "skirk": {
    "bis_weapon": "Azurelight",
    "secondary_weapon": "Mistsplitter Reforged",
    "f2p_weapon": ["Finale of the Deep", "Amenoma Kageuchi", "Harbinger of Dawn", "Fleuve Cendre Ferryman", "Sapwood Blade", "Skyrider Sword", "The Black Sword"],
    "niche_weapon": ["Primordial Jade Cutter", "Absolution", "Light of Foliar Incision", "Uraku Misugiri", "Haran Geppaku Futsu", "Skyward Blade", "Freedom-Sworn"],
    },
     "wriothesley": {
    "bis_weapon": "Cashflow Supervision",
    "secondary_weapon": "Lost Prayer to the Sacred Winds",
    "f2p_weapon": ["Flowing Purity", "The Widsith", "Ballad of the Boundless Blue", "Mappa Mare", "Favonius Codex", "Magic Guide", "Fruit of Fulfillment"],
    "niche_weapon": ["Skyward Atlas", "Kagura's Verity", "Starcaller's Watch", "Sunny Morning Sleep-In", "Memory of Dust", "Surf's Up", "Tulaytullah's Remembrance"],
    },
     "sandrone": {
     "bis_weapon": "A Teaspoon of Transcendence",
"secondary_weapon": "A Thousand Blazing Suns",
"f2p_weapon": ["Tidal Shadow", "Mailed Flower", "Ultimate Overlord's Mega Magic Sword", "Prototype Archaic", "Earth Shaker", "Blackcliff Slasher", "Serpent Spine"],
"niche_weapon": ["Verdict", "Beacon of the Reed Sea", "Wolf's Gravestone", "Redhorn Stonethresher", "Skyward Pride", "The Unforged", "Talking Stick", "Gest of the Mighty Wolf"],
     },
# ==========================================================
# GEO
# ==========================================================
    "albedo": {
    "bis_weapon": "Peak Patrol Song",
    "secondary_weapon": "Cinnabar Spindle",
    "f2p_weapon": ["Harbinger of Dawn", "Finale of the Deep", "Amenoma Kageuchi", "Fleuve Cendre Ferryman", "Sapwood Blade", "Skyrider Sword", "Prototype Rancour"],
    "niche_weapon": ["Uraku Misugiri", "Primordial Jade Cutter", "Mistsplitter Reforged", "Absolution", "Light of Foliar Incision", "Skyward Blade", "Freedom-Sworn"],
    },
     "chiori": {
    "bis_weapon": "Uraku Misugiri",
    "secondary_weapon": "Primordial Jade Cutter",
    "f2p_weapon": ["Harbinger of Dawn", "Finale of the Deep", "Amenoma Kageuchi", "Fleuve Cendre Ferryman", "Sapwood Blade", "Skyrider Sword", "Prototype Rancour"],
    "niche_weapon": ["Peak Patrol Song", "Mistsplitter Reforged", "Absolution", "Light of Foliar Incision", "Skyward Blade", "Freedom-Sworn", "Haran Geppaku Futsu"],
    },
     "gorou": {
    "bis_weapon": "Elegy for the End",
    "secondary_weapon": "Favonius Warbow",
    "f2p_weapon": ["Favonius Warbow", "Sacrificial Bow", "End of the Line", "Fading Twilight", "Prototype Crescent", "Messenger", "Recurve Bow"],
    "niche_weapon": ["Polar Star", "Skyward Harp", "The Stringless", "Aqua Simulacra", "Hunter's Path", "The First Great Magic", "Astral Vulture's Crimson Plumage"],
    },
     "itto": {
    "bis_weapon": "Redhorn Stonethresher",
    "secondary_weapon": "Beacon of the Reed Sea",
    "f2p_weapon": ["Whiteblind", "Ultimate Overlord's Mega Magic Sword", "Earth Shaker", "Prototype Archaic", "Tidal Shadow", "Mailed Flower", "Favonius Greatsword"],
    "niche_weapon": ["Serpent Spine", "Wolf's Gravestone", "Verdict", "Skyward Pride", "The Unforged", "Talking Stick", "Akuoumaru"],
    },
     "kachina": {
    "bis_weapon": "Mountain-Bracing Bolt",
    "secondary_weapon": "Favonius Lance",
    "f2p_weapon": ["Rightful Reward", "Prototype Starglitter", "Dialogues of the Desert Sages", "Black Tassel", "Missive Windspear", "Moonpiercer", "Kitain Cross Spear"],
    "niche_weapon": ["Engulfing Lightning", "Skyward Spine", "Staff of Homa", "Calamity Queller", "Lumidouce Elegy", "Staff of the Scarlet Sands", "Vortex Vanquisher"],
    },
     "navia": {
    "bis_weapon": "Verdict",
    "secondary_weapon": "Beacon of the Reed Sea",
    "f2p_weapon": ["Ultimate Overlord's Mega Magic Sword", "Tidal Shadow", "Prototype Archaic", "Earth Shaker", "Mailed Flower", "Favonius Greatsword", "Whiteblind"],
    "niche_weapon": ["Wolf's Gravestone", "Redhorn Stonethresher", "Skyward Pride", "The Unforged", "Serpent Spine", "Talking Stick", "Akuoumaru"],
    },
     "ningguang": {
    "bis_weapon": "Lost Prayer to the Sacred Winds",
    "secondary_weapon": "Sunny Morning Sleep-In",
    "f2p_weapon": ["The Widsith", "Flowing Purity", "Ballad of the Boundless Blue", "Mappa Mare", "Favonius Codex", "Magic Guide", "Fruit of Fulfillment"],
    "niche_weapon": ["Cashflow Supervision", "Skyward Atlas", "Kagura's Verity", "Memory of Dust", "Starcaller's Watch", "Surf's Up", "Tulaytullah's Remembrance"],
    },
     "noelle": {
    "bis_weapon": "Redhorn Stonethresher",
    "secondary_weapon": "Serpent Spine",
    "f2p_weapon": ["Whiteblind", "Prototype Archaic", "Ultimate Overlord's Mega Magic Sword", "Earth Shaker", "Tidal Shadow", "Mailed Flower", "Favonius Greatsword"],
    "niche_weapon": ["Beacon of the Reed Sea", "Wolf's Gravestone", "Verdict", "Skyward Pride", "The Unforged", "Talking Stick", "Akuoumaru"],
    },
     "xilonen": {
    "bis_weapon": "Peak Patrol Song",
    "secondary_weapon": "Freedom-Sworn",
    "f2p_weapon": ["Favonius Sword", "Fleuve Cendre Ferryman", "Sapwood Blade", "Amenoma Kageuchi", "Skyrider Sword", "Harbinger of Dawn", "Finale of the Deep"],
    "niche_weapon": ["Uraku Misugiri", "Primordial Jade Cutter", "Skyward Blade", "Absolution", "Mistsplitter Reforged", "Light of Foliar Incision", "Key of Khaj-Nisut"],
    },
     "yunjin": {
    "bis_weapon": "Engulfing Lightning",
    "secondary_weapon": "Favonius Lance",
    "f2p_weapon": ["Prototype Starglitter", "Rightful Reward", "Dialogues of the Desert Sages", "Missive Windspear", "Black Tassel", "Kitain Cross Spear", "Moonpiercer"],
    "niche_weapon": ["Skyward Spine", "Staff of Homa", "Calamity Queller", "Staff of the Scarlet Sands", "Lumidouce Elegy", "Primordial Jade Winged-Spear", "Vortex Vanquisher"],
    },
      "zhongli": {
    "bis_weapon": "Staff of Homa",
    "secondary_weapon": "Favonius Lance",
    "f2p_weapon": ["Black Tassel", "Rightful Reward", "Prototype Starglitter", "Dialogues of the Desert Sages", "Missive Windspear", "Kitain Cross Spear", "Moonpiercer"],
    "niche_weapon": ["Engulfing Lightning", "Calamity Queller", "Skyward Spine", "Staff of the Scarlet Sands", "Lumidouce Elegy", "Primordial Jade Winged-Spear", "Vortex Vanquisher"],
    },
    "aloy": {
    "bis_weapon": "Thundering Pulse",
    "secondary_weapon": "Polar Star",
    "f2p_weapon": ["The Stringless", "Favonius Warbow", "Sacrificial Bow", "Slingshot"],
    "niche_weapon": ["Skyward Harp", "Aqua Simulacra", "Hunter's Path", "The First Great Magic"],
    },
    "durin": {
    "bis_weapon": "Athame Artis",
    "secondary_weapon": "Mistsplitter Reforged",
    "f2p_weapon": ["Favonius Sword", "Fleuve Cendre Ferryman", "Sapwood Blade", "Harbinger of Dawn"],
    "niche_weapon": ["Primordial Jade Cutter", "Absolution", "Light of Foliar Incision", "Skyward Blade", "Freedom-Sworn"],
    },
    "jahoda": {
    "bis_weapon": "Elegy for the End",
    "secondary_weapon": "Favonius Warbow",
    "f2p_weapon": ["Favonius Warbow", "Sacrificial Bow", "End of the Line", "Fading Twilight", "Slingshot"],
    "niche_weapon": ["Skyward Harp", "Polar Star", "Aqua Simulacra", "The Stringless"],
    },
}
