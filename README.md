# Selena

[![Discord](https://img.shields.io/discord/440354555197128704.svg)](https://discord.gg/BtnTPFF)
[![Build Status](https://travis-ci.org/dylanaraps/pywal.svg?branch=master)](https://travis-ci.org/dylanaraps/pywal)
[![MIT licensed](https://img.shields.io/badge/license-MIT-blue.svg)](./LICENSE.md)
[![Donate](https://img.shields.io/badge/donate-patreon-yellow.svg)](https://www.patreon.com/dyla)

A minimal bot to log all Discord messages for
transparency.

This bot logs every message and sends them to another
channel. It’s like the audit log but for messages. The
messages can also be sent to a different server if
you’d like to keep logging separate.


## Dependencies

- python 3.5+
- discord-rewrite


## Getting Started

**Setup**

```sh
git clone https://dylanaraps.com/discord-selena`
cd discord-selena
mkdir -p ~/.config/selena
cp config.ini ~/.config/selena
```

**Bot Token**

- Add your bot token to the config file.

```ini
token =
```

**Log Channel**

- Change the value to the Channel ID of your logging
  channel.

```ini
log_channel = 447547444566163457
```
