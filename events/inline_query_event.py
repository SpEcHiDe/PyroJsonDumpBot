#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K


from io import BytesIO
from pyrogram import Client
from pyrobot import LOGGER
from pyrogram.errors import (
    PeerIdInvalid,
    UserIsBlocked
)


@Client.on_inline_query()
async def new_inline_query(client, inline_query):
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
        await inline_query.answer(
            results=[],
            cache_time=0,
            is_gallery=False,
            is_personal=True,
            next_offset="",
            switch_pm_text="please /start bot, first",
            switch_pm_parameter="bot_not_started"
        )
        return False
    except Exception as e:
        LOGGER.info(str(e))
        with BytesIO(str.encode(str(inline_query))) as out_file:
            out_file.name = "json.text"
            await client.send_document(
                chat_id=inline_query.from_user.id,
                document=out_file,
                caption=str(e),
                disable_notification=True,
            )
