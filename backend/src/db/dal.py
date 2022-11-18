from abc import ABC, abstractmethod
from typing import List
from src.models.transaction_data_class import Transactions
from src.models.user_data_class import User


class DAL(ABC):
    @abstractmethod
    def get_user_by_id(self, user_id: int) -> User:
        pass

    @abstractmethod
    def get_all_transactions_by_user(self, user_id: int) -> List[Transactions]:
        pass

    @abstractmethod
    def get_transaction_by_id(self, transaction_id: int) -> Transactions:
        pass

    @ abstractmethod
    def remove_transaction_by_id(self, transaction_id: int):
        pass

    @ abstractmethod
    def add_transaction(self, new_transaction: Transactions, user_id: int = 1) -> int:
        pass

    @ abstractmethod
    def change_balanceֹ_for_user(self, amount: int, user_id: int):
        pass

    @ abstractmethod
    def get_all_categories(self):
        pass

    @ abstractmethod
    def get_breakdown(self):
        pass
