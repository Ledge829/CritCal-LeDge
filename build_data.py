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
        "niche_artifact_sets": ["Flower of Paradise Lost", "Gilded Dreams"],
        "team_archetype": "Main DPS -- Vaporize / Melt / Plunge Hypercarry, pairs with Xianyun",
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

# ==========================================================
# HYDRO
# ==========================================================

    "barbara": {
        "bis_artifact_set": "Ocean-Hued Clam",
        "secondary_artifact_set": "Song of Days Past",
        "niche_artifact_sets": ["Maiden Beloved"],
        "team_archetype": "Bloom/Hyperbloom-enabling healer, or general team-wide sustain in any comp",
    },
    "candace": {
        "bis_artifact_set": "Scroll of the Hero of Cinder City",
        "secondary_artifact_set": "Noblesse Oblige",
        "niche_artifact_sets": ["Emblem of Severed Fate"],
        "team_archetype": "Hydro application enabler for Bloom/Electro-Charged/Vaporize; secondary ATK buffer",
    },
    "childe": {
        "bis_artifact_set": "Nymph's Dream",
        "secondary_artifact_set": "Heart of Depth",
        "niche_artifact_sets": ["Marechaussee Hunter"],
        "team_archetype": "on-field Riptide DPS -- Melt/Vaporize bow rotations, Foul Legacy: Raging Tide combo",
    },
    "furina": {
        "bis_artifact_set": "Golden Troupe",
        "secondary_artifact_set": "Tenacity of the Millelith",
        "niche_artifact_sets": [],
        "team_archetype": "pairs with a team-wide healer (Kokomi/Baizhu/Charlotte); powers National, Vaporize, Freeze comps",
    },
    "kokomi": {
        "bis_artifact_set": "Ocean-Hued Clam",
        "secondary_artifact_set": "Tenacity of the Millelith",
        "niche_artifact_sets": ["Song of Days Past", "Maiden Beloved"],
        "team_archetype": "Healing Support / Hydro Driver",
    },
    "mona": {
        "bis_artifact_set": "Noblesse Oblige",
        "secondary_artifact_set": "Emblem of Severed Fate",
        "niche_artifact_sets": ["Scroll of the Hero of Cinder City", "Instructor's", "Tenacity of the Millelith"],
        "team_archetype": "Burst Support / Hydro Buffer",
    },
    "mualani": {
        "bis_artifact_set": "Obsidian Codex",
        "secondary_artifact_set": "Heart of Depth",
        "niche_artifact_sets": ["Marechaussee Hunter", "Nymph's Dream", "Gilded Dreams"],
        "team_archetype": "on-field Vaporize Hypercarry -- pairs with a Pyro applier and Natlan Nightsoul teammates",
    },
    "neuvillette": {
        "bis_artifact_set": "Marechaussee Hunter",
        "secondary_artifact_set": "Heart of Depth",
        "niche_artifact_sets": ["Nymph's Dream", "Obsidian Codex", "Wanderer's Troupe"],
        "team_archetype": "Charged Attack Hypercarry",
    },
    "nilou": {
        "bis_artifact_set": "Flower of Paradise Lost",
        "secondary_artifact_set": "Gilded Dreams",
        "niche_artifact_sets": ["Deepwood Memories", "Tenacity of the Millelith", "Vourukasha's Glow"],
        "team_archetype": "Dendro+Hydro-only comps for Bountiful Cores -- Superbloom/Bloom-focused",
    },
    "sigewinne": {
        "bis_artifact_set": "Song of Days Past",
        "secondary_artifact_set": "Ocean-Hued Clam",
        "niche_artifact_sets": ["Maiden Beloved", "Emblem of Severed Fate", "Noblesse Oblige"],
        "team_archetype": "Furina-centric healer/buffer -- boosts off-field Skill DMG for the team",
    },
    "xingqiu": {
        "bis_artifact_set": "Emblem of Severed Fate",
        "secondary_artifact_set": "Noblesse Oblige",
        "niche_artifact_sets": ["Heart of Depth", "Nymph's Dream", "Gilded Dreams"],
        "team_archetype": "damage reduction plus off-field application -- National, Vaporize, Freeze near-universal support",
    },
    "yelan": {
        "bis_artifact_set": "Emblem of Severed Fate",
        "secondary_artifact_set": "Noblesse Oblige",
        "niche_artifact_sets": ["Golden Troupe", "Heart of Depth", "Nymph's Dream"],
        "team_archetype": "off-field Sub-DPS -- National, Vaporize, Taser near-universal support",
    },

# ==========================================================
# ANEMO
# ==========================================================

    "chasca": {
        "bis_artifact_set": "Obsidian Codex",
        "secondary_artifact_set": "Viridescent Venerer",
        "niche_artifact_sets": ["Golden Troupe", "Marechaussee Hunter", "Desert Pavilion Chronicle"],
        "team_archetype": "on-field DPS via Nightsoul Burst plunges -- pairs with a Nightsoul battery like Mavuika/Ororon",
    },
    "faruzan": {
        "bis_artifact_set": "Scroll of the Hero of Cinder City",
        "secondary_artifact_set": "Viridescent Venerer",
        "niche_artifact_sets": ["Noblesse Oblige", "Emblem of Severed Fate", "Tenacity of the Millelith"],
        "team_archetype": "provides team-wide CRIT DMG via VV/EM support -- pairs with a Swirl DPS",
    },
    "heizou": {
        "bis_artifact_set": "Viridescent Venerer",
        "secondary_artifact_set": "Desert Pavilion Chronicle",
        "niche_artifact_sets": ["Marechaussee Hunter", "Gilded Dreams", "Shimenawa's Reminiscence"],
        "team_archetype": "Normal-Attack-scaling catalyst DPS -- Swirl/EM reaction teams",
    },
    "jean": {
        "bis_artifact_set": "Viridescent Venerer",
        "secondary_artifact_set": "Noblesse Oblige",
        "niche_artifact_sets": ["Ocean-Hued Clam", "Song of Days Past", "Emblem of Severed Fate"],
        "team_archetype": "AoE healing plus Anemo application -- flexible in nearly any team comp",
    },
    "kazuha": {
        "bis_artifact_set": "Viridescent Venerer",
        "secondary_artifact_set": "Scroll of the Hero of Cinder City",
        "niche_artifact_sets": ["Instructor's", "Noblesse Oblige", "Gilded Dreams"],
        "team_archetype": "near-universal EM/DMG buffer -- National, Freeze, Hyperbloom, Taser support",
    },
    "lanyan": {
        "bis_artifact_set": "Viridescent Venerer",
        "secondary_artifact_set": "Scroll of the Hero of Cinder City",
        "niche_artifact_sets": ["Noblesse Oblige", "Song of Days Past", "Ocean-Hued Clam"],
        "team_archetype": "shield uptime plus Anemo application -- flexible support pick",
    },
    "lynette": {
        "bis_artifact_set": "Viridescent Venerer",
        "secondary_artifact_set": "Golden Troupe",
        "niche_artifact_sets": ["Noblesse Oblige", "Emblem of Severed Fate", "Desert Pavilion Chronicle"],
        "team_archetype": "enables quick-swap combos and Swirl reactions -- pairs well with Lyney",
    },
    "sayu": {
        "bis_artifact_set": "Viridescent Venerer",
        "secondary_artifact_set": "Ocean-Hued Clam",
        "niche_artifact_sets": ["Song of Days Past", "Noblesse Oblige", "Maiden Beloved"],
        "team_archetype": "budget healer with Swirl utility -- flexible F2P-friendly support",
    },
    "sucrose": {
        "bis_artifact_set": "Viridescent Venerer",
        "secondary_artifact_set": "Scroll of the Hero of Cinder City",
        "niche_artifact_sets": ["Instructor's", "Gilded Dreams", "Noblesse Oblige"],
        "team_archetype": "team-wide EM buff via Swirl -- near-universal reaction-team support",
    },
    "venti": {
        "bis_artifact_set": "Viridescent Venerer",
        "secondary_artifact_set": "Scroll of the Hero of Cinder City",
        "niche_artifact_sets": ["Noblesse Oblige", "Emblem of Severed Fate", "Gilded Dreams"],
        "team_archetype": "grouping plus Swirl application -- strong in AoE and reaction-heavy teams",
    },
    "wanderer": {
        "bis_artifact_set": "Desert Pavilion Chronicle",
        "secondary_artifact_set": "Marechaussee Hunter",
        "niche_artifact_sets": ["Shimenawa's Reminiscence", "Echoes of an Offering", "Viridescent Venerer"],
        "team_archetype": "on-field Normal Attack DPS -- flexible Freeze/Vaporize/Melt/Taser teams",
    },
    "xianyun": {
        "bis_artifact_set": "Viridescent Venerer",
        "secondary_artifact_set": "Song of Days Past",
        "niche_artifact_sets": ["Noblesse Oblige", "Ocean-Hued Clam", "Scroll of the Hero of Cinder City"],
        "team_archetype": "healing plus ATK buff via plunge attacks -- pairs with plunge-attack DPS like Gaming",
    },

}


WEAPON_TIERS: Dict[str, Dict[str, Any]] = {

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
        "f2p_weapon": ["Prototype Archaic", "Dragon's Bane"],
        "niche_weapon": ["Mailed Flower", "White Tassel"],
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

# ==========================================================
# HYDRO
# ==========================================================

    "barbara": {
        "bis_weapon": "Thrilling Tales of Dragon Slayers",
        "secondary_weapon": "Prototype Amber",
        "f2p_weapon": ["Favonius Codex"],
        "niche_weapon": ["Sacrificial Fragments"],
    },
    "candace": {
        "bis_weapon": "Favonius Lance",
        "secondary_weapon": "Dialogues of the Desert Sages",
        "f2p_weapon": ["Rightful Reward"],
        "niche_weapon": ["Black Tassel"],
    },
    "childe": {
        "bis_weapon": "Polar Star",
        "secondary_weapon": "Aqua Simulacra",
        "f2p_weapon": ["The Viridescent Hunt"],
        "niche_weapon": ["Hamayumi"],
    },
    "furina": {
        "bis_weapon": "Splendor of Tranquil Waters",
        "secondary_weapon": "Primordial Jade Cutter",
        "f2p_weapon": ["Festering Desire", "Favonius Sword", "Fleuve Cendre Ferryman"],
        "niche_weapon": ["Wolf-Fang", "Key of Khaj-Nisut"],
    },
    "kokomi": {
        "bis_weapon": "Everlasting Moonglow",
        "secondary_weapon": "Prototype Amber",
        "f2p_weapon": ["Thrilling Tales of Dragon Slayers", "Favonius Codex"],
        "niche_weapon": ["Hakushin Ring"],
    },
    "mona": {
        "bis_weapon": "A Thousand Floating Dreams",
        "secondary_weapon": "Skyward Atlas",
        "f2p_weapon": ["Prototype Amber", "Favonius Codex", "The Widsith", "Thrilling Tales of Dragon Slayers"],
        "niche_weapon": [],
    },
    "mualani": {
        "bis_weapon": "Surf's Up",
        "secondary_weapon": "Tome of the Eternal Flow",
        "f2p_weapon": ["Ring of Yaxche", "Prototype Amber"],
        "niche_weapon": ["Cashflow Supervision", "Lost Prayer to the Sacred Winds", "Sacrificial Jade"],
    },
    "neuvillette": {
        "bis_weapon": "Tome of the Eternal Flow",
        "secondary_weapon": "Sacrificial Jade",
        "f2p_weapon": ["Prototype Amber", "Ring of Yaxche"],
        "niche_weapon": ["Cashflow Supervision", "Lost Prayer to the Sacred Winds", "Jadefall's Splendor"],
    },
    "nilou": {
        "bis_weapon": "Key of Khaj-Nisut",
        "secondary_weapon": "Freedom-Sworn",
        "f2p_weapon": ["Iron Sting", "Sapwood Blade"],
        "niche_weapon": ["Xiphos' Moonlight", "Primordial Jade Cutter", "Favonius Sword"],
    },
    "sigewinne": {
       "bis_weapon": "Silvershower Heartstrings",
        "secondary_weapon": "Aqua Simulacra",
        "f2p_weapon": ["Sequence of Solitude", "Recurve Bow", "Messenger"],
        "niche_weapon": ["Favonius Warbow", "Elegy for the End"],
    },
    "xingqiu": {
        "bis_weapon": "Mistsplitter Reforged",
        "secondary_weapon": "Sacrificial Sword",
        "f2p_weapon": ["Favonius Sword", "Fleuve Cendre Ferryman"],
        "niche_weapon": ["Light of Foliar Incision", "Summit Shaper", "Haran Geppaku Futsu"],
    },
    "yelan": {
        "bis_weapon": "Aqua Simulacra",
        "secondary_weapon": "Elegy for the End",
        "f2p_weapon": ["Favonius Warbow", "Fading Twilight", "Slingshot"],
        "niche_weapon": ["Silvershower Heartstrings", "Hunter's Path", "Mouun's Moon"],
    },

# ==========================================================
# ANEMO
# ==========================================================

    "chasca": {
        "bis_weapon": "Astral Vulture's Crimson Plumage",
        "secondary_weapon": "The First Great Magic",
        "f2p_weapon": ["Chain Breaker", "Scion of the Blazing Sun", "Song of Stillness"],
        "niche_weapon": ["Aqua Simulacra", "Polar Star", "Skyward Harp"],
    },
    "faruzan": {
        "bis_weapon": "Elegy for the End",
        "secondary_weapon": "Favonius Warbow",
        "f2p_weapon": ["Favonius Warbow", "End of the Line"],
        "niche_weapon": ["End of the Line", "Mouun's Moon", "Skyward Harp"],
    },
    "heizou": {
        "bis_weapon": "Cashflow Supervision",
        "secondary_weapon": "Tulaytullah's Remembrance",
        "f2p_weapon": ["Flowing Purity", "Mappa Mare", "The Widsith"],
        "niche_weapon": ["Lost Prayer to the Sacred Winds", "Skyward Atlas", "Kagura's Verity"],
    },
    "jean": {
        "bis_weapon": "Freedom-Sworn",
        "secondary_weapon": "Skyward Blade",
        "f2p_weapon": ["Amenoma Kageuchi", "Sapwood Blade", "Fleuve Cendre Ferryman"],
        "niche_weapon": ["Favonius Sword", "Primordial Jade Cutter", "Key of Khaj-Nisut"],
    },
    "kazuha": {
        "bis_weapon": "Freedom-Sworn",
        "secondary_weapon": "Xiphos' Moonlight",
        "f2p_weapon": ["Iron Sting", "Dark Iron Sword", "Sapwood Blade"],
        "niche_weapon": ["Favonius Sword", "Key of Khaj-Nisut", "Primordial Jade Cutter"],
    },
    "lanyan": {
        "bis_weapon": "Sunny Morning Sleep-In",
        "secondary_weapon": "Thrilling Tales of Dragon Slayers",
        "f2p_weapon": ["Prototype Amber", "Fruit of Fulfillment", "Mappa Mare"],
        "niche_weapon": ["A Thousand Floating Dreams", "Favonius Codex"],
    },
    "lynette": {
        "bis_weapon": "Freedom-Sworn",
        "secondary_weapon": "Favonius Sword",
        "f2p_weapon": ["Fleuve Cendre Ferryman", "Sapwood Blade", "Amenoma Kageuchi"],
        "niche_weapon": ["Skyward Blade", "Primordial Jade Cutter", "Key of Khaj-Nisut"],
    },
    "sayu": {
        "bis_weapon": "Wolf's Gravestone",
        "secondary_weapon": "Skyward Pride",
        "f2p_weapon": ["Katsuragikiri Nagamasa", "Forest Regalia", "Tidal Shadows"],
        "niche_weapon": ["Favonius Greatsword", "Beacon of the Reed Sea", "Rainslasher"],
    },
    "sucrose": {
        "bis_weapon": "A Thousand Floating Dreams",
        "secondary_weapon": "Sacrificial Fragments",
        "f2p_weapon": ["Magic Guide", "Mappa Mare", "Fruit of Fulfillment"],
        "niche_weapon": ["Sunny Morning Sleep-In", "Wandering Evenstar", "Hakushin Ring"],
    },
    "venti": {
        "bis_weapon": "Elegy for the End",
        "secondary_weapon": "The First Great Magic",
        "f2p_weapon": ["Stringless", "End of the Line", "Fading Twilight"],
        "niche_weapon": ["Polar Star", "Aqua Simulacra", "Skyward Harp"],
    },
    "wanderer": {
        "bis_weapon": "Tulaytullah's Remembrance",
        "secondary_weapon": "Cashflow Supervision",
        "f2p_weapon": ["Flowing Purity", "Frostbearer", "Mappa Mare"],
        "niche_weapon": ["Lost Prayer to the Sacred Winds", "Skyward Atlas", "Memory of Dust"],
    },
    "xianyun": {
        "bis_weapon": "Crane's Echoing Call",
        "secondary_weapon": "Skyward Atlas",
        "f2p_weapon": ["Oathsworn Eye", "Prototype Amber", "Favonius Codex"],
        "niche_weapon": ["A Thousand Floating Dreams", "Memory of Dust", "Cashflow Supervision"],
    },

}
