from typing import Union
import re
import os
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import config
from config import GROUP_USERNAME, CHANNEL_USERNAME


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="✚ ᴀᴅᴅ мє το ʏουя gяουρ ✚",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text=" ᴄᴏᴍᴍᴀɴᴅ ",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text=" ꜱᴇᴛᴛɪɴɢꜱ ", callback_data="settings_helper"
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="нοᴡ το υѕє мє? ϲοммαиᴅ мєиυ.", callback_data="settings_back_helper"
            )
        ],
        [
            InlineKeyboardButton(
                text="🥀 ɢяουᴘ 💥", url=f"http://t.me/TaitanXSupport",
            ),
            InlineKeyboardButton(
                text="🥀 ᴄнαииєʟ 💥", url=f"https://t.me/TaitanXbot",
            )
        ],
        [
            InlineKeyboardButton(
                text="✚ ᴀᴅᴅ мє το ʏουя gяουρ ✚",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="✨ οωиєя ✨",
                url=f"https://t.me/taitangamer",
            ),
            InlineKeyboardButton(
                text="💮 ѕουяϲє 💮",
                url=f"https://t.me/taitangamer",
            )
        ],
     ]
    return buttons
