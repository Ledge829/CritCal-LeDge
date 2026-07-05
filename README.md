# Genshin Build Rater API

Rates a character's build (crit ratio, substat efficiency, overall grade,
recommendations) either from manually entered stats, or automatically
pulled from a player's live Enka.Network showcase using just their UID.

## 1. Deploy to Render (free)

1. Create a free account at https://render.com (GitHub/Google login, no
   card needed).
2. Push these files to a **public or private GitHub repo**:
   `app.py`, `scoring.py`, `enka_client.py`, `requirements.txt`
3. In Render: **New +** → **Web Service** → connect your repo.
4. Settings:
   - **Runtime:** Python 3
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app`
   - **Instance Type:** Free
5. Deploy. Render gives you a URL like:
   `https://your-app-name.onrender.com`

## 2. Keep it awake with UptimeRobot

Render's free tier sleeps after ~15 min of no traffic (cold start ~30-60s
on the next request). To avoid that:

1. Go to https://uptimerobot.com → free account.
2. **Add New Monitor** → HTTP(s).
3. URL: `https://your-app-name.onrender.com/ping`
4. Interval: 5 minutes.

This isn't bulletproof (Render officially discourages it, and a rare cold
start can still slip through), but it works well in practice for a
Discord bot's traffic pattern.

## 3. Calling it from BDFD

BDFD's `$jsonRequest[method;url;headers;body]` function sends HTTP
requests and lets you pull fields out of the JSON response with
`$jsonRequest[get;...]`-style syntax (check BDFD's current docs for the
exact retrieval function name/version, as it does change between BDFD
versions).

### Option A — UID-based command (auto-pull, recommended)

Command trigger: `!build <uid> <character name>`

```
$jsonRequest[POST;https://your-app-name.onrender.com/rate/uid;Content-Type=application/json;{"uid":"$message[2]","character":"$message[3]"}]
```

Then read fields like `grade`, `overall_score`, `crit_ratio_note`, and
`recommendations` from the response to build your embed/reply.

### Option B — Manual stat entry command

Command trigger: `!build manual <character> <critRate> <critDMG> <atk>`

```
$jsonRequest[POST;https://your-app-name.onrender.com/rate/manual;Content-Type=application/json;{"character":"$message[3]","crit_rate":$message[4],"crit_dmg":$message[5],"atk":$message[6]}]
```

You can extend this to also collect `hp`, `def`, `elemental_mastery`,
`energy_recharge`, and a `substats` object as the command grows — BDFD
lets you chain more `$message[n]` args or use a modal/multi-step command
if you want a friendlier input flow.

## 4. Response shape (both endpoints)

```json
{
  "character": "Hu Tao",
  "grade": "A",
  "grade_description": "Great — strong, min-maxed build",
  "overall_score": 84.8,
  "crit_value": 270,
  "crit_rate": 65,
  "crit_dmg": 140,
  "crit_ratio_note": "Crit ratio is well balanced...",
  "substat_efficiency_score": 73.9,
  "estimated_relative_damage": 83.8,
  "recommendations": ["..."],
  "stats_used": { "atk": 2200, "hp": 30000, "def": 700, ... }
}
```

`estimated_relative_damage` is a 0-100 build-quality indicator relative to
a theoretical BiS build — **not** a literal in-game damage number. Getting
an exact damage number requires per-character talent multipliers, enemy
RES/DEF, and rotation data, which is a much bigger project than this API.

## 5. Known limitations / next steps

- Character name lookup for UID mode depends on Enka's public reference
  data staying in its current format. If a brand-new character shows up
  as `"Character #10000XX"` instead of their name shortly after a patch,
  Enka's data just hasn't updated yet — it'll resolve within a day or so.
- `character_scaling` defaults to `"atk"`. Pass `"em"` in the request body
  for reaction/EM-focused characters to weight the score differently.
- Enka only sees what's in the player's **in-game Character Showcase** —
  if a character isn't showcased, UID mode won't find them and manual
  entry is the fallback.
  
