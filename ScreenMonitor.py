
import requests
from PIL import ImageGrab
from datetime import datetime
from pathlib import Path

from config import WEBHOOK_URL, SCREENSHOT_DIR

def main():
    print("VMware Screen Monitor")
    print("A screenshot will be captured and uploaded.")
    confirmation = input("Type YES to continue: ").strip()

    if confirmation != "YES":
        print("Cancelled.")
        return

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    path = SCREENSHOT_DIR / f"screenshot_{timestamp}.png"

    try:
        image = ImageGrab.grab()
        image.save(path)

        with open(path, "rb") as file:
            response = requests.post(
                WEBHOOK_URL,
                files={"file": (path.name, file, "image/png")},
                data={"content": "VM screenshot"}
                ,
                timeout=30
            )

        response.raise_for_status()
        print(f"Screenshot uploaded: {path}")

    except Exception as error:
        print(f"Screenshot error: {error}")

if __name__ == "__main__":
    main()
