#
# Copyright (C) 2021-2022 by kenkansaja@Github, < https://github.com/kenkansaja >.
#
# This file is part of < https://github.com/kenkansaja/Musikku > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/kenkansaja/Musikku/blob/master/LICENSE >
#
# All rights reserved.

import asyncio
import importlib
import sys

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from config import BANNED_USERS
from Musikku import LOGGER, app, userbot
from Musikku.core.call import Musikku
from Musikku.plugins import ALL_MODULES
from Musikku.utils.database import get_banned_users, get_gbanned

loop = asyncio.get_event_loop()


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER("Musikku").error(
            "Tidak Ada Asisten Klien yang Ditentukan Vars!.. Proses Keluar."
        )
        return
    if (
        not config.SPOTIFY_CLIENT_ID
        and not config.SPOTIFY_CLIENT_SECRET
    ):
        LOGGER("MusikkuMusic").warning(
            "Tidak ada Spotify Vars yang ditentukan. Bot Anda tidak akan dapat memainkan kueri spotify."
        )
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("Musikku.plugins" + all_module)
    LOGGER("Musikku.plugins").info(
        "Modul Berhasil Diimpor"
    )
    await userbot.start()
    await Musikku.start()
    get_ah = await app.get_me()
    uh_ah = get_ah.username
    await userbot.one.send_message("musikkugroup", f"@{uh_ah}")
    try:
        await Musikku.stream_call(
            "http://docs.evostream.com/sample_content/assets/sintel1m720p.mp4"
        )
    except NoActiveGroupCall:
        LOGGER("Musikku").error(
            "[ERROR] - \n\nHarap aktifkan Panggilan Suara Grup Logger Anda. Pastikan Anda tidak pernah menutup/mengakhiri panggilan suara di grup log Anda"
        )
        sys.exit()
    except:
        pass
    await Musikku.decorators()
    LOGGER("Musikku").info("Musikku Music Bot Berhasil Dimulai")
    await idle()


if __name__ == "__main__":
    loop.run_until_complete(init())
    LOGGER("Musikku").info("Menghentikan Bot Musikku! Selamat tinggal")
