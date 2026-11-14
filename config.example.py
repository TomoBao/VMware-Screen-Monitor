
from pathlib import Path

BOT_TOKEN = ""

GUILD_ID = 0
CONTROL_CHANNEL_ID = 0

BASE_DIR = Path(__file__).resolve().parent

SCREENSHOT_DIR = BASE_DIR / "Screenshots"
DOWNLOAD_DIR = BASE_DIR / "Downloads"
LOG_DIR = BASE_DIR / "logs"

for directory in (SCREENSHOT_DIR, DOWNLOAD_DIR, LOG_DIR):
    directory.mkdir(parents=True, exist_ok=True)
