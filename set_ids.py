"""
Static mapping from Enka artifact setId → set name.

Artifact sets in Enka's response include a numeric setId.
When the nameTextMapHash isn't in their published loc.json,
we resolve the set name from this mapping instead.
"""

SET_IDS: dict[int, str] = {
    # Early game sets
    15001: "Resolution of Sojourner",
    15002: "Brave Heart",
    15003: "Defender's Will",
    15004: "Tiny Miracle",
    15005: "Berserker",
    15007: "Adventurer",
    15008: "Lucky Dog",
    15009: "Traveling Doctor",
    15010: "Gambler",
    15011: "Scholar",
    15012: "Martial Artist",
    15013: "Instructor",
    15014: "The Exile",

    # 5-star domain sets
    15015: "Gladiator's Finale",
    15016: "Wanderer's Troupe",
    15017: "Noblesse Oblige",
    15018: "Bloodstained Chivalry",
    15019: "Maiden Beloved",
    15020: "Archaic Petra",
    15021: "Retracing Bolide",

    # Elemental domain sets
    15023: "Crimson Witch of Flames",
    15024: "Lavawalker",
    15025: "Thundersoother",
    15026: "Thundering Fury",
    15027: "Viridescent Venerer",
    15028: "Blizzard Strayer",
    15029: "Heart of Depth",

    # Inazuma/early 2.x sets
    15030: "Tenacity of the Millelith",
    15031: "Pale Flame",
    15032: "Shimenawa's Reminiscence",
    15033: "Emblem of Severed Fate",
    15034: "Husk of Opulent Dreams",
    15035: "Ocean-Hued Clam",
    15036: "Vermillion Hereafter",
    15037: "Echoes of an Offering",

    # Sumeru sets
    15038: "Deepwood Memories",
    15039: "Gilded Dreams",
    15040: "Desert Pavilion Chronicle",
    15041: "Flower of Paradise Lost",
    15042: "Nymph's Dream",
    15043: "Vourukasha's Glow",

    # Fontaine sets
    15044: "Marechaussee Hunter",
    15045: "Golden Troupe",
    15046: "Song of Days Past",
    15047: "Nighttime Whispers in the Echoing Woods",
    15048: "Fragment of Harmonic Whimsy",
    15049: "Unfinished Reverie",

    # Natlan sets
    15050: "Scroll of the Hero of Cinder City",
    15051: "Obsidian Codex",
    15052: "Finale of the Deep (Artifact)",
    15053: "Long Night's Oath",
    15054: "Disenchantment in Deep Shadow",
    15055: "A Day Carved from Rising Winds",
    15056: "Silken Moon's Serenade",
    15057: "Night of the Sky's Unveiling",
    15058: "Finale of the Deep Galleries",
}
