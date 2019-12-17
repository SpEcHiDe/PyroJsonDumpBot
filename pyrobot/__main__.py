#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K

# the logging things
import logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
LOGGER = logging.getLogger(__name__)


from pyrobot import (
    TG_BOT_TOKEN,
    APP_ID,
    API_HASH
)

import pyrogram
logging.getLogger("pyrogram").setLevel(logging.WARNING)


if __name__ == "__main__":
    plugins = dict(
        root="events",
    )
    app = pyrogram.Client(
        "PyroJsonDumpBot",
        bot_token=Config.TG_BOT_TOKEN,
        api_id=Config.APP_ID,
        api_hash=Config.API_HASH,
        plugins=plugins
    )
    app.add_handler(pyrogram.MessageHandler(new_message_event))
    app.run()
