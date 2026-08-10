from .models import * 
from rest_framework import serializers

class CustomerSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    account_number = serializers.CharField(max_length=20)
    account_type = serializers.CharField(max_length=100)
    balance = serializers.DecimalField(max_digits=10, decimal_places=2)

