from fastapi import APIRouter, HTTPException, status, Request
from src.db.dal_sql import CONNECTOR
import pymysql as mysql


router = APIRouter()


@router.get("/users/{user_id}", status_code=200)
def get_all_transactions(user_id: int = 1):
    try:
        user = CONNECTOR.get_user_by_id(user_id)
    except mysql.MySQLError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=e)
    return user
