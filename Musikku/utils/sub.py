from pyrogram.errors import ChatAdminRequired, ChatWriteForbidden, UserNotParticipant
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

from Musikku import app
import config


def ken(func):
    async def wrapper(_, message: Message):
        if not config.MUST_JOIN:  # Not compulsory
            return
        try:
            try:
                await app.get_chat_member(config.MUST_JOIN, message.from_user.id)
            except UserNotParticipant:
                if config.MUST_JOIN.isalpha():
                    link = "https://t.me/" + config.MUST_JOIN
                else:
                    chat_info = await app.get_chat(config.MUST_JOIN)
                    chat_info.invite_link
                try:
                    await app.reply_text(_["subcribe"],
                        disable_web_page_preview=True,
                        reply_markup=InlineKeyboardMarkup(
                            [[InlineKeyboardButton("••ᴊᴏɪɴ••", url=link)]]
                        ),
                    )
                    await message.stop_propagation()
                except ChatWriteForbidden:
                    pass
        except ChatAdminRequired:
            await app.reply_text(
                f"Saya bukan admin di chat MUST_JOIN chat : {config.MUST_JOIN} !"
            )
        return await func(_, message)

    return wrapper
