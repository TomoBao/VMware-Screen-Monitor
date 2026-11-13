# VMware Screen Monitor

<div align="center">
  <img src="assets/banner.png" alt="VMware Screen Monitor" width="100%">

  **A Python-powered Discord bot for monitoring a Windows VMware lab.**

  ![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)
  ![Platform](https://img.shields.io/badge/Platform-Windows-0078D6?logo=windows)
  ![Discord](https://img.shields.io/badge/Discord-Bot-5865F2?logo=discord)
  ![License](https://img.shields.io/badge/License-MIT-green)
</div>

---

## Overview

VMware Screen Monitor is a Python project that connects a Windows virtual machine to a Discord bot.

It provides system information, predefined diagnostic commands, file downloads, and a locally confirmed screenshot workflow.

Designed for personal VMware labs and authorized testing environments.

## Features

- **System Monitoring** — View CPU, RAM, disk, and system information.
- **Diagnostic Commands** — Run predefined Windows diagnostic commands.
- **File Downloads** — Download files from HTTPS URLs with basic restrictions.
- **Screenshot Workflow** — Capture and upload a screenshot after local confirmation.
- **Voice Connection** — Connect or disconnect the bot from a Discord voice channel.
- **Webhook Notifications** — Send bot status notifications through Discord webhooks.

## Commands

| Command | Description |
|---|---|
| `/status` | Display VM system information |
| `/runcmd` | Run a predefined diagnostic command |
| `/download` | Download a file from an HTTPS URL |
| `/ss` | Request a locally confirmed screenshot |
| `/share` | Connect to your current voice channel |
| `/leave` | Disconnect from voice |

## Requirements

- Windows 10 or later
- VMware Workstation or compatible virtualization software
- Python 3.10 or later
- Discord bot application
- Internet connection

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/TomoBao/VMware-Screen-Monitor.git
cd VMware-Screen-Monitor
```

### 2. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 3. Configure the bot

Create a local `config.py` using `config.example.py` as a template.

Configure your own:

- Discord bot token
- Discord webhook URL
- Discord server ID
- Control channel ID

**Never upload real credentials to GitHub.**

### 4. Start the bot

```bash
python bot.py
```

The bot should connect to Discord and synchronize its slash commands.

## Screenshot Workflow

The screenshot workflow requires local confirmation.

1. Run the screenshot program inside your Windows VM:

   ```bash
   python ScreenMonitor.py
   ```

2. Review the local confirmation prompt.
3. Type `YES` to authorize the capture.
4. The screenshot is saved locally and uploaded to the configured webhook.

Screenshots are not captured silently or continuously.

## Project Structure

```text
VMware-Screen-Monitor/
│
├── assets/
│   └── banner.png
│
├── bot.py
├── ScreenMonitor.py
├── config.example.py
├── local_shell.py
├── monitor.py
├── requirements.txt
├── README.md
├── .gitignore
└── LICENSE
```

The `Downloads/` and `Screenshots/` directories are used for local project data when created by the application.

## Security

- Keep bot tokens and webhook URLs private.
- Use the bot only on systems you own or are authorized to monitor.
- Diagnostic commands are restricted to predefined operations.
- Screenshot uploads require local confirmation.
- Downloaded files are not automatically executed.
- Download restrictions are basic safeguards, not a guarantee that files are safe.

## Limitations

- `/share` connects the bot to voice; it does not automatically start Discord Go Live.
- `/ss` requires local execution and confirmation.
- Download restrictions should not be treated as a hardened security boundary.

## Contributing

Suggestions, bug reports, and improvements are welcome!

1. Fork this repository.
2. Create a feature branch.
3. Make your changes.
4. Submit a Pull Request.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

---

<div align="center">

**VMware Screen Monitor**

Made with Python and Discord.py.

[Repository](https://github.com/TomoBao/VMware-Screen-Monitor)

</div>
