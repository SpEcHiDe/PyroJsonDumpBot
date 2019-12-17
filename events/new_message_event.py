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
from pyrogram import Client
from pyrobot import TMP_DOWNLOAD_DIRECTORY


@Client.on_message()
async def new_message_event(client, message):
    try:
        await message.reply_text(
            f"<code>{message}</code>",
            quote=True,
            disable_web_page_preview=True,
            disable_notification=True,
        )
    except Exception as e:
        work_area = os.path.join(
            TMP_DOWNLOAD_DIRECTORY,
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
