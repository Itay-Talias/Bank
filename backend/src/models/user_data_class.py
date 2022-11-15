from pydantic import BaseModel


class User(BaseModel):
    user_id: int | None
    username: str
    password: str
    balance: int
