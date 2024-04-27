import asyncio

from .database import run_db
from .tables import Chat, ChatPidor, Member, Pidor, User

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)


async def startup():
    await run_db()


async def main():
    await startup()

asyncio.get_event_loop().run_until_complete(main())