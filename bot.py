
import discord
from discord import app_commands
from discord.ext import commands

import requests
import socket
import ipaddress
from urllib.parse import urlparse
from pathlib import Path

from config import (
    BOT_TOKEN,
    WEBHOOK_URL,
    GUILD_ID,
    CONTROL_CHANNEL_ID,
    DOWNLOAD_DIR,
    MAX_DOWNLOAD_SIZE,
)

from local_shell import run_command
from monitor import get_status

GUILD = discord.Object(id=GUILD_ID)

intents = discord.Intents.default()

class VMLabBot(commands.Bot):
    async def setup_hook(self):
        synced = await self.tree.sync(guild=GUILD)
        print(f"Registered {len(synced)} guild commands:")
        for command in synced:
            print(f" - /{command.name}")

bot = VMLabBot(command_prefix="!", intents=intents)

async def send_webhook_message(message):
    if not WEBHOOK_URL or WEBHOOK_URL == "YOUR_WEBHOOK_URL":
        return

    try:
        requests.post(
            WEBHOOK_URL,
            json={"content": message},
            timeout=10
        ).raise_for_status()
    except requests.RequestException as error:
        print(f"Webhook error: {error}")

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    await send_webhook_message(
        f"VM Lab bot online: `{socket.gethostname()}`"
    )

@bot.tree.command(name="status", description="Show VM status")
@app_commands.guilds(GUILD)
async def status(interaction: discord.Interaction):
    await interaction.response.defer(ephemeral=True)

    try:
        await interaction.followup.send(
            get_status(),
            ephemeral=True
        )
    except Exception as error:
        await interaction.followup.send(
            f"Status error: `{error}`",
            ephemeral=True
        )

@bot.tree.command(name="runcmd", description="Run a predefined diagnostic")
@app_commands.guilds(GUILD)
@app_commands.describe(command="Choose a predefined diagnostic")
@app_commands.choices(command=[
    app_commands.Choice(name="hostname", value="hostname"),
    app_commands.Choice(name="whoami", value="whoami"),
    app_commands.Choice(name="ipconfig", value="ipconfig"),
    app_commands.Choice(name="tasklist", value="tasklist"),
    app_commands.Choice(name="systeminfo", value="systeminfo"),
    app_commands.Choice(name="dir", value="dir"),
])
async def runcmd(
    interaction: discord.Interaction,
    command: app_commands.Choice[str]
):
    await interaction.response.defer(ephemeral=True)

    output = run_command(command.value)

    await interaction.followup.send(
        f"```text\n{output[:1800]}\n```",
        ephemeral=True
    )

@bot.tree.command(name="ss", description="Request a local screenshot")
@app_commands.guilds(GUILD)
async def ss(interaction: discord.Interaction):
    await interaction.response.defer(ephemeral=True)

    await interaction.followup.send(
        "Screenshot request received.\n"
        "Inside the VM, run `python screenmonitor.py`.\n"
        "The local program will ask you to confirm before capturing "
        "and uploading one screenshot.",
        ephemeral=True
    )

BLOCKED_EXTENSIONS = {
    ".exe", ".msi", ".bat", ".cmd", ".ps1", ".com",
    ".scr", ".vbs", ".js", ".dll", ".sys", ".hta", ".reg"
}

def public_host(hostname):
    try:
        addresses = socket.getaddrinfo(
            hostname, None, type=socket.SOCK_STREAM
        )
        return bool(addresses) and all(
            ipaddress.ip_address(item[4][0]).is_global
            for item in addresses
        )
    except (OSError, ValueError):
        return False

@bot.tree.command(name="download", description="Download a small public HTTPS file")
@app_commands.guilds(GUILD)
@app_commands.describe(url="HTTPS URL of the file")
async def download(interaction: discord.Interaction, url: str):
    await interaction.response.defer(ephemeral=True)

    parsed = urlparse(url)

    if parsed.scheme != "https" or not parsed.hostname:
        await interaction.followup.send(
            "Only HTTPS URLs are accepted.",
            ephemeral=True
        )
        return

    if parsed.username or parsed.password:
        await interaction.followup.send(
            "URLs containing credentials are not accepted.",
            ephemeral=True
        )
        return

    if not public_host(parsed.hostname):
        await interaction.followup.send(
            "The destination must resolve to public IP addresses.",
            ephemeral=True
        )
        return

    filename = Path(parsed.path).name or "download.bin"

    if Path(filename).suffix.lower() in BLOCKED_EXTENSIONS:
        await interaction.followup.send(
            "That file type is blocked.",
            ephemeral=True
        )
        return

    destination = DOWNLOAD_DIR / filename
    temporary = destination.with_suffix(destination.suffix + ".part")

    try:
        total = 0

        with requests.get(
            url,
            stream=True,
            timeout=20,
            allow_redirects=False
        ) as response:
            response.raise_for_status()

            if response.headers.get("Content-Length"):
                if int(response.headers["Content-Length"]) > MAX_DOWNLOAD_SIZE:
                    raise ValueError("File exceeds the size limit.")

            with open(temporary, "wb") as file:
                for chunk in response.iter_content(65536):
                    if not chunk:
                        continue

                    total += len(chunk)
                    if total > MAX_DOWNLOAD_SIZE:
                        raise ValueError("File exceeds the size limit.")

                    file.write(chunk)

        temporary.replace(destination)

        await interaction.followup.send(
            f"Downloaded `{filename}` ({total:,} bytes).\n"
            "The file was saved, not executed.",
            ephemeral=True
        )

    except Exception as error:
        temporary.unlink(missing_ok=True)
        await interaction.followup.send(
            f"Download failed: `{error}`",
            ephemeral=True
        )

@bot.tree.command(name="share", description="Join your current voice channel")
@app_commands.guilds(GUILD)
async def share(interaction: discord.Interaction):
    await interaction.response.defer(ephemeral=True)

    if not isinstance(interaction.user, discord.Member):
        await interaction.followup.send(
            "Could not identify your server membership.",
            ephemeral=True
        )
        return

    channel = interaction.user.voice.channel if interaction.user.voice else None

    if channel is None:
        await interaction.followup.send(
            "Join a voice channel first.",
            ephemeral=True
        )
        return

    try:
        if interaction.guild.voice_client:
            await interaction.guild.voice_client.move_to(channel)
        else:
            await channel.connect()

        await interaction.followup.send(
            f"Connected to **{channel.name}**.",
            ephemeral=True
        )

    except Exception as error:
        await interaction.followup.send(
            f"Voice connection failed: `{error}`",
            ephemeral=True
        )

@bot.tree.command(name="leave", description="Disconnect from voice")
@app_commands.guilds(GUILD)
async def leave(interaction: discord.Interaction):
    await interaction.response.defer(ephemeral=True)

    voice = interaction.guild.voice_client if interaction.guild else None

    if voice is None:
        await interaction.followup.send(
            "The bot is not connected to voice.",
            ephemeral=True
        )
        return

    await voice.disconnect()

    await interaction.followup.send(
        "Disconnected from voice.",
        ephemeral=True
    )

if __name__ == "__main__":
    if not BOT_TOKEN or BOT_TOKEN == "YOUR_BOT_TOKEN":
        raise RuntimeError("Set BOT_TOKEN in config.py first.")

    bot.run(BOT_TOKEN)
