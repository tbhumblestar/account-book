from rest_framework import serializers
from .models import Expense


class ExpenseSerailizer(serializers.ModelSerializer):
    date = serializers.DateField(read_only=True)

    class Meta:
        model = Expense
        fields = (
            "pk",
            "date",
            "amount",
            "memo",
        )
