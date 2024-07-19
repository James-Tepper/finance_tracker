import jwt
from api.dtos.accounts import AccountDTO
from fastapi import APIRouter, Depends, HTTPException, Response, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordRequestForm

from app.server.api.services import auth
from app.server.api.services.auth import AuthResponse
from app.server.repositories import accounts
from app.server.repositories.accounts import Account

router = APIRouter(default_response_class=Response)


@router.post("/users/register")
async def register() -> Response: ...


@router.post("/users/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()) -> JSONResponse:
    auth_response = await auth.authenticate_user(
        username=form_data.username, password=form_data.password
    )

    auth_status_code = auth_response["status_code"]

    if auth_status_code is not status.HTTP_200_OK:
        raise HTTPException(
            status_code=auth_status_code, detail="Login Error Occured"
        )

    account = jsonable_encoder(auth_response["account"])

    return JSONResponse(status_code=auth_status_code, content=account)


@router.get("/users/{account_id}")
async def get_account(account_id: int) -> JSONResponse:
    try:
        account = await accounts.fetch_by_account_id(account_id)
    except:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )

    assert account is not None

    account_dto = AccountDTO(
        account_id=account["account_id"],
        username=account["username"],
        email=account["email"],
        first_name=account["first_name"],
        last_name=account["last_name"],
        country=account["country"],
    )

    account_dto_json = jsonable_encoder(account_dto)

    return JSONResponse(status_code=status.HTTP_200_OK, content=account_dto_json)
