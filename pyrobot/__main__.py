from pyrogram import (
    Client
)
from pyrogram.enums import ParseMode
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
        plugins=plugins,
        parse_mode=ParseMode.HTML
    )
    app.run()
