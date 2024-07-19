from server import clients
from getpass import getpass
from enum import StrEnum
import asyncio

class Tables(StrEnum):
    ACCOUNTS = "accounts"
    TRANSACTIONS = "transactions"


async def test_database():
    while True:
        print(table for table in vars(Tables))
        selected_table = input("Select a table from the list above\n")
        if selected_table not in Tables:
            continue

        match selected_table:
            case Tables.ACCOUNTS:
                ...



# def modify_accounts():


if __name__ == "__main__":
    asyncio.run(test_database())
