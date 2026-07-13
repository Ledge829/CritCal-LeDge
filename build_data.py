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
    "niche_artifact_sets": ["Instructor", "Song of Days Past", "Maiden Beloved", "Ocean-Hued Clam", "Deepwood Memories", "Tenacity of the Millelith"],
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
    "niche_artifact_sets": ["Deepwood Memories", "Noblesse Oblige", "Tenacity of the Millelith", "Instructor", "2pc HP% + 2pc Emblem of Severed Fate", "Scroll of the Hero of Cinder City"],
    "team_archetype": "Burgeon Trigger / Shield Support / Burning Support",
    },
    "xiangling": {
    "bis_artifact_set": "Emblem of Severed Fate",
    "secondary_artifact_set": "Crimson Witch of Flames",
    "niche_artifact_sets": ["Scroll of the Hero of Cinder City", "Gilded Dreams", "Lavawalker", "Instructor", "Noblesse Oblige", "Unfinished Reverie"],
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
    "niche_artifact_sets": ["Maiden Beloved", "Tenacity of the Millelith", "Instructor", "Deepwood Memories", "Noblesse Oblige"],
    "team_archetype": "Healer / Bloom Driver / Hydro Support",
    },
    "candace": {
    "bis_artifact_set": "Scroll of the Hero of Cinder City",
    "secondary_artifact_set": "Noblesse Oblige",
    "niche_artifact_sets": ["Emblem of Severed Fate", "Tenacity of the Millelith", "Instructor", "Scroll of the Hero of Cinder City", "Vourukasha's Glow"],
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
    "niche_artifact_sets": ["Song of Days Past", "Deepwood Memories", "Instructor", "Maiden Beloved", "Heart of Depth", "Nymph's Dream"],
    "team_archetype": "Healer / Bloom Driver / Freeze Support / Mono Hydro Driver",
    },
    "mona": {
    "bis_artifact_set": "Emblem of Severed Fate",
    "secondary_artifact_set": "Noblesse Oblige",
    "niche_artifact_sets": ["Golden Troupe", "Heart of Depth", "Nymph's Dream", "Instructor", "Scroll of the Hero of Cinder City", "Tenacity of the Millelith"],
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
    "niche_artifact_sets": ["Gilded Dreams", "Tenacity of the Millelith", "Deepwood Memories", "Heart of Depth", "Nymph's Dream", "Instructor"],
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
    "niche_artifact_sets": ["Heart of Depth", "Nymph's Dream", "Golden Troupe", "Scroll of the Hero of Cinder City", "Instructor", "Tenacity of the Millelith"],
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
    "niche_artifact_sets": ["Viridescent Venerer", "Emblem of Severed Fate", "Tenacity of the Millelith", "Instructor", "The Exile", "Scroll of the Hero of Cinder City"],
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
    "niche_artifact_sets": ["Noblesse Oblige", "Instructor", "Gilded Dreams", "Flower of Paradise Lost", "Emblem of Severed Fate", "Tenacity of the Millelith"],
    "team_archetype": "Swirl Support / Elemental DMG Buffer / Crowd Control / Quickswap",
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
    "f2p_weapon": ["Festering Desire", "Fleuve Cendre Ferryman", "Favonius Sword", "Sacrificial Sword", "Wolf-Fang", "The Dockhand's Assistant", "Ferryman"],
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
