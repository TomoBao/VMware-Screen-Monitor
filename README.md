# VMware Screen Monitor

<p align="center">
  <img src="assets/banner.png" alt="VMware Screen Monitor Banner" width="800">
</p>

<p align="center">
  **A Python-based Discord monitoring project for Windows VMware environments.**
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-blue?logo=python" alt="Python">
  <img src="https://img.shields.io/badge/Platform-Windows-blue?logo=windows" alt="Windows">
  <img src="https://img.shields.io/badge/Discord-Bot-5865F2?logo=discord" alt="Discord">
  <img src="https://img.shields.io/badge/License-MIT-green" alt="MIT License">
</p>

---

## About

**VMware Screen Monitor** is an open-source Python project designed for monitoring and performing authorized diagnostic operations in Windows VMware lab environments through Discord.

The project uses a Discord bot as an interface for interacting with your configured Windows lab machine.

**Default project directory:**

```text
C:\VMLab
```

## Screenshots

### VMware Windows Environment

![VMware Screen Monitor Windows Environment](assets/example.png)

### Discord Bot

![VMware Screen Monitor Discord Example](assets/example2.png)

## Features

- Discord bot integration
- Windows system monitoring
- System status reporting
- Diagnostic command interface
- Screenshot workflow with local confirmation
- HTTPS file downloads
- Discord voice channel connection
- Webhook notifications

## Discord Commands

| Command | Description |
|---|---|
| `/status` | Display system status |
| `/runcmd` | Run supported diagnostic commands |
| `/ss` | Start the screenshot workflow |
| `/download` | Download a file from an HTTPS URL |
| `/share` | Connect the bot to a voice channel |
| `/leave` | Disconnect the bot from a voice channel |

Command availability depends on the installed version and configuration.

## Requirements

- Windows 10 or later
- Python 3.10+
- VMware Workstation or compatible VMware environment
- Git
- Discord account
- Discord bot application

## Installation

### 1. Clone the repository

Open PowerShell or Command Prompt:

```powershell
git clone https://github.com/TomoBao/VMware-Screen-Monitor.git C:\VMLab
```

### 2. Open the project folder

```powershell
cd C:\VMLab
```

### 3. Install Python dependencies

```powershell
python -m pip install -r requirements.txt
```

### 4. Configure the project

Create your local `config.py` using the example configuration.

Configure the required settings:

- Discord bot token
- Webhook URL
- Discord server ID
- Control channel ID

Never publish your actual credentials.

### 5. Start the bot

Make sure your terminal is inside `C:\VMLab`.

Run:

```powershell
python bot.py
```

## Project Structure

```text
C:\VMLab
│
├── assets/
│   ├── banner.png
│   ├── example.png
│   └── example2.png
│
├── Downloads/
├── Screenshots/
│
├── bot.py
├── config.py
├── local_shell.py
├── monitor.py
├── screenmonitor.py
│
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
```

## Configuration

The project uses `config.py` for local configuration.

Keep the following information private:

- Discord bot token
- Discord webhook URL
- Private server and channel IDs
- Other credentials

For public GitHub distribution, use a sanitized example configuration instead of uploading your private configuration.

## Security

This project is intended for authorized Windows VMware lab environments.

- Only monitor machines you own or have permission to access.
- Restrict diagnostic commands to supported operations.
- Require visible local confirmation before screenshot capture.
- Do not automatically execute downloaded files.
- Protect Discord tokens and webhook URLs.
- Avoid publishing private information in screenshots or logs.

## Contributing

Contributions are welcome!

You can help improve VMware Screen Monitor by:

- Reporting bugs through GitHub Issues.
- Suggesting improvements.
- Submitting pull requests.
- Improving documentation.

## License

VMware Screen Monitor is licensed under the **MIT License**.

See the [LICENSE](LICENSE) file for the full license text.

## Repository

GitHub: [TomoBao/VMware-Screen-Monitor](https://github.com/TomoBao/VMware-Screen-Monitor)

---

<p align="center">
  Made with ❤️ and Python by <a href="https://github.com/TomoBao">TomoBao</a>
</p>
