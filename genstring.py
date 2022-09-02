#
# Copyright (C) 2021-2022 by kenkansaja@Github, < https://github.com/kenkansaja >.
#
# This file is part of < https://github.com/kenkansaja/Musikku > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/kenkansaja/Musikku/blob/master/LICENSE >
#
# All rights reserved.


import asyncio

from pyrogram import Client as c

API_ID = input("\nMasukkan API_ID:\n > ")
API_HASH = input("\nMasukkan API_HASH:\n > ")

print("\n\n Masukkan Nomor Handphone Yang Terdaftar.\n\n")

i = c(":memory:", api_id=API_ID, api_hash=API_HASH)


async def main():
    await i.start()
    ss = await i.export_session_string()
    print("\nDISINI STRINGMU, SALIN, JANGAN DISHARE!!\n")
    print(f"\n{ss}\n")


asyncio.run(main())
