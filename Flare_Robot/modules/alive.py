import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from Flare_Robot.events import register
from Flare_Robot import telethn as tbot


PHOTO = "https://telegra.ph/file/90959b8d78cf50d7e87d7.jpg"


@register(pattern=("/alive"))
async def awake(event):
    TEXT = "**I,m Sir NightEye** \n\n"
    TEXT += f"**Predicting Future Properly** \n\n"
    TEXT += f"**NightEye: LATEST Version** \n\n"
    TEXT += f"**My Creator: [Freak](http://t.me/Freaking_tag)** \n\n"
    TEXT += f"**For queries Contact in @Foresight_Academy** \n\n"
    TEXT += "**Thanks for adding me here!!**"
    BUTTON = [
        [
            Button.url("📢 Updates", "https://t.me/Foresight_Updates"),
            Button.url("🚑 Support", "https://t.me/ForeSight_Academy"),
        ]
    ]
    await tbot.send_file(event.chat_id, PHOTO, caption=TEXT, buttons=BUTTON)
