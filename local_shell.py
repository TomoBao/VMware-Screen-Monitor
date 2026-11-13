
import subprocess
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

ALLOWED_COMMANDS = {
    "hostname": ["hostname"],
    "whoami": ["whoami"],
    "ipconfig": ["ipconfig"],
    "tasklist": ["tasklist"],
    "systeminfo": ["systeminfo"],
    "dir": ["cmd.exe", "/c", "dir", str(BASE_DIR)],
}

def run_command(name):
    if name not in ALLOWED_COMMANDS:
        return "Command not allowed."

    try:
        result = subprocess.run(
            ALLOWED_COMMANDS[name],
            capture_output=True,
            text=True,
            timeout=15,
            shell=False
        )

        output = result.stdout or result.stderr
        return output[:1800] or "Command completed with no output."

    except subprocess.TimeoutExpired:
        return "Command timed out."
    except Exception as error:
        return f"Error: {error}"
