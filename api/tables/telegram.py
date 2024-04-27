from piccolo.columns.column_types import (
    Boolean,
    ForeignKey,
    Integer,
    LazyTableReference,
    Timestamp,
    Varchar,
)
from piccolo.columns.m2m import M2M

# from piccolo.engine.postgres import PostgresEngine
from piccolo.engine.sqlite import SQLiteEngine
from piccolo.table import Table

from .patches import BetterTable

DB = SQLiteEngine(path="jdanbot.db")


class Pidor(Table, db=DB):
    id = Integer(primary_key=True)
    count = Integer()
    latest_time = Timestamp()
    is_allowed = Boolean(default=True)

    chats: list["Chat"] = M2M(
        LazyTableReference("ChatPidor", module_path=__name__)
    )


class Chat(BetterTable, Table, db=DB):
    username = Varchar(null=True)
    title = Varchar()
    members: list["User"] = M2M(
        LazyTableReference("Member", module_path=__name__)
    )
    pidors: list[Pidor] = M2M(
        LazyTableReference("ChatPidor", module_path=__name__)
    )


class User(BetterTable, Table, db=DB):
    username = Varchar(null=True)
    first_name = Varchar()
    last_name = Varchar(null=True)
    chats: list["Chat"] = M2M(
        LazyTableReference("Member", module_path=__name__)
    )


class Member(BetterTable, Table, db=DB):
    user = ForeignKey(User)
    chat = ForeignKey(Chat)
    iq = Integer(default=200)


class ChatPidor(Table, db=DB):
    chat = ForeignKey(Chat)
    pidor = ForeignKey(Pidor)
