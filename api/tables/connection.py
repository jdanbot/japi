from . import Chat, ChatPidor, Command, Member, Pidor, User

# class GenreToBandT(BaseModel, nested=True):
#     band: Band
#     genre: Genre


# BandModel = create_pydantic_model(GenreToBandT, nested=True)


async def load_users():
    await User.create_table(if_not_exists=True)
    await Chat.create_table(if_not_exists=True)
    await Member.create_table(if_not_exists=True)
    await ChatPidor.create_table(if_not_exists=True)
    await Pidor.create_table(if_not_exists=True)

    await User.insert(
        User(first_name="Ankapow"),
        User(first_name="Militarow", last_name="Karl"),
        User(first_name="Dunkelnow"),
    )

    await Pidor.insert(
        Pidor(id=1, count=200),
        Pidor(id=2, count=400),
        Pidor(id=3, count=88),
    )

    await Chat.insert(
        Chat(title="Deutsche Faille"),
        Chat(title="Unser Kampf fuer Imperialismus"),
        Chat(title="ZVTV"),
    )

    await Member.insert(
        Member(user=1, chat=1),
        Member(user=1, chat=2),
        Member(user=2, chat=2),
        Member(user=3, chat=1),
        Member(user=3, chat=3),
    )

    await ChatPidor.insert(
        ChatPidor(chat=1, pidor=1),
        ChatPidor(chat=1, pidor=2),
        ChatPidor(chat=3, pidor=3),
    )
