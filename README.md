# VMware Screen Monitor

<div align="center">
  <img src="assets/banner.png" alt="VMware Screen Monitor Banner" width="100%">
  
  **A Python-powered Discord bot for monitoring your Windows VMware lab.**
  
  ![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)
  ![Platform](https://img.shields.io/badge/Platform-Windows-0078D6?logo=windows)
  ![Discord](https://img.shields.io/badge/Discord-Bot-5865F2?logo=discord)
  ![License](https://img.shields.io/badge/License-MIT-green)
</div>

---

## About

VMware Screen Monitor is a Python Discord bot designed for monitoring and managing a Windows virtual machine in a personal VMware lab.

It connects your Windows VM to a Discord server and provides useful diagnostic information through slash commands.

## Features

| Feature | Description |
|---|---|
| VM Monitoring | View CPU, RAM, disk, and system information |
| Diagnostic Commands | Run predefined Windows diagnostic commands |
| File Downloads | Download small files from public HTTPS URLs |
| Screenshot Workflow | Capture and upload screenshots after local confirmation |
| Voice Connection | Connect or disconnect the bot from a Discord voice channel |
| Webhook Notifications | Send bot status notifications to Discord |

## Commands

| Command | Description |
|---|---|
| `/status` | Display VM system information |
| `/runcmd` | Run a predefined diagnostic command |
| `/download` | Download a file from an HTTPS URL |
| `/ss` | Request a locally confirmed screenshot |
| `/share` | Connect the bot to your current voice channel |
| `/leave` | Disconnect the bot from voice |

## Requirements

- Windows 10 or later
- VMware Workstation or another compatible VMware environment
- Python 3.10 or later
- A Discord account and Discord bot application
- Internet connection

## Installation

### 1. Clone the repository

```bash
git clone YOUR_REPOSITORY_URL
cd VMware-Screen-Monitor
```

### 2. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 3. Configure the bot

Copy `config.example.py` and rename the copy to `config.py`.

Fill in your own:

- Discord bot token
- Discord webhook URL
- Discord server ID
- Control channel ID

**Never publish your real credentials on GitHub.**

### 4. Start the bot

```bash
python bot.py
```

If everything is configured correctly, the bot should connect to Discord and synchronize its slash commands.

## Screenshot Workflow

The `/ss` command sends a screenshot request.

To capture a screenshot:

1. Run `python screenmonitor.py` inside the Windows VM.
2. Review the local confirmation prompt.
3. Type `YES` to authorize one screenshot.
4. The screenshot is saved in `Screenshots/` and uploaded to the configured webhook.

Screenshots are not captured silently or continuously.

## Project Structure

```text
VMware-Screen-Monitor/
│
├── assets/
│   └── banner.png
│
├── Downloads/
│   └── .gitkeep
│
├── Screenshots/
│   └── .gitkeep
│
├── bot.py
├── config.py
├── config.example.py
├── local_shell.py
├── monitor.py
├── screenmonitor.py
│
├── requirements.txt
├── README.md
├── .gitignore
└── LICENSE
```

## Security

- Keep Discord tokens and webhook URLs private.
- Remote diagnostic commands are restricted to predefined commands.
- Screenshot uploads require local confirmation.
- Downloaded files are not automatically executed.
- Do not use this project to monitor devices without authorization.

## Limitations

- `/share` connects the bot to a voice channel; it does not automatically start Discord Go Live.
- `/ss` requires local execution and confirmation inside the VM.
- Download restrictions are basic safeguards, not a guarantee against malicious files.

## Contributing

Contributions, bug reports, and suggestions are welcome!

1. Fork this repository.
2. Create a feature branch.
3. Commit your changes.
4. Open a Pull Request.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

---

<div align="center">

**VMware Screen Monitor**

Made with Python and Discord.py.

</div>
