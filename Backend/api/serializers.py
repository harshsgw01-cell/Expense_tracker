from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Expense


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password']
        )
        return user


class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        # ← Explicitly list fields so 'user' is never required in the request body
        fields = ['id', 'amount', 'description', 'category', 'date']
        read_only_fields = ['id']