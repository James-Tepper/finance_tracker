from databases import Database as _Database
import settings

class Database(_Database):
    ...


def dsn(
    db_scheme: str,
    db_user: str,
    db_pass: str,
    db_port: int,
    db_host: str,
    db_name: str
):
    return f"{db_scheme}://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}"
