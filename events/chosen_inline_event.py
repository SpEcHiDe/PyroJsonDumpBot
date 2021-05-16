from io import BytesIO
from pyrogram import Client
from pyrobot import LOGGER
from pyrogram.errors import (
    PeerIdInvalid,
    UserIsBlocked,
    MessageTooLong
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
    except MessageTooLong:
        with BytesIO(str.encode(str(inline_query))) as out_file:
            out_file.name = "json.text"
            await client.send_document(
                chat_id=inline_query.from_user.id,
                document=out_file,
                caption=str(e),
                disable_notification=True,
            )
