"""
Selena Gomez - A bot for Discord.
"""
import datetime
import logging
import os
import sys

from discord.ext.commands import Bot


TOKEN = os.environ.get("DTOKEN")
BOT = Bot(description="Selena Gomez", command_prefix="selena")


@BOT.event
async def on_message(m):
    """Log all messages."""
    log_msg = f"[{m.timestamp}] [#{m.channel}] {m.author}: {m.content} "
    log_msg += ", ".join([attach["url"] for attach in m.attachments])
    logging.info(log_msg)

    await BOT.process_commands(m)


@BOT.event
async def on_message_delete(m):
    """Log deleted messages."""
    log_msg = f"DELETED [{m.timestamp}] [#{m.channel}] {m.author}: {m.content}"
    logging.info(log_msg)

    await BOT.process_commands(m)


@BOT.event
async def on_message_edit(_, m):
    """Log edited messages."""
    log_msg = f"EDITED [{m.timestamp}] [#{m.channel}] {m.author}: {m.content}"
    logging.info(log_msg)

    await BOT.process_commands(m)


def main():
    """Main function."""
    if not TOKEN:
        print("error: Token not found.")
        sys.exit(1)

    os.makedirs("logs", exist_ok=True)
    logging.basicConfig(format=("%(message)s"),
                        level=logging.INFO,
                        filename="logs/%s-log" % (datetime.date.today()),
                        filemode="a")
    BOT.run(TOKEN)


main()
