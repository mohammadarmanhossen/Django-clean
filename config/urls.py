from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.customers.api.viewsets import CustomerViewSet

router = DefaultRouter()
router.register(r'customers', CustomerViewSet, basename='customer')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
