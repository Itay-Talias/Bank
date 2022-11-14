from fastapi import APIRouter, HTTPException, status
from backend.src.db.dal_sql import CONNECTOR
import pymysql as mysql


router = APIRouter()


@router.get("/transactions", status_code=200)
def get_all_transactions():
    try:
        CONNECTOR.get_all_transactions()
    except mysql.MySQLConnectionError as e:
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail=e)


@router.post("/transactions", status_code=201)
def add_transactions():
    pass


@router.delete("/transactions", status_code=204)
def add_transactions():
    pass
