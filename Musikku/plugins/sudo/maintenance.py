#
# Copyright (C) 2021-2022 by kenkansaja@Github, < https://github.com/kenkansaja >.
#
# This file is part of < https://github.com/kenkansaja/Musikku > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/kenkansaja/Musikku/blob/master/LICENSE >
#
# All rights reserved.

from pyrogram import filters
from pyrogram.types import Message

from strings import get_command
from Musikku import app
from Musikku.misc import SUDOERS
from Musikku.utils.database import add_off, add_on
from Musikku.utils.decorators.language import language

# Commands
MAINTENANCE_COMMAND = get_command("MAINTENANCE_COMMAND")


@app.on_message(filters.command(MAINTENANCE_COMMAND) & SUDOERS)
@language
async def maintenance(client, message: Message, _):
    usage = _["maint_1"]
    if len(message.command) != 2:
        return await message.reply_text(usage)
    message.chat.id
    state = message.text.split(None, 1)[1].strip()
    state = state.lower()
    if state == "enable":
        user_id = 1
        await add_on(user_id)
        await message.reply_text(_["maint_2"])
    elif state == "disable":
        user_id = 1
        await add_off(user_id)
        await message.reply_text(_["maint_3"])
    else:
        await message.reply_text(usage)
