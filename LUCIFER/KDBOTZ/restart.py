import asyncio
import heroku3
import os
from pyrogram import Client, filters, enums
from info import ADMINS

HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY")
HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME")

async def app_restart():
    heroku = heroku3.from_key(HEROKU_API_KEY)
    app = heroku.apps()[HEROKU_APP_NAME]
    if HEROKU_API_KEY:
        app.restart()
    else:
        return


@Client.on_message(filters.command("restart") & filters.user(ADMINS))
async def restarts(client, message):
    if HEROKU_API_KEY:
        kd = await message.reply_text("Trying to restart...")
        await app_restart()
        await kd.edit("Please Wait Restarting....")
        await asyncio.sleep(3.5)
        await kd.delete()
    else:
        await message.reply_text("Api key not found!")
