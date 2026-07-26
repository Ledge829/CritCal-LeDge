"""
Static mapping from Enka artifact setId → set name.

These IDs are extracted directly from Enka's API response data.
Only add IDs here that have been VERIFIED against actual Enka data.
"""

SET_IDS: dict[int, str] = {
    # Verified from Enka API responses
    10005: "Berserker",
    15001: "Resolution of Sojourner",
    15003: "Defender's Will",
    15006: "Martial Artist",
    15025: "Thundersoother",
    15038: "Deepwood Memories",
    15039: "Gilded Dreams",
    15042: "Nymph's Dream",
}
