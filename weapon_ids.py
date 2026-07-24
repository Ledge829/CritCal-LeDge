"""
Static mapping from Enka weapon itemId → weapon name.

Enka returns a numeric itemId for each weapon. When the name hash
isn't in their loc.json, we look it up here instead. This covers
weapons whose hash is missing from Enka's published data.

HOW TO ADD: when you see "X-Star Y (Unrecognized)" for a weapon
you know the name of, find its itemId from the Enka raw response
and add it below. Over time this covers every weapon in the game.
"""

WEAPON_IDS: dict[int, str] = {
    # Swords (1xxxx)
    11513: "Splendor of Tranquil Waters",
    11511: "Key of Khaj-Nisut",
    11502: "Skyward Blade",
    11416: "Kagotsurube Isshin",
    11414: "Amenoma Kageuchi",
    11422: "Toukabou Shigure",
    # Polearms (13xxx)
    13501: "Staff of Homa",
    13416: "The Catch",
    # Bows (15xxx)
    15508: "Aqua Simulacra",
    15401: "Favonius Warbow",
    # Claymores (12xxx)
    12406: "Prototype Archaic",
    # Catalysts (14xxx)
    14501: "Skyward Atlas",
    14407: "Mappa Mare",

    # ── Unmapped IDs from UID 631904091 ──
    # 15515 (5★ Bow) — Venti
    # 14415 (4★ Catalyst) — Xianyun
    # 13432 (4★ Polearm) — Xiao
    # 14403 (4★ Catalyst)
    # 14302 (3★ Catalyst) — Sucrose
    # 11405 (4★ Sword) — Lynette
    # 14414 (4★ Catalyst) — Lan Yan
}
