from rest_framework import serializers
from .models import Expense
from django.contrib.auth.models import User

class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = ['id', 'title', 'amount', 'category', 'date']

class RegisterSerializer(serializers.ModelSerializer):
    # write_only=True means password will never be returned in any response
    password = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = User
        fields = ['username', 'password']

    def create(self, validated_data):
        # create_user() hashes the password properly — never use User.objects.create() for this
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user