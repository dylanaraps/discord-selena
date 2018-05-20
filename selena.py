"""
Selena - A bot for Discord.
"""
import os
import shutil
import subprocess
import sys

from discord.ext.commands import Bot


TOKEN = os.environ.get("DTOKEN")
BOT = Bot(description="Selena", command_prefix="selena")


@BOT.event
async def on_message(m):
    """Log all messages."""
    if m.author.bot:
        return

    if m.channel.id == "447524267199037451":
        return

    channel = BOT.get_channel("447547444566163457")
    await BOT.send_message(channel, log_msg(m))


@BOT.event
async def on_message_delete(m):
    """Log deleted messages."""
    if m.author.bot:
        return

    if m.channel.id == "447524267199037451":
        return

    channel = BOT.get_channel("447547444566163457")
    await BOT.send_message(channel, log_msg(m, "DELETED"))


@BOT.event
async def on_message_edit(_, m):
    """Log deleted messages."""
    if m.author.bot:
        return

    if m.channel.id == "447524267199037451":
        return

    channel = BOT.get_channel("447547444566163457")
    await BOT.send_message(channel, log_msg(m, "EDITED"))


def log_msg(m, msg_type="MSG"):
    """Log message in specific format."""
    msg = "__%s__ [#%s] **@%s** \n```%s" \
        % (msg_type, m.channel, m.author, m.content)
    msg += ", ".join([attach["url"] for attach in m.attachments])
    msg += "```"
    return msg


def main():
    """Main function."""
    if not TOKEN:
        print("error: Token not found.")
        sys.exit(1)

    if shutil.which("git"):
        print("info: Updating bot.")
        subprocess.run(["git", "pull"])

    BOT.run(TOKEN)


main()
