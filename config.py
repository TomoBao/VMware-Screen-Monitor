
from pathlib import Path

# Discord bot credentials
BOT_TOKEN = ""

# Discord webhook
WEBHOOK_URL = ""

# Discord server and channel IDs
GUILD_ID = 0
CONTROL_CHANNEL_ID = 0

# Project directories
BASE_DIR = Path(__file__).resolve().parent
SCREENSHOT_DIR = BASE_DIR / "Screenshots"
DOWNLOAD_DIR = BASE_DIR / "Downloads"

# Download size limit (10 MB)
MAX_DOWNLOAD_SIZE = 10 * 1024 * 1024

# Create directories
SCREENSHOT_DIR.mkdir(exist_ok=True)
DOWNLOAD_DIR.mkdir(exist_ok=True)
