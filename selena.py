"""
Selena Gomez - A bot for Discord.
"""
import os
import sys

from discord.ext.commands import Bot


TOKEN = os.environ.get("DTOKEN")
BOT = Bot(description="Selena", command_prefix="selena")


@BOT.event
async def on_message(m):
    """Log all messages."""
    if m.author.bot:
        return

    channel = BOT.get_channel("447547444566163457")
    await BOT.send_message(channel, log_msg(m))


@BOT.event
async def on_message_delete(m):
    """Log deleted messages."""
    if m.author.bot:
        return

    channel = BOT.get_channel("447547444566163457")
    await BOT.send_message(channel, log_msg(m, "DELETED"))


@BOT.event
async def on_message_edit(_, m):
    """Log deleted messages."""
    if m.author.bot:
        return

    channel = BOT.get_channel("447547444566163457")
    await BOT.send_message(channel, log_msg(m, "EDITED"))


def log_msg(m, msg_type="MSG"):
    """Log message in specific format."""
    msg = f"__{msg_type}__ [#{m.channel}] **@{m.author}** \n``` {m.content}"
    msg += ", ".join([attach["url"] for attach in m.attachments])
    msg += "```"
    return msg


def main():
    """Main function."""
    if not TOKEN:
        print("error: Token not found.")
        sys.exit(1)

    BOT.run(TOKEN)


main()
