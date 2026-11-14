
from pathlib import Path

BOT_TOKEN = "YOUR_DISCORD_BOT_TOKEN"
WEBHOOK_URL = ""

GUILD_ID = 0
CONTROL_CHANNEL_ID = 0

BASE_DIR = Path(__file__).resolve().parent
LOG_DIR = BASE_DIR / "logs"
SCREENSHOT_DIR = BASE_DIR / "Screenshots"
DOWNLOAD_DIR = BASE_DIR / "Downloads"

for folder in (LOG_DIR, SCREENSHOT_DIR, DOWNLOAD_DIR):
    folder.mkdir(parents=True, exist_ok=True)
