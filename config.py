# Telegram API credentials (load from .env in main.py)
API_ID = None
API_HASH = None

# --- NEW AI CONFIGURATION ---
GEMINI_API_KEY = None # <<< IMPORTANT: Get this from Google AI Studio
MODE = "AI" # <<< CHANGED from "RANDOM" to "AI"
# ---------------------------

# Channels you want to monitor
CHANNELS = ["tiktokleadsgen",
            "stockverified",
            -1002404659940, #Practicals
            "Uefa_Champions_Leagueee",
            "uefa_champ_league",
            "onefootball_updates",
            "juventus",
            "footballfactlys",
            "Football433_uk",
            "tottenhm",
            "goal264",
            "goal24officiaI",
            "goal_sport_football",
            "goal_football_uk",
            "BBC_Sports_Football_Updates",
            "sofascore_uk",
            "liverpool_worldwide",
            "bayern_munich",
            "real_madrid_en",
            "Realmadrid_world",
            "Barcelona_worldwide",
            "barcelona_eng",
            "Messi_lionel_uk",
            "jfball",
            "officialmanchester",
            "united_4_life",
            "manchester",
            "manchester_united_uk",
            "Manchester_Utdfc",
            "manchester_city",
            "Official_Chelsea_Blues",
            "CFC_ChelseaFC",
            "FabrizioRomano_uk",
            "br_football_news",
            "Espn_Football_News_UK",
            "premier",
            "premier_league_football_news",
            "Premier_League_News_TG",
            "Premier_League_Updates",
            "skysportsfootballupdates",
            "sky_sports_football_updates",
            "Sky_Sportz_football",
            "skysports_football",
            "vetland_sports_football1",
            "messimedia",
            "manchesterunited_passion",
            "footballxilive",
            "footymadness",
            "Empire_MU"
            ]

# Behaviour controls
DELAY_RANGE = (15, 60)
SKIP_PROBABILITY = 0.3
LOG_ONLY = False  # For posting on comments, I'll change to True if I want logs print only
# Reply queue settings: how long to keep trying to find the discussion message (seconds)
# Increased to 300s to allow the discussion message to appear and conversion to threaded reply
REPLY_QUEUE_MAX_WAIT = 300
# Poll interval for queued jobs (seconds)
REPLY_QUEUE_POLL_INTERVAL = 3
# Local cooldown per linked discussion to avoid flood limits (seconds)
COOLDOWN = 300
# How many recent messages to scan when searching for the discussion message
REPLY_QUEUE_SEARCH_LIMIT = 1000
# If True, allow reply jobs to be queued even when the server requests a wait longer
# than REPLY_QUEUE_MAX_WAIT. Use with caution — this can cause jobs to sit for long periods.
REPLY_QUEUE_ALLOW_LONG_WAIT = False
# When allowing long waits, add this slack (seconds) after the required wait before giving up
REPLY_QUEUE_LONG_WAIT_SLACK = 60
# When True, dump a compact debug view of recent messages for a discussion when mapping fails
DEBUG_DUMP_RECENT = True