from typing import Annotated, Any

from fastapi import Body, Depends, FastAPI
from piccolo.engine.sqlite import SQLiteEngine

from .tables.command import Command
from .tables.connection import load_users
from .tables.telegram import Chat, Member, Pidor, User, ChatPidor

DB = SQLiteEngine()

app = FastAPI()


async def transaction():
    async with DB.transaction() as transaction:
        yield transaction


@app.get("/user/test")
async def update_():
    await load_users()

    return {"status": "ok"}


@app.get("/member/all", dependencies=[Depends(transaction)])
async def return_alles_usera():
    return await Chat.select(
        Chat.title,
        Chat.members(User.first_name, User.last_name, User.iq),
        Chat.pidors(Pidor.count, Pidor.latest_time),
    )


@app.post("/user/get/{id}")
async def method_get_user_by(
    body: Annotated[Any, Body(alias="BodyAlias")], id: int
):
    return await User.get_or_update(id, body)


@app.get("/user/get/{id}")
async def method_get_user(id: int):
    return await User.get(id)


@app.post("/chat/get/{id}")
async def method_get_chat_by(
    body: Annotated[Any, Body(alias="BodyAlias")], id: int
):
    print(body)

    return await Chat.get_or_update(id, body)


@app.get("/chat/get/{id}")
async def method_get_chat(id: int):
    return await Chat.get(id)


@app.post("/member/get/{user_id}@{chat_id}")
async def method_get_member_by(
    user_id: int,
    chat_id: int,
):
    print(user_id, chat_id)

    member = await Member.objects().get_or_create(
        (Member.user == user_id) & (Member.chat == chat_id)
    )

    return await Member.select(
        Member.chat.all_columns(), Member.user.all_columns(), Member.iq
    ).output(nested=True)


@app.get("/member/get/{id}")
async def method_get_member(id: int):
    return await Member.get(id)


@app.get("/info")
async def method_get_info():
    return dict(name="japi-nigthly", version="0.0.1", system="alpine")


@app.get("/stats")
async def method_get_stats():
    return dict(users=200, commands=5889)
