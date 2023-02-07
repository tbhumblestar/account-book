from django.db import models


class Book(models.Model):
    user = models.OneToOneField(
        "users.User",
        on_delete=models.CASCADE,
    )


class Expense(models.Model):
    date = models.DateField()
    amount = models.PositiveIntegerField()
    memo = models.TextField(
        max_length=300,
        blank=True,
        null=True,
    )
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name="expenses",
    )
