"""
Static mapping from Enka weapon itemId → weapon name.

Enka returns a numeric itemId for each weapon. When the name hash
isn't in their loc.json, we look it up here instead. This covers
weapons whose hash is missing from Enka's published data.

Populated incrementally — add new entries as they're discovered.
"""

WEAPON_IDS: dict[int, str] = {
    # Swords
    11513: "Splendor of Tranquil Waters",
    11511: "Key of Khaj-Nisut",
    11416: "Kagotsurube Isshin",
    11414: "Amenoma Kageuchi",
    11422: "Toukabou Shigure",
    11502: "Skyward Blade",
    # Polearms
    13501: "Staff of Homa",
    13416: "The Catch",
    # Bows
    15508: "Aqua Simulacra",
    15401: "Favonius Warbow",
    # Claymores
    12406: "Prototype Archaic",
    # Catalysts
    14501: "Skyward Atlas",
    14407: "Mappa Mare",
}
