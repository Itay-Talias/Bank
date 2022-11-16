from pydantic import BaseModel


class Transactions(BaseModel):
    transaction_id: int | None
    amount: int
    category: str
    vendor: str
    user_id: int | None
