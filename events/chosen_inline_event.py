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
from pyrogram.errors import (
    PeerIdInvalid,
    UserIsBlocked
)


@Client.on_chosen_inline_result()
async def chosen_inline_result(client, inline_query):
    try:
        await client.send_message(
            chat_id=inline_query.from_user.id,
            text=f"<code>{inline_query}</code>",
            # parse_mode=,
            disable_web_page_preview=True,
            disable_notification=True,
            # reply_to_message_id=,
        )
    except (PeerIdInvalid, UserIsBlocked):
        # this should ideally not happen,
        # but, who knows? :\
        pass
    except Exception as e:
        LOGGER.info(str(e))
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
            out_file.write(str(inline_query))
        await client.send_document(
            chat_id=inline_query.from_user.id,
            document=temp_writing_file,
            caption=str(e),
            disable_notification=True,
        )
        os.remove(temp_writing_file)
