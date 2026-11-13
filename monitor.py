
import platform
import psutil
import socket

def get_status():
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage("C:\\")

    return (
        f"**VM Status**\n"
        f"Hostname: `{socket.gethostname()}`\n"
        f"OS: `{platform.platform()}`\n"
        f"CPU usage: `{psutil.cpu_percent(interval=1)}%`\n"
        f"RAM usage: `{memory.percent}%`\n"
        f"Disk usage: `{disk.percent}%`\n"
    )
