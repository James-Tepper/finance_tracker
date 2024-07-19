from pydantic import BaseModel


class AccountDTO(BaseModel):
    account_id: int
    username: str
    email: str
    first_name: str
    last_name: str
    country: str


class AccountUpdateDTO(BaseModel):
    username: str | None = None
    email: str | None = None
    password: str | None = None
    country: str | None = None


class AccountPasswordHandlerDTO(BaseModel):
    account_id: int
    password: str
