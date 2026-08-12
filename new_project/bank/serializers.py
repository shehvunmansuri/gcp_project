import types
from distro import name
# from tomlkit import value
from .models import * 
from rest_framework import serializers

class CustomerSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    account_number = serializers.CharField(max_length=20)
    account_type = serializers.CharField(max_length=100)
    balance = serializers.DecimalField(max_digits=10, decimal_places=2)


class CustomerPostSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    account_number = serializers.CharField(max_length=20)
    account_type = serializers.CharField(max_length=100)
    balance = serializers.DecimalField(max_digits=15, decimal_places=2)

    def validate_name(self, value):
        if not value.isalpha():
            raise serializers.ValidationError("Name must contains only alphhabets")
        return value

    def validate_account_number(self,value):
        if not value.isalnum():
            raise serializers.ValidationError("account number must contain alphanumeric")
        return value

    def validate_account_type(self,value):
        types = ['savings', 'current', 'fixed_deposit']
        if value not in types:
            raise serializers.ValidationError(f"account must be one of the following {types}")
        return value

    def validate_balance(self,value):
        if value < 0:
            raise serializers.ValidationError("balance must be greater than 0")
        return value

    def create(self, validated_data):
        return Customer.objects.create(
            name=validated_data.get('name'),
            account_number=validated_data.get('account_number'),
            account_type=validated_data.get('account_type'),
            balance=validated_data.get('balance')
        )
    

