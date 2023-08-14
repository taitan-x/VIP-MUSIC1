from typing import Union
import asyncio
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def help_pannel(_, START: Union[bool, int] = None):
    first = [
        InlineKeyboardButton(
            text=_["CLOSEMENU_BUTTON"], callback_data=f"close"
        )
    ]
    second = [
        InlineKeyboardButton(
            text=_["BACK_BUTTON"],
            callback_data=f"settingsback_helper",
        ),
        InlineKeyboardButton(
            text=_["CLOSEMENU_BUTTON"], callback_data=f"close"
        ),
        InlineKeyboardButton(
            text="★ мοяє ★", callback_data="help_callback hb13"
        ),
    ]
    mark = second if START else first
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="🍁 α∂мιи 🍁",
                    callback_data="help_callback hb1",
                ),
                InlineKeyboardButton(
                    text="🔺αυτн🔺",
                    callback_data="help_callback hb2",
                ),
            
                InlineKeyboardButton(
                    text="♨️ вℓσ¢к ♨️",
                    callback_data="help_callback hb3",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="📣 gϲαѕτ 📣",
                    callback_data="help_callback hb4",
                ),
                InlineKeyboardButton(
                    text="🚫 gϐαи 🚫",
                    callback_data="help_callback hb12",
                ),
                InlineKeyboardButton(
                    text="🍷ℓγяι¢ѕ🍷",
                    callback_data="help_callback hb5",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="🎙️ρℓαγℓιѕτ🎙️",
                    callback_data="help_callback hb6",
                ),
                InlineKeyboardButton(
                    text="🎸νοιϲє ϲнατ 🎸",
                    callback_data="help_callback hb10",
                ),
            ],
            [
           
                InlineKeyboardButton(
                    text="🕹️ ρℓαγ 🕹️",
                    callback_data="help_callback hb8",
                ),
            
            
                InlineKeyboardButton(
                    text="🍸ѕυ∂ο🍸",
                    callback_data="help_callback hb9",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="⚜️ ѕταяτ ⚜️",
                    callback_data="help_callback hb11",
                ),
            ],
            mark,
        ]
    )
    return upl


def help_back_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["BACK_BUTTON"],
                    callback_data=f"settings_back_helper",
                ),
                InlineKeyboardButton(
                    text=_["CLOSE_BUTTON"], callback_data=f"close"
                ),
                InlineKeyboardButton(
                    text="★ мοяє ★", callback_data="help_callback hb13"
                )

            ]
        ]
    )
    return upl


def private_help_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="🎭 нєℓρ 🎭",
                callback_data="settings_back_helper",
            ),
        ],
    ]
    return buttons

