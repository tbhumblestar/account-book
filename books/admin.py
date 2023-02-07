from django.contrib import admin
from .models import Book, Expense


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "user",
    )


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "book",
        "date",
        "amount",
        "memo",
    )
