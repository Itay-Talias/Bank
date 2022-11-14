from fastapi import APIRouter, HTTPException, status, Request
from src.db.dal_sql import CONNECTOR
import pymysql as mysql
from src.models.transaction_data_class import Transactions


router = APIRouter()


@router.get("/transactions", status_code=200)
def get_all_transactions():
    try:
        transactions = CONNECTOR.get_all_transactions_by_user()
    except mysql.MySQLError as e:
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail=e)
    return transactions


@router.post("/transactions", status_code=201)
async def add_transactions(new_transaction: Transactions):
    try:
        transaction_id = CONNECTOR.add_transaction(new_transaction)
        new_transaction.transaction_id = transaction_id
    except mysql.MySQLError as e:
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail=e)
    return new_transaction


@router.delete("/transactions", status_code=204)
async def add_transactions(request: Request):
    try:
        transaction_id = await request.json()
        if (len(transaction_id) == 0):
            raise ValueError("transaction_id - empty")
        CONNECTOR.remove_transaction_by_id(transaction_id=transaction_id["id"])
    except mysql.MySQLError as e:
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail=e)
    except mysql.ValueError as e:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, detail=e)
