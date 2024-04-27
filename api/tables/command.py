from piccolo.columns.column_types import Integer, Timestamp, Varchar
from piccolo.table import Table


class Command(Table):
    id = Integer(pk=True)

    user_id = Integer()
    chat_id = Integer()

    name = Varchar()
    args = Varchar(null=True)

    runned_at = Timestamp()
