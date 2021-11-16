[![Stargazers][stars-shield]][stars-url]

## About

A discord bot that interacts directly with a Windows 10 computer. Written in Python

### Built With

* [Python 3](https://www.python.org/)
* [discord.py](https://github.com/Rapptz/discord.py)
* [discord-interactions](https://github.com/goverfl0w/discord-interactions)
* [PyYAML](https://pyyaml.org/)

### Prerequisites

* discord.py
  ```sh
  pip install discord.py
  ```
* discord-interactions
  ```sh
  pip install discord-py-interactions
  ```
* PyYAML
  ```sh
  pip install PyYAML
  ```

### Setup

1. Clone the repo
   ```sh
   git clone https://github.com/k200-dev/DiscordPC
   ```
2. Rename config-example.yaml to config.yaml and edit the values 
   ```yaml
   TOKEN: 'DISCORD_AUTH_TOKEN_HERE'
   USERNAME: 'YOUR_NAME_HERE'
   BANNEDWORDS: ["BANNED_WORDS_FROM_SEARCH_HERE"]
   BANNEDPROCESSES: ["BANNED_PROCESSES_HERE"]
   SERVERIP: "PINGED_SERVER_IP_HERE"
   ```
3. Create a file called quotes.txt in the directory

## Usage

Run `index.py` through python or a process manager like pm2

![Image of the RAT server](https://files.k200.site/github-Windows-Python-RAT-example.png)

[stars-shield]: https://img.shields.io/github/stars/k200-dev/DiscordPC.svg?style=for-the-badge
[stars-url]: https://github.com/k200-dev/DiscordPC/stargazers
