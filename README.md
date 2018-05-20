# Discord Selena

A minimal bot to log all Discord messages for
transparency.

This bot logs every message and sends them to another
channel. It’s like the audit log but for messages. The
messages can also be sent to a different server if
you’d like to keep logging separate.


## Dependencies

- python 3.5+
- [discord](https://pypi.org/project/discord/)
  (*python module*)


## Getting Started

**Setup**

- `git clone https://dylanaraps.com/discord-selena`
- `cd discord-selena`
- `mkdir -p ~/.config/selena`
- `cp config.ini ~/.config/selena`

**Bot Token**

- Add your bot token to the config file.

```
token =
```

**Log Channel**

- Change the value to the Channel ID of your logging
  channel.

```
log_channel = 447547444566163457
```

**Exluding Channels**

- Change the list to a list of Channel IDs to exclude.
    - For example: Add all NSFW channel IDs to disable
      logging in NSFW channels.

```
exclude_channels = [440356939256299530, 447524267199037451, 447524102505496576]
```
