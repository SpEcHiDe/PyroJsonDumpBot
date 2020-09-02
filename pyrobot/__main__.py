#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K


from pyrogram import (
    Client
)
from pyrobot import (
    APP_ID,
    API_HASH,
    TG_BOT_TOKEN
)


if __name__ == "__main__":
    plugins = dict(
        root="events",
    )
    app = Client(
        ":memory:",
        bot_token=TG_BOT_TOKEN,
        api_id=APP_ID,
        api_hash=API_HASH,
        plugins=plugins
    )
    #
    app.set_parse_mode("html")
    #
    app.run()
