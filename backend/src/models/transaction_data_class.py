from pydantic import BaseModel


class Transactions(BaseModel):
    transaction_id: int | None
    amount: int
    category: str
    vendor: str
    is_depoist: bool
