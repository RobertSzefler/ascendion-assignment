# A script for initializing the DB (table creation etc)

import asyncio

import models  # noqa
from db import init_db


async def run_init_db():
    await init_db()


asyncio.run(run_init_db())
