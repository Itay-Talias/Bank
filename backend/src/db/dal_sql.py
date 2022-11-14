from src.db.dal import DAL
import pymysql as mysql
from src.db.queries import *
from src.models.transaction_data_class import Transactions

DEFAULT_HOST = "localhost"
DEFAULT_USER = "root"
DEFAULT_DB = "sql_bank"
DEFAULT_PWD = ""


class dalSQL(DAL):
    def __init__(self, user: str = DEFAULT_USER, pwd: str = DEFAULT_PWD, db: str = DEFAULT_DB, host: str = DEFAULT_HOST):
        self.connection = mysql.connect(
            host=host, user=user, password=pwd, db=db, charset="utf8", cursorclass=mysql.cursors.DictCursor)

    def get_all_transactions_by_user(self, user_id: int = 1):
        with self.connection.cursor() as cursor:
            cursor.execute(SELECT_TRANSACTIONS_BY_ID, [user_id])
            result = cursor.fetchall()
            return result

    def remove_transaction_by_id(self, transaction_id: int):
        with self.connection.cursor() as cursor:
            cursor.execute(DELETE_TRANSACTION, [transaction_id])
            self.connection.commit()

    def add_transaction(self, new_transaction: Transactions, user_id: int = 1) -> int:
        with self.connection.cursor() as cursor:
            cursor.execute(ADD_TRANSACTION, [
                           new_transaction.amount, new_transaction.category, new_transaction.vendor, new_transaction.is_depoist, user_id])
            self.connection.commit()
            return cursor.lastrowid


try:
    CONNECTOR = dalSQL()
except Exception as e:
    print(e)
