
import platform
import socket

import psutil


def get_status():
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage("C:\\")
    cpu = psutil.cpu_percent(interval=1)

    return (
        "**VMware Screen Monitor — v1.0.2**\n"
        f"Hostname: `{socket.gethostname()}`\n"
        f"OS: `{platform.platform()}`\n"
        f"CPU: `{cpu}%`\n"
        f"RAM: `{memory.percent}%`\n"
        f"Disk: `{disk.percent}%`"
    )
