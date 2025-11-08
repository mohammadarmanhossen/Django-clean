# apps/customers/api/viewsets.py
from rest_framework import viewsets
from rest_framework.response import Response
from apps.customers.adapters.repository.customer_repo import DjangoCustomerRepository
from apps.customers.usecases.customer_usecases import CustomerUseCases
from .serializers import CustomerSerializer

class CustomerViewSet(viewsets.ViewSet):
    repo = DjangoCustomerRepository()
    usecases = CustomerUseCases(repo)

    def list(self, request):
        customers = self.usecases.list_customers()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        customer = self.usecases.get_customer(int(pk))
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)

    def create(self, request):
        customer = self.usecases.create_customer(request.data["name"], request.data["email"])
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)

    def update(self, request, pk=None):
        customer = self.usecases.update_customer(int(pk), request.data["name"], request.data["email"])
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        self.usecases.delete_customer(int(pk))
        return Response({"message": "Deleted successfully"})
