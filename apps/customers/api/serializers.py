# apps/customers/api/serializers.py
from rest_framework import serializers

class CustomerSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255)
    email = serializers.EmailField()
