
# VMware Screen Monitor

A Python Discord bot for a Windows VMware monitoring lab.

## Features

- VM status monitoring
- Predefined diagnostic commands
- HTTPS file downloads with basic restrictions
- Locally confirmed one-time screenshot workflow
- Discord voice channel connection and disconnection

## Requirements

- Python 3.10+
- Windows VM
- Discord bot application

## Installation

```bash
git clone https://github.com/TomoBao/VMware-Screen-Monitor.git
cd VMware-Screen-Monitor
python -m pip install -r requirements.txt
```

Copy `config.example.py` to `config.py` and configure your own credentials locally.

## Run

```bash
python bot.py
```

## Screenshot workflow

Run `python screenmonitor.py` inside the VM and confirm locally before capturing and uploading a screenshot.

## Security

- Never commit bot tokens or webhook URLs.
- Remote commands are restricted to predefined diagnostics.
- Screenshots require local confirmation.
- Downloaded files are not automatically executed.
