from src.db.dal import DAL
import pymysql as mysql
from src.db.queries import *
from src.models.transaction_data_class import Transactions
from typing import List
from src.models.user_data_class import User
from configuration.db_cofiguration import *


class DalSQL(DAL):
    def __init__(self, user: str = DEFAULT_USER, pwd: str = DEFAULT_PWD, db: str = DEFAULT_DB, host: str = DEFAULT_HOST):
        self.connection = mysql.connect(
            host=host, user=user, password=pwd, db=db, charset="utf8", cursorclass=mysql.cursors.DictCursor, autocommit=True)

    def get_user_by_id(self, user_id: int) -> User:
        with self.connection.cursor() as cursor:
            cursor.execute(SELECT_USER_BY_ID, [user_id])
            result = cursor.fetchone()
            user = User(**result)
            return user

    def get_all_transactions_by_user(self, user_id: int) -> List[Transactions]:
        with self.connection.cursor() as cursor:
            cursor.execute(SELECT_TRANSACTIONS_BY_USER_ID, [user_id])
            result = cursor.fetchall()
            transactions = [Transactions(**t) for t in result]
            return transactions

    def get_transaction_by_id(self, transaction_id: int) -> Transactions:
        with self.connection.cursor() as cursor:
            cursor.execute(SELECT_TRANSACTION_BY_ID, [transaction_id])
            result = cursor.fetchone()
            return Transactions(**result)

    def remove_transaction_by_id(self, transaction_id: int):
        with self.connection.cursor() as cursor:
            transaction = self.get_transaction_by_id(transaction_id)
            self.change_balanceֹ_for_user(
                transaction.amount, transaction.user_id)
            cursor.execute(DELETE_TRANSACTION, [transaction_id])
            self.connection.commit()

    def add_transaction(self, new_transaction: Transactions, user_id: int) -> int:
        with self.connection.cursor() as cursor:
            cursor.execute(ADD_TRANSACTION, [
                           new_transaction.amount, new_transaction.category, new_transaction.vendor, user_id])
            self.connection.commit()
        self.change_balanceֹ_for_user(new_transaction.amount, user_id)
        return cursor.lastrowid

    def change_balanceֹ_for_user(self, amount: int, user_id: int):
        with self.connection.cursor() as cursor:
            cursor.execute(SELECT_USER_BY_ID, [user_id])
            balance = int(cursor.fetchone()["balance"])
            balance = balance + int(amount)
            cursor.execute(UPDATE_BALANCE_BY_ID, [balance, user_id])
            self.connection.commit()

    def get_all_categories(self):
        with self.connection.cursor() as cursor:
            cursor.execute(SELECT_ALL_CATEGORIES)
            result = cursor.fetchall()
            return result


CONNECTOR = None


def get_db_connector():
    global CONNECTOR
    if CONNECTOR is None:
        try:
            CONNECTOR = DalSQL()
        except Exception as e:
            print(e)
    return CONNECTOR
