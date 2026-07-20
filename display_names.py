"""
Human-readable display names for characters whose canonical key (used
internally throughout characters.py / build_data.py / scoring.py) isn't
just their name with the first letter capitalized -- e.g. "hutao" ->
"Hu Tao", "sara" -> "Kujou Sara".

Used ONLY for display purposes (the /characters endpoint, and anywhere
the frontend needs a name to show a person). Never used for lookups --
those always go through characters.py's normalize_character() /
CHARACTER_ALIASES, which are unaffected by anything in this file.

Any canonical key not listed here falls back to key.title() (e.g.
"xilonen" -> "Xilonen"), which is correct for the large majority of
single-word names. Add an entry here only when that fallback would be
wrong (compound/surname names, Traveler variants, etc.).
"""

from typing import Dict

DISPLAY_NAMES: Dict[str, str] = {
    # Compound / surname names (mostly Inazuma's official full-name convention)
    "hutao": "Hu Tao",
    "kazuha": "Kaedehara Kazuha",
    "heizou": "Shikanoin Heizou",
    "sara": "Kujou Sara",
    "kukishinobu": "Kuki Shinobu",
    "kokomi": "Sangonomiya Kokomi",
    "raiden": "Raiden Shogun",
    "yaemiko": "Yae Miko",
    "ayaka": "Kamisato Ayaka",
    "itto": "Arataki Itto",
    "lanyan": "Lan Yan",
    "childe": "Tartaglia",
    "ayato": "Kamisato Ayato",
    "mizuki": "Yumemizuki Mizuki",

    # Traveler variants
    "traveler": "Traveler",
    "anemotraveler": "Traveler (Anemo)",
    "geotraveler": "Traveler (Geo)",
    "electrotraveler": "Traveler (Electro)",
    "dendrotraveler": "Traveler (Dendro)",
    "hydrotraveler": "Traveler (Hydro)",
    "pyrotraveler": "Traveler (Pyro)",
}


def display_name(canonical_key: str) -> str:
    """Returns the best display name for a canonical character key."""
    if canonical_key in DISPLAY_NAMES:
        return DISPLAY_NAMES[canonical_key]
    return canonical_key.replace("_", " ").title()
