
from apps.customers.adapters.orm.models import CustomerModel
from apps.customers.domain.entities import Customer
from apps.customers.ports.customer_repository import CustomerRepository

class DjangoCustomerRepository(CustomerRepository):
    def get_all(self):
        return [Customer(c.id, c.name, c.email) for c in CustomerModel.objects.all()]

    def get_by_id(self, id):
        c = CustomerModel.objects.get(id=id)
        return Customer(c.id, c.name, c.email)

    def create(self, customer):
        c = CustomerModel.objects.create(name=customer.name, email=customer.email)
        return Customer(c.id, c.name, c.email)

    def update(self, customer):
        c = CustomerModel.objects.get(id=customer.id)
        c.name = customer.name
        c.email = customer.email
        c.save()
        return Customer(c.id, c.name, c.email)

    def delete(self, id):
        CustomerModel.objects.filter(id=id).delete()
