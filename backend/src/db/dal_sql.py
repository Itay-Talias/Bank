from src.db.dal import DAL
import pymysql as mysql
from src.db.queries import *

DEFAULT_HOST = "localhost"
DEFAULT_USER = "root"
DEFAULT_DB = "sql_bank"
DEFAULT_PWD = ""


class dalSQL(DAL):
    def __init__(self, user: str = DEFAULT_USER, pwd: str = DEFAULT_PWD, db: str = DEFAULT_DB, host: str = DEFAULT_HOST):
        self.connection = mysql.connect(
            host=host, user=user, password=pwd, db=db, charset="utf8", cursorclass=mysql.cursors.DictCursor)

    def get_all_transactions(self):
        with self.connection.cursor() as cursor:
            cursor.execute(SELECT_ALL_TRANSACTIONS)
            result = cursor.fetchall()
            return result

    def remove_transaction_by_id(self, transaction_id):
        with self.connection.cursor() as cursor:
            cursor.execute(DELETE_TRANSACTION, [transaction_id])
            self.connection.commit()

    def add_transaction(self, amount: int, category: str, vendor: str, is_depoist: bool):
        with self.connection.cursor() as cursor:
            cursor.execute(ADD_TRANSACTION, [
                           amount, category, vendor, is_depoist])
            self.connection.commit()


try:
    CONNECTOR = dalSQL()
except Exception as e:
    print(e)
