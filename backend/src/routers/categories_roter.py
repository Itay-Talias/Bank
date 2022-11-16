from fastapi import APIRouter, HTTPException, status, Depends
from src.db.dal_sql import get_db_connector
from src.db.dal import DAL
import pymysql as mysql


router = APIRouter()


@router.get("/categories", status_code=200)
def get_categories(db: DAL = Depends(get_db_connector)):
    try:
        categories = db.get_all_categories()
    except mysql.MySQLError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=e)
    return list(map(lambda m: m["category"], categories))
