from rest_framework import serializers
from .models import Expense


class ExpenseSerailizer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = (
            "pk",
            "date",
            "amount",
            "memo",
        )
