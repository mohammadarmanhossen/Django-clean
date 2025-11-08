
from apps.customers.domain.entities import Customer

class CustomerUseCases:
    def __init__(self, repo):
        self.repo = repo

    def list_customers(self):
        return self.repo.get_all()

    def get_customer(self, id):
        return self.repo.get_by_id(id)

    def create_customer(self, name, email):
        return self.repo.create(Customer(None, name, email))

    def update_customer(self, id, name, email):
        return self.repo.update(Customer(id, name, email))

    def delete_customer(self, id):
        self.repo.delete(id)
