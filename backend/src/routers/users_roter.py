from fastapi import APIRouter, HTTPException, status, Depends
from src.db.dal_sql import get_db_connector
from src.db.dal import DAL
import pymysql as mysql


router = APIRouter()


@router.get("/users/{user_id}", status_code=200)
def get_user(user_id: int = 1, db: DAL = Depends(get_db_connector)):
    try:
        user = db.get_user_by_id(user_id)
    except mysql.MySQLError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=e)
    return user
