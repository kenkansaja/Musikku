#
# Copyright (C) 2021-2022 by kenkansaja@Github, < https://github.com/kenkansaja >.
#
# This file is part of < https://github.com/kenkansaja/Musikku > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/kenkansaja/Musikku/blob/master/LICENSE >
#
# All rights reserved.

from motor.motor_asyncio import AsyncIOMotorClient as _mongo_client_
from pymongo import MongoClient

import config

_mongo_async_ = _mongo_client_(config.MONGO_DB_URI)
_mongo_sync_ = MongoClient(config.MONGO_DB_URI)

mongodb = _mongo_async_.Musikku
pymongodb = _mongo_sync_.Musikku
