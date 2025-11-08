
from abc import ABC, abstractmethod
from apps.customers.domain.entities import Customer

class CustomerRepository(ABC):
    @abstractmethod
    def get_all(self): pass

    @abstractmethod
    def get_by_id(self, id: int) -> Customer: pass

    @abstractmethod
    def create(self, customer: Customer) -> Customer: pass

    @abstractmethod
    def update(self, customer: Customer) -> Customer: pass

    @abstractmethod
    def delete(self, id: int): pass
