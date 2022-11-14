from fastapi import APIRouter, HTTPException, status, Request
from ..db.dal_sql import CONNECTOR
import pymysql as mysql


router = APIRouter()


@router.get("/transactions", status_code=200)
def get_all_transactions():
    try:
        transactions = CONNECTOR.get_all_transactions()
    except mysql.MySQLError as e:
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail=e)
    return transactions


@router.post("/transactions", status_code=201)
async def add_transactions(request: Request):
    pass


@router.delete("/transactions", status_code=204)
def add_transactions():
    pass
