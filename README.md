<div align="center">

```
   *  .  ✦        .    ✦      .        *        .    ✦
       ____              _____             __     _         __ 
      / __ \____ ___  __/ ___/____  ____ _/ /____ / |_ ____  / /_ 
     / / / / __ `/ / / /\__ \/ __ \/ __ `/ __/ __ /| | / __ \/ __/  
    / /_/ / /_/ / /_/ /___/ / /_/ / /_/ / /_/ /_/ / | |/ / / / /_ 
   /_____/\__,_/\__, //____/ .___/\__,_/\__/\____/  |___/_/ /_/\__/ 
               /____/     /_/         B R I E F I N G
   .        ✦      *   .        ✦   *    .    ✦     .       *
```

### 🛰️ Live space data, straight to your terminal.

**One command. Three NASA data feeds. Zero fluff.**

![Python](https://img.shields.io/badge/Python-3.14-3776AB?style=for-the-badge&logo=python&logoColor=white)
![NASA](https://img.shields.io/badge/Powered%20by-NASA%20Open%20APIs-0B3D91?style=for-the-badge&logo=nasa&logoColor=white)
![Status](https://img.shields.io/badge/status-100%25%20operational-success?style=for-the-badge)
![Made with](https://img.shields.io/badge/made%20with-☕%20%2B%20😤-orange?style=for-the-badge)

<br>

`git clone` → `.env` → `run` → **you're browsing the solar system.**

</div>

---

## 🌠 What is this?

Ever wanted your terminal to feel a little more like Mission Control? **Daily Space Briefing** connects directly to NASA's live public data feeds and drops the results right into your CLI — no browser, no clutter, just the data.

Pick an option. It fetches, displays, and **quietly logs everything** to a running history file — so weeks from now, you'll have your own personal archive of the sky.

<div align="center">

| 🌌 | ☄️ | 🌍 |
|:---:|:---:|:---:|
| **Astronomy Picture of the Day** | **Near-Earth Asteroid Watch** | **Live Earth Imagery** |
| Today's featured space photo, straight from NASA's archives | Every asteroid passing Earth this week — hazardous ones flagged 🔴 | Real satellite photos of Earth from 1.5 million km away |

</div>

---

## ⚡ Quick Look

```
   ✦    .        ✦   *    .    ✦     .       *   ✦
   ------ DAILY SPACE BRIEFING -----
   1. Today's Astronomy Picture
   2. Near-Earth Asteroids (Next 7 Days)
   3. Earth Imagery (EPIC)
   0. Exit
   Choose an option: 1

   🌌 Title: The Sky Turns Above Paranal
   📅 Date: 2026-08-28
   📝 At the latitude of ESO's Paranal Observatory in Chile...
   🔗 https://apod.nasa.gov/apod/image/2608/TheSkyTurnsAboveParanal_1024.jpg
```

<details>
<summary>☄️ <b>See an asteroid scan in action</b></summary>

```
   ----> Date: 2026-08-29

    Name: (2019 LL5)
    Hazardous: False
    Diameter: 1153.55 meters
   ===================================
    Name: (2012 TB53)
    Hazardous: False
    Diameter: 142.57 meters
   ===================================
```
</details>

---

## 🧬 How it's built

<div align="center">

```
                    ┌──────────────┐
                    │   main.py    │   ← menu & program flow
                    └──────┬───────┘
           ┌───────────────┼───────────────┐
     ┌─────▼─────┐   ┌─────▼─────┐   ┌─────▼─────┐
     │  apod.py  │   │ neows.py  │   │  epic.py  │
     │  🌌 APOD  │   │ ☄️ NeoWs  │   │ 🌍 EPIC   │
     └─────┬─────┘   └─────┬─────┘   └─────┬─────┘
           └───────────────┼───────────────┘
                    ┌───────▼───────┐
                    │  logger.py    │  → space_log.txt
                    └───────────────┘
```

</div>

Every module fetches its own data and hands it back clean — `main.py` never touches raw API responses directly. Every successful lookup gets appended (never overwritten) to a growing local log.

## 🛠️ Under the hood

<div align="center">

![requests](https://img.shields.io/badge/requests-HTTP-000000?style=flat-square)
![dotenv](https://img.shields.io/badge/python--dotenv-secrets-000000?style=flat-square)
![datetime](https://img.shields.io/badge/datetime-date%20ranges-000000?style=flat-square)

</div>

- 🔁 **Auto-retry logic** — flaky network? It tries again before giving up, instead of crashing
- 🔐 **`.env`-based secrets** — your API key never touches the codebase or Git history
- 🧩 **Fully modular** — every API is one self-contained file, easy to extend or swap out

## 🚀 Get it running

```bash
# 1. Clone it
git clone https://github.com/YOUR-USERNAME/SpaceBriefing.git
cd SpaceBriefing

# 2. Install the two dependencies
pip install requests python-dotenv

# 3. Grab a free NASA API key → https://api.nasa.gov (takes 30 seconds)

# 4. Drop it in a .env file
echo "NASA_API_KEY=your_key_here" > .env

# 5. Launch
python src/main.py
```

That's it. No config files, no build step, no nonsense.

## 🪐 Why I built this

This is my first-ever Python project — built right after finishing **StockVault**, a full inventory management system I built in C. I wanted a project that would push me into real-world territory: actual APIs, actual JSON, actual bugs that don't show up until you run the thing.

**What it taught me:**

- 🌐 Talking to REST APIs and parsing JSON — worlds easier than C's cJSON, but the concepts carried straight over
- 🔑 Managing secrets properly instead of hardcoding them
- 🛡️ Writing code that fails *gracefully* — status checks, retries, `None` guards everywhere
- 🗃️ Splitting a growing script into a real multi-file project structure
- 🐛 Debugging methodically — chasing down silent bugs (unindented loops, wrong endpoints, functions defined but never called) with nothing but print statements and patience

## 🔭 What's next

- [ ] 🌋 EONET integration — track wildfires, storms, and volcanic activity
- [ ] ⏰ Scheduled daily auto-run
- [ ] 📊 Export history to CSV + visualize trends with pandas/matplotlib
- [ ] 🖥️ Web dashboard version (Flask)

---

<div align="center">

**Built with 🛰️, ☕, and an unreasonable number of `print("DEBUG...")` statements.**

*If you made it this far — thanks for reading. Go check out the code.* ⭐

</div>
