from abc import ABC, abstractmethod


class DAL(ABC):
    @abstractmethod
    def get_all_transactions():
        pass

    @abstractmethod
    def remove_transaction_by_id(id):
        pass

    def add_transaction(i):
        pass
