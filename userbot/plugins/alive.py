# For @TeleBotHelp
"""Check if your userbot is working."""
import asyncio
import requests
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd


DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "No name set yet, check pinned in @TeleBotHelp"

@command(outgoing=True, pattern="^.alive$")
async def amireallyalive(alive):
    """ For .alive command, check if the bot is running.  """
    
    await borg.send_message(alive.chat_id, f"**Welcome To TeleBot **"
f"**`Hey! I'm alive. All systems online and functioning normally!`**"
f"` 🔸 Telethon version:` **1.15.0**\n` 🔹 Python:` **3.8.3**"
f"` 🔸 More info:` [TeleBot](https://telegra.ph/TeleBot-07-08)"
f"` 🔹 Bot created by:` [Aditya 🇮🇳](tg://user?id=719195224)"
f"` 🔸 Database Status:` **All OK 👌!**"
f"` 🔹 My pro owner`: {DEFAULTUSER}"
f"[✨ GitHub Repository ✨](https://github.com/xditya/TeleBot)", link_preview = False)

    #await borg.forward_messages(alive.chat_id, 167, -1001195912925)
    await alive.delete()
