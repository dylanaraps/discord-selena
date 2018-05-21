"""
Selena - A bot for Discord.
"""
import configparser
import os
import shutil
import subprocess
import sys

import discord


CONFIG = configparser.ConfigParser()
BOT = discord.Client()
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

    await BOT.send_message(LOG_CHANNEL, embed=make_embed(m, "sent"))


@BOT.event
async def on_message_delete(m):
    """Log deleted messages."""
    if m.author.bot:
        return

    if m.channel.id in CONFIG.get("channel", "exclude_channels"):
        return

    await BOT.send_message(LOG_CHANNEL, embed=make_embed(m, "deleted"))


@BOT.event
async def on_message_edit(r, m):
    """Log deleted messages."""
    if m.author.bot:
        return

    if m.channel.id in CONFIG.get("channel", "exclude_channels"):
        return

    m.content = "%s\n=\n%s" % (r.content, m.content)
    await BOT.send_message(LOG_CHANNEL, embed=make_embed(m, "edited"))


def msg_icon(msg_type):
    """Get the icon to use for the msg type."""
    return {
        "sent":     ":e_mail:",
        "edited":   ":pencil:",
        "deleted":  ":wastebasket:",
    }.get(msg_type, ":shrug:")


def msg_color(msg_type):
    """Get the color to use for the msg type."""
    return {
        "sent":     0x4caf50,
        "edited":   0xffc107,
        "deleted":  0xff5252,
    }.get(msg_type, 0xffffff)


def make_embed(m, msg_type="sent"):
    """Create an embed."""
    title = "%s Message %s by __%s__ in #%s" \
        % (msg_icon(msg_type), msg_type, m.author, m.channel)
    conte = "```fix\n%s %s\n```" \
        % (m.content, ", ".join([attach["url"] for attach in m.attachments]))

    embed = discord.Embed(title=title,
                          description=conte,
                          color=msg_color(msg_type))
    return embed.set_footer(text="MSG ID: %s, ID: %s" % (m.id, m.author.id))


def get_config():
    """Find the config file."""
    home = os.path.expanduser("~")
    user_config = os.path.join(home, ".config", "selena", "config.ini")

    if os.path.isfile(user_config):
        return user_config

    return "config.ini"


def main():
    """Main function."""
    CONFIG.read(get_config())

    if not CONFIG.get("auth", "token"):
        print("error: Token not found.")
        sys.exit(1)

    if shutil.which("git"):
        print("info: Updating bot.")
        subprocess.run(["git", "pull"])

    BOT.run(CONFIG.get("auth", "token"))


main()
