
import subprocess

from logger import logger

COMMANDS = {
    "hostname": ["hostname"],
    "whoami": ["whoami"],
    "ipconfig": ["ipconfig"],
    "tasklist": ["tasklist"],
    "systeminfo": ["systeminfo"],
}


def run_command(name):
    command = COMMANDS.get(name)

    if command is None:
        return "Unsupported diagnostic."

    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=15,
            shell=False,
            check=False,
        )

        return (result.stdout or result.stderr or "No output.")[:1800]

    except Exception:
        logger.exception("Diagnostic failed: %s", name)
        return "Diagnostic failed. Check logs/bot.log."
