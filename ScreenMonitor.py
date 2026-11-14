
from datetime import datetime

from PIL import ImageGrab

from config import SCREENSHOT_DIR
from logger import logger


def main():
    print("VMware Screen Monitor - Local Screenshot")
    print("Screenshots are saved locally only.")

    if input("Type YES to capture: ").strip() != "YES":
        print("Cancelled.")
        return

    try:
        SCREENSHOT_DIR.mkdir(parents=True, exist_ok=True)

        filename = datetime.now().strftime(
            "screenshot_%Y%m%d_%H%M%S.png"
        )
        path = SCREENSHOT_DIR / filename

        ImageGrab.grab().save(path)

        logger.info("Screenshot saved: %s", filename)
        print(f"Saved: {path}")

    except Exception:
        logger.exception("Screenshot failed")
        print("Screenshot failed. Check logs.")


if __name__ == "__main__":
    main()
