#
# Copyright (C) 2021-2022 by kenkansaja@Github, < https://github.com/kenkansaja >.
#
# This file is part of < https://github.com/kenkansaja/Musikku > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/kenkansaja/Musikku/blob/master/LICENSE >
#
# All rights reserved.

from pykeyboard import InlineKeyboard
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, Message

from config import BANNED_USERS
from strings import get_command, get_string
from Musikku import app
from Musikku.utils.database import get_lang, set_lang
from Musikku.utils.decorators import (ActualAdminCB, language,
                                         languageCB)

# Languages Available


def lanuages_keyboard(_):
        keyboard = InlineKeyboard(row_width=3)
        keyboard.row(
            InlineKeyboardButton(text="🏴󠁧󠁢󠁥󠁮󠁧󠁿 Inggris", callback_data=f"languages:en"),
            InlineKeyboardButton(text="🇹🇷 Turki", callback_data=f"languages:tr"),
            InlineKeyboardButton(text="🇮🇩 Indonesia", callback_data=f"languages:id"),
        )
        keyboard.row(
            InlineKeyboardButton(text="🇮🇩 Jawa", callback_data=f"languages:jawa"),
            InlineKeyboardButton(text="🇮🇩 Sunda", callback_data=f"languages:sunda"),
        )
        keyboard.row(
            InlineKeyboardButton(text=_["BACK_BUTTON"], callback_data=f"settingsback_helper"),
            InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data=f"close"),
        )
        return keyboard
    


LANGUAGE_COMMAND = get_command("LANGUAGE_COMMAND")


@app.on_message(
    filters.command(LANGUAGE_COMMAND)
    & filters.group
    & ~filters.edited
    & ~BANNED_USERS
)
@language
async def langs_command(client, message: Message, _):
    keyboard = lanuages_keyboard(_)
    await message.reply_text(
        _["setting_1"].format(message.chat.title, message.chat.id),
        reply_markup=keyboard,
    )


@app.on_callback_query(filters.regex("LG") & ~BANNED_USERS)
@languageCB
async def lanuagecb(client, CallbackQuery, _):
    try:
        await CallbackQuery.answer()
    except:
        pass
    keyboard = lanuages_keyboard(_)
    return await CallbackQuery.edit_message_reply_markup(
        reply_markup=keyboard
    )


@app.on_callback_query(
    filters.regex(r"languages:(.*?)") & ~BANNED_USERS
)
@ActualAdminCB
async def language_markup(client, CallbackQuery, _):
    langauge = (CallbackQuery.data).split(":")[1]
    old = await get_lang(CallbackQuery.message.chat.id)
    if str(old) == str(langauge):
        return await CallbackQuery.answer(
            "Anda sudah menggunakan bahasa yang sama", show_alert=True
        )
    await set_lang(CallbackQuery.message.chat.id, langauge)
    try:
        _ = get_string(langauge)
        await CallbackQuery.answer(
            "Berhasil mengubah bahasa Anda.", show_alert=True
        )
    except:
        return await CallbackQuery.answer(
            "Gagal mengubah bahasa atau bahasa dalam pembaruan.",
            show_alert=True,
        )
    await set_lang(CallbackQuery.message.chat.id, langauge)
    keyboard = lanuages_keyboard(_)
    return await CallbackQuery.edit_message_reply_markup(
        reply_markup=keyboard
    )
