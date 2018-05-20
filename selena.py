"""
Selena - A bot for Discord.
"""
import configparser
import os
import shutil
import subprocess
import sys

from discord.ext.commands import Bot


def get_config():
    """Find the config file."""
    home = os.path.expanduser("~")
    user_config = os.path.join(home, ".config", "selena", "config.ini")

    if os.path.isfile(user_config):
        return user_config

    return "config.ini"


CONFIG = configparser.ConfigParser()
CONFIG.read(get_config())
BOT = Bot(description=CONFIG.get("bot", "description"),
          command_prefix=CONFIG.get("bot", "prefix"))
LOG_CHANNEL = ""


@BOT.event
async def on_ready():
    """On bot start."""
    global LOG_CHANNEL
    LOG_CHANNEL = BOT.get_channel(CONFIG.get("channel", "log_channel"))


@BOT.event
async def on_message(m):
    """Log all messages."""
    if m.author.bot:
        return

    if m.channel.id in CONFIG.get("channel", "exclude_channels"):
        return

    await BOT.send_message(LOG_CHANNEL, log_msg(m, "MSG"))


@BOT.event
async def on_message_delete(m):
    """Log deleted messages."""
    if m.author.bot:
        return

    if m.channel.id in CONFIG.get("channel", "exclude_channels"):
        return

    await BOT.send_message(LOG_CHANNEL, log_msg(m, "DELETED"))


@BOT.event
async def on_message_edit(_, m):
    """Log deleted messages."""
    if m.author.bot:
        return

    if m.channel.id in CONFIG.get("channel", "exclude_channels"):
        return

    await BOT.send_message(LOG_CHANNEL, log_msg(m, "EDITED"))


def log_msg(m, msg_type):
    """Log message in specific format."""
    return "__%s__ [#%s] **@%s** \n```%s %s```" \
           % (msg_type, m.channel, m.author, m.content,
              ", ".join([attach["url"] for attach in m.attachments]))


def main():
    """Main function."""
    if not CONFIG.get("auth", "token"):
        print("error: Token not found.")
        sys.exit(1)

    if shutil.which("git"):
        print("info: Updating bot.")
        subprocess.run(["git", "pull"])

    BOT.run(CONFIG.get("auth", "token"))


main()
