CritCal

A production-ready Genshin Impact Build Rating API built with Python and Flask.

CritCal analyzes a character's build using character-specific scoring logic, benchmark goals, crit optimization, and build heuristics. It supports both manually entered builds and automatic retrieval from Enka.Network using a player's UID.

Designed for Discord bots, web apps, and other Genshin tools.

---

Features

- Character-specific scoring
- Manual build rating ("/rate/manual")
- Live Enka.Network support ("/rate/uid")
- Automatic character recognition
- Crit Ratio analysis
- Crit Value calculation
- Substat efficiency scoring
- Relative damage estimation
- Character benchmark comparison
- Dynamic build recommendations
- Character aliases (Hu Tao, Raiden Shogun, Scaramouche, etc.)
- Weapon extraction
- Artifact set extraction
- Status & monitoring endpoints
- UptimeRobot integration
- Metadata caching
- Structured JSON responses

---

API Endpoints

"POST /rate/manual"

Rates a build from manually entered stats.

Example request:

{
  "character": "Furina",
  "crit_rate": 82,
  "crit_dmg": 188,
  "hp": 39200,
  "atk": 1210,
  "def": 720,
  "energy_recharge": 181,
  "elemental_mastery": 40,

  "weapon": {
    "name": "Splendor of Tranquil Waters",
    "level": 90,
    "refinement": 1
  },

  "artifact_sets": [
    {
      "name": "Golden Troupe",
      "count": 4
    }
  ]
}

---

"POST /rate/uid"

Fetches a player's showcased character directly from Enka.Network and rates it automatically.

Example request:

{
  "uid": "600000000",
  "character": "Furina"
}

The character field is optional if only one showcased character matches your request.

---

"GET /status"

Returns API status information.

Includes:

- API health
- Uptime
- Cache status
- Monitor information
- Response timing
- Service diagnostics

---

"GET /ping"

Simple health endpoint.

Returns:

OK

Useful for Render health checks and UptimeRobot monitoring.

---

Example Response

{
  "character": "Furina",
  "grade": "S",
  "overall_score": 92.6,
  "grade_description": "Exceptional — close to an optimized endgame build",

  "crit_rate": 82.0,
  "crit_dmg": 188.0,
  "crit_value": 352,

  "substat_efficiency_score": 89.3,
  "estimated_relative_damage": 91.7,

  "weapon": {
    "name": "Splendor of Tranquil Waters",
    "level": 90,
    "refinement": 1
  },

  "artifact_sets": [
    {
      "name": "Golden Troupe",
      "count": 4
    }
  ],

  "recommendations": [
    "Excellent Crit Ratio.",
    "HP benchmark achieved.",
    "Very efficient substat distribution."
  ]
}

---

Scoring Philosophy

CritCal does not attempt to simulate exact in-game damage.

Instead, it evaluates overall build quality using several independent metrics.

These include:

- Character-specific stat scaling
- Crit Ratio optimization
- Crit Value
- Substat efficiency
- Benchmark comparisons
- Relative damage estimation
- Character-specific Energy Recharge requirements
- Dynamic recommendations

Each character can have unique scoring behaviour based on their intended role.

For example:

- HP scalers
- DEF scalers
- EM scalers
- Burst-reliant supports
- Freeze carries
- Hypercarries

This allows builds to be judged according to the character instead of using a single generic formula.

---

Character Database

CritCal includes a growing character database containing:

- Character aliases
- Stat scaling
- Crit ratio targets
- Energy Recharge exceptions
- Benchmark goals
- Build archetypes
- Future scoring hooks

The database is designed to make supporting new characters straightforward while keeping the scoring engine data-driven.

---

Project Structure

app.py

Flask application and API routes.

scoring.py

Core scoring engine.

characters.py

Character configuration database.

enka_client.py

Enka.Network integration.

status.py

Status monitoring and uptime endpoints.

requirements.txt

Python dependencies.

---

Running Locally

Clone the repository.

Install dependencies:

pip install -r requirements.txt

Run the server:

python app.py

The API will start on:

http://127.0.0.1:5000

---

Deployment

CritCal is designed to work well on platforms such as Render.

Typical deployment:

- Runtime: Python 3
- Build Command:

pip install -r requirements.txt

- Start Command:

gunicorn app:app

The optional "/ping" endpoint can be monitored by services such as UptimeRobot.

---

Roadmap

Planned improvements include:

- Expanded character database
- Additional artifact set support
- Expanded weapon database
- Better build summaries
- Improved recommendation engine
- Enhanced benchmark system
- Additional API endpoints
- Documentation improvements
- Automated tests
- Performance optimizations

---

Contributing

Issues, suggestions, and pull requests are welcome.

As Genshin Impact continues to receive new characters, weapons, and artifact sets, the project will continue expanding to support them.

---

License

This project is provided for educational and personal use.

Genshin Impact and all related assets belong to HoYoverse.

Enka.Network is an independent community project used for publicly available showcase data.
