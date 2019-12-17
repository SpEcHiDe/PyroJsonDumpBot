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


import os


# the secret configuration specific things
if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config

import pyrogram
logging.getLogger("pyrogram").setLevel(logging.WARNING)


from events.new_message_event import new_message_event


if __name__ == "__main__":
    # create download directory, if not exist
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
    app = pyrogram.Client(
        "PyroJsonDumpBot",
        bot_token=Config.TG_BOT_TOKEN,
        api_id=Config.APP_ID,
        api_hash=Config.API_HASH
    )
    app.add_handler(pyrogram.MessageHandler(new_message_event))
    app.run()
