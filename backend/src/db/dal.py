from abc import ABC, abstractmethod
from src.models.transaction_data_class import Transactions


class DAL(ABC):
    @abstractmethod
    def get_all_transactions_by_user(self, user_id: int = 1):
        pass

    @abstractmethod
    def remove_transaction_by_id(self, transaction_id: int):
        pass

    @abstractmethod
    def add_transaction(self, new_transaction: Transactions, user_id: int = 1) -> int:
        pass
