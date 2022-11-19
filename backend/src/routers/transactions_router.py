from fastapi import APIRouter, HTTPException, status, Request, Depends
from src.db.dal_sql import get_db_connector
from src.db.dal import DAL
import pymysql as mysql
from src.models.transaction_data_class import Transactions
from src.models.user_data_class import User


router = APIRouter()


@router.get("/transactions", status_code=200)
def get_all_transactions(user_id: int = 1, db: DAL = Depends(get_db_connector)):
    try:
        transactions = db.get_all_transactions_by_user(user_id)
    except mysql.MySQLError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=e)
    return transactions


@router.post("/transactions", status_code=201)
async def add_transactions(new_transaction: Transactions, user_id: int = 1, db: DAL = Depends(get_db_connector)):
    try:
        transaction_id = db.add_transaction(new_transaction, user_id)
        new_transaction.transaction_id = transaction_id
        new_transaction.user_id = user_id
    except mysql.MySQLError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=e)
    return new_transaction


@router.delete("/transactions/{transaction_id}", status_code=204)
async def delete_transactions(transaction_id: int = -1, db: DAL = Depends(get_db_connector)):
    try:
        if (transaction_id == -1):
            raise ValueError("transaction_id - empty")
        db.remove_transaction_by_id(transaction_id)
    except mysql.MySQLError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=e)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=e)
    except TypeError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=e)
