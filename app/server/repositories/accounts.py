from datetime import datetime
from typing import TypedDict, cast

from app.server import clients

READ_PARAMS = """\
    account_id
    username,
    email,
    first_name,
    last_name,
    password,
    country,
    created_at,
    updated_at
"""


class Account(TypedDict):
    account_id: int
    username: str
    email: str
    first_name: str
    last_name: str
    password: str
    country: str
    created_at: datetime
    updated_at: datetime


async def create(
    username: str,
    email: str,
    first_name: str,
    last_name: str,
    password: str,
    country: str,
) -> Account:
    account = await clients.database.fetch_one(
        query=f"""
        INSERT INTO accounts
        username, email,
        first_name, last_name, password, country)
        VALUES (:username, :email,
        :first_name, :last_name, :password, :country)
        RETURNING {READ_PARAMS}
        """,
        values={
            "username": username,
            "email": email,
            "first_name": first_name,
            "last_name": last_name,
            "password": password,
            "country": country,
        },
    )
    assert account is not None
    return cast(Account, account)


async def fetch_by_username(username: str) -> Account | None:
    account = await clients.database.fetch_one(
        query=f"""
            SELECT {READ_PARAMS}
            FROM accounts WHERE username = :username
            """,
        values={
            "username": username,
        },
    )
    return cast(Account, account) if account is not None else None


async def fetch_by_email(email: str) -> Account | None:
    account = await clients.database.fetch_one(
        query=f"""
            SELECT {READ_PARAMS}
            FROM accounts WHERE email = :email
            """,
        values={
            "email": email,
        },
    )
    return cast(Account, account) if account is not None else None



async def fetch_by_account_id(account_id: int) -> Account | None:
    account = await clients.database.fetch_one(
        query=f"""
            SELECT {READ_PARAMS}
            FROM accounts WHERE account_id = :account_id
            """,
        values={
            "account_id": account_id,
        },
    )
    return cast(Account, account) if account is not None else None

