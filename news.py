"""
CritCal News system.

Provides Genshin Impact news from Hoyolab RSS with admin posting support.
Only users with the NEWS_SECRET key can create manual posts.
"""
import time
import requests
import json
import os
from typing import List, Dict, Any, Optional

NEWS_SECRET = os.environ.get("NEWS_SECRET", "critcal-admin-2026")
NEWS_FILE = "/tmp/critcal_news.json"
HOYOLAB_FEED = "https://www.hoyolab.com/apis/gamepost/w2/getNewsList?gids=2&page_size=5&type=3"

# Static fallback news when Hoyolab is unreachable
FALLBACK_NEWS = [
    {
        "id": "critcal-v2",
        "title": "CritCal v2 Update — Smarter scoring, new databases",
        "summary": "Weapons and artifacts now have richer data with best-for recommendations and character themes.",
        "image": "",
        "url": "",
        "source": "critcal",
        "timestamp": int(time.time()),
    },
    {
        "id": "fallback-1",
        "title": "CritCal is live!",
        "summary": "Enter any UID or analyze a build manually. Open source and community-driven.",
        "image": "",
        "url": "https://github.com/Ledge829/CritCal-LeDge",
        "source": "critcal",
        "timestamp": int(time.time()) - 86400,
    },
    {
        "id": "fallback-2",
        "title": "Version 5.x characters added",
        "summary": "All Natlan characters now have build data, artifact recommendations, and weapon tiers.",
        "image": "",
        "url": "",
        "source": "critcal",
        "timestamp": int(time.time()) - 172800,
    },
]

_news_cache = {"data": None, "time": 0}
_CACHE_TTL = 30 * 60  # 30 minutes


def _fetch_hoyolab_news() -> List[Dict[str, Any]]:
    """Fetches latest Genshin news from Hoyolab."""
    try:
        resp = requests.get(HOYOLAB_FEED, timeout=10, headers={
            "User-Agent": "CritCal/2.0",
            "Accept": "application/json",
        })
        if resp.status_code != 200:
            return []
        data = resp.json()
        posts = []
        for item in (data.get("data", {}).get("list", [])):
            posts.append({
                "id": f"hl-{item.get('post_id', '')}",
                "title": item.get("subject", ""),
                "summary": item.get("content", "")[:200],
                "image": _extract_image(item),
                "url": f"https://www.hoyolab.com/article/{item.get('post_id', '')}",
                "source": "hoyolab",
                "timestamp": item.get("created_at", int(time.time())),
            })
        return posts
    except Exception:
        return []


def _extract_image(item: Dict) -> str:
    """Extracts the first image URL from a Hoyolab post."""
    for img in item.get("images", []):
        if img:
            return img
    return ""


def get_news(force_refresh: bool = False) -> List[Dict[str, Any]]:
    """Returns merged news: Hoyolab posts + manual CritCal posts."""
    now = time.time()

    # Auto-fetch Hoyolab news
    if force_refresh or not _news_cache["data"] or now - _news_cache["time"] > _CACHE_TTL:
        hoyolab = _fetch_hoyolab_news()
        if hoyolab:
            _news_cache["data"] = hoyolab
            _news_cache["time"] = now

    all_news = list(_news_cache["data"] or []) + list(FALLBACK_NEWS)

    # Add manual posts from file
    try:
        with open(NEWS_FILE, "r") as f:
            manual_posts = json.load(f)
            all_news.extend(manual_posts)
    except (FileNotFoundError, json.JSONDecodeError):
        pass

    # Sort by timestamp descending (newest first)
    all_news.sort(key=lambda n: n.get("timestamp", 0), reverse=True)

    # Deduplicate by id
    seen = set()
    unique = []
    for n in all_news:
        nid = n.get("id", "")
        if nid not in seen:
            seen.add(nid)
            unique.append(n)

    return unique


def create_post(title: str, summary: str = "", image: str = "", url: str = "") -> bool:
    """Creates a manual news post (requires NEWS_SECRET)."""
    try:
        with open(NEWS_FILE, "r") as f:
            posts = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        posts = []

    posts.append({
        "id": f"critcal-{int(time.time())}",
        "title": title,
        "summary": summary,
        "image": image,
        "url": url,
        "source": "critcal",
        "timestamp": int(time.time()),
    })

    # Keep max 50 manual posts
    posts = posts[-50:]

    with open(NEWS_FILE, "w") as f:
        json.dump(posts, f)

    return True
