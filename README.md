# Telegram MtProto meta-data

A Telegram robot based on [Pyrogram](https://github.com/pyrogram/pyrogram)

## installing

### The Easy Way

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

### The Legacy Way
Simply clone the repository and run the main file:

```sh
git clone https://github.com/SpEcHiDe/PyroJsonDumpBot.git
cd PyroJsonDumpBot
python3 -m venv venv
. ./venv/bin/activate
pip install -r requirements.txt
export APP_ID=6 API_HASH="eb06d4abfb49dc3eeb1aeb98ae0f581e" TG_BOT_TOKEN="93372553:AAFNrcXeRFJGIaSsQA4wf81JX7TgQZQJmzI"
python3 -m pyrobot
```


### Variable Explanations

##### Mandatory Variables

* `TG_BOT_TOKEN`: Create a bot using [@BotFather](https://telegram.dog/BotFather), and get the Telegram API token.

* `APP_ID`
* `API_HASH`: Get these two values from [my.telegram.org/apps](https://my.telegram.org/apps).
  * N.B.: if Telegram is blocked by your ISP, try our [Telegram bot](https://telegram.dog/UseTGXBot) to get the IDs.


## Credits, and Thanks to

* [Dan Tès](https://telegram.dog/haskell) for his [Pyrogram Library](https://github.com/pyrogram/pyrogram)
