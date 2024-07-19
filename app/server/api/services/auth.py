from enum import IntEnum
from typing import TypedDict
from fastapi import status
import password_service
from dtos.accounts import AccountPasswordHandlerDTO
from repositories import accounts


class AuthResponseCode(IntEnum):
    SUCCESSFUL = status.HTTP_200_OK
    UNAUTHORIZED = status.HTTP_401_UNAUTHORIZED
    NOT_FOUND = status.HTTP_404_NOT_FOUND


class AuthResponse(TypedDict):
    status_code: AuthResponseCode
    account: AccountPasswordHandlerDTO | None


async def authenticate_user(
    password: str, username: str | None = None, email: str | None = None
) -> AuthResponse:

    assert email and username
    assert email is not None and username is not None

    if username:
        account = await accounts.fetch_by_username(username)
    else:
        account = await accounts.fetch_by_email(email)

    if account is None:
        return AuthResponse(status_code=AuthResponseCode.NOT_FOUND, account=None)

    if not password_service.check_password(
        password=password, hashword=account["password"]
    ):
        return AuthResponse(status_code=AuthResponseCode.UNAUTHORIZED, account=None)

    else:
        return AuthResponse(
            status_code=AuthResponseCode.SUCCESSFUL,
            account=AccountPasswordHandlerDTO(
                account_id=account["account_id"],
                password=account["password"],
            ),
        )
