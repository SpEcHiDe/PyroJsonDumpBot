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
import time

# the secret configuration specific things
if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config

import pyrogram
logging.getLogger("pyrogram").setLevel(logging.WARNING)


async def new_message_event(client, message):
    try:
        await message.reply_text(
            message,
            quote=True,
            disable_web_page_preview=True,
            disable_notification=True,
        )
    except Exception as e:
        work_area = os.path.join(
            Config.TMP_DOWNLOAD_DIRECTORY,
            str(time.time())
        )
        # create download directory, if not exist
        if not os.path.isdir(work_area):
            os.makedirs(work_area)
        temp_writing_file = os.path.join(
            work_area,
            "json.text"
        )
        with open(temp_writing_file, "w+", encoding="utf8") as out_file:
            out_file.write(str(message))
        await message.reply_document(
            document=temp_writing_file,
            caption=str(e),
            disable_notification=True,
            quote=True
        )
        os.remove(temp_writing_file)


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
