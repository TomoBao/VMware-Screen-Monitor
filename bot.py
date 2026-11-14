
import discord
from discord import app_commands
from discord.ext import commands

from config import BOT_TOKEN, GUILD_ID, CONTROL_CHANNEL_ID
from logger import logger
from monitor import get_status
from local_shell import run_command
from webhook import send_webhook_message


GUILD = discord.Object(id=GUILD_ID)

intents = discord.Intents.default()


class MonitorBot(commands.Bot):
    async def setup_hook(self):
        commands_synced = await self.tree.sync(guild=GUILD)
        logger.info("Registered %s slash commands", len(commands_synced))


bot = MonitorBot(command_prefix="!", intents=intents)

DIAGNOSTICS = [
    app_commands.Choice(name="hostname", value="hostname"),
    app_commands.Choice(name="whoami", value="whoami"),
    app_commands.Choice(name="ipconfig", value="ipconfig"),
    app_commands.Choice(name="tasklist", value="tasklist"),
    app_commands.Choice(name="systeminfo", value="systeminfo"),
]


async def check_channel(interaction):
    allowed = (
        interaction.guild_id == GUILD_ID
        and interaction.channel_id == CONTROL_CHANNEL_ID
    )

    if not allowed:
        message = "This is not the configured control channel."

        if not interaction.response.is_done():
            await interaction.response.send_message(
                message, ephemeral=True
            )

        return False

    return True


@bot.event
async def on_ready():
    logger.info("Connected as %s", bot.user)
    await send_webhook_message(
        f"VMware Screen Monitor online: `{bot.user}`"
    )


# 1. STATUS
@bot.tree.command(name="status", description="Show VM status")
@app_commands.guilds(GUILD)
async def status(interaction: discord.Interaction):
    if not await check_channel(interaction):
        return

    await interaction.response.send_message(
        get_status(), ephemeral=True
    )
    logger.info("Status requested")


# 2. RUNCMD
@bot.tree.command(
    name="runcmd",
    description="Run a predefined diagnostic",
)
@app_commands.guilds(GUILD)
@app_commands.describe(command="Select a diagnostic")
@app_commands.choices(command=DIAGNOSTICS)
async def runcmd(
    interaction: discord.Interaction,
    command: app_commands.Choice[str],
):
    if not await check_channel(interaction):
        return

    await interaction.response.defer(ephemeral=True)
    output = run_command(command.value)

    await interaction.followup.send(
        f"```text\n{output}\n```",
        ephemeral=True,
    )
    logger.info("Diagnostic requested: %s", command.value)


# 3. SS
@bot.tree.command(
    name="ss",
    description="Show local screenshot instructions",
)
@app_commands.guilds(GUILD)
async def ss(interaction: discord.Interaction):
    if not await check_channel(interaction):
        return

    await interaction.response.send_message(
        "Run `python screenmonitor.py` inside the VM. "
        "Confirm locally to save the screenshot.",
        ephemeral=True,
    )
    logger.info("Screenshot instructions requested")


# 4. DOWNLOAD
@bot.tree.command(
    name="download",
    description="Show local download instructions",
)
@app_commands.guilds(GUILD)
async def download(interaction: discord.Interaction):
    if not await check_channel(interaction):
        return

    await interaction.response.send_message(
        "Remote URL downloads are disabled. "
        "Download files through your VM browser and save them "
        "in the Downloads folder.",
        ephemeral=True,
    )
    logger.info("Download instructions requested")


# 5. SHARE
@bot.tree.command(
    name="share",
    description="Connect the bot to your voice channel",
)
@app_commands.guilds(GUILD)
async def share(interaction: discord.Interaction):
    if not await check_channel(interaction):
        return

    if not interaction.user.voice:
        await interaction.response.send_message(
            "Join a voice channel first.",
            ephemeral=True,
        )
        return

    if interaction.guild.voice_client:
        await interaction.response.send_message(
            "The bot is already connected to a voice channel.",
            ephemeral=True,
        )
        return

    channel = interaction.user.voice.channel

    await interaction.response.defer(ephemeral=True)

    try:
        await channel.connect()
        await interaction.followup.send(
            f"Connected to **{channel.name}**. "
            "This does not share the VM desktop.",
            ephemeral=True,
        )
        logger.info("Connected to voice channel: %s", channel.id)

    except Exception:
        logger.exception("Voice connection failed")
        await interaction.followup.send(
            "Could not connect. Check bot voice permissions.",
            ephemeral=True,
        )


# 6. LEAVE
@bot.tree.command(
    name="leave",
    description="Disconnect the bot from voice",
)
@app_commands.guilds(GUILD)
async def leave(interaction: discord.Interaction):
    if not await check_channel(interaction):
        return

    voice = interaction.guild.voice_client

    if voice is None:
        await interaction.response.send_message(
            "The bot is not connected to voice.",
            ephemeral=True,
        )
        return

    await voice.disconnect()

    await interaction.response.send_message(
        "Disconnected from voice.",
        ephemeral=True,
    )
    logger.info("Disconnected from voice")


if __name__ == "__main__":
    if not BOT_TOKEN or not GUILD_ID or not CONTROL_CHANNEL_ID:
        raise RuntimeError(
            "Configure BOT_TOKEN, GUILD_ID and CONTROL_CHANNEL_ID."
        )

    logger.info("Starting VMware Screen Monitor v1.0.2")
    bot.run(BOT_TOKEN)
