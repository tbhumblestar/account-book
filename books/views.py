from django.db.models import Sum
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound, PermissionDenied, ParseError
from books.models import Expense
from books.serializers import ExpenseSerailizer
import datetime

# book/year/month
# GET
class Monthly(APIView):
    def get(self, request, year, month):
        book = request.user.book
        expense_list = (
            book.expenses.filter(
                date__year=year,
                date__month=month,
            )
            .values("date")
            .annotate(amount=Sum("amount"))
            .order_by("date")
        )

        expenses = dict()
        for per_date in list(expense_list):
            date, amount = per_date.values()
            expenses[str(date)] = amount

        return Response(
            expenses,
            status=status.HTTP_200_OK,
        )


# book/year/month/date
# GET POST
class Daily(APIView):
    def check_date(self, year, month, date):
        try:
            return datetime.date(year, month, date)
        except ValueError:
            raise ParseError("Invalid date")

    def get(self, request, year, month, date):
        date = self.check_date(year, month, date)
        book = request.user.book
        expense_objects = book.expenses.filter(
            date=date,
        )
        expense_list = ExpenseSerailizer(expense_objects, many=True)

        return Response(
            expense_list.data,
            status=status.HTTP_200_OK,
        )

    def post(self, request, year, month, date):
        date = self.check_date(year, month, date)
        serializer = ExpenseSerailizer(data=request.data)

        if serializer.is_valid():
            expense = serializer.save(
                date=date,
                book=request.user.book,
            )

            return Response(
                ExpenseSerailizer(expense).data,
                status=status.HTTP_201_CREATED,
            )

        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST,
            )


# book/expenses/pk
# GET PUT POST
class ExpenseDetail(APIView):
    def get_object(self, pk):
        try:
            return Expense.objects.get(pk=pk)
        except Expense.DoesNotExist:
            raise NotFound("Expense does not exist")

    def get(self, request, pk):
        expense = self.get_object(pk)
        return Response(
            ExpenseSerailizer(expense).data,
            status=status.HTTP_200_OK,
        )

    def patch(self, request, pk):
        expense = self.get_object(pk)

        if request.user != expense.book.user:
            raise PermissionDenied("Permission Denied")

        serializer = ExpenseSerailizer(
            instance=expense,
            data=request.data,
            partial=True,
        )

        if serializer.is_valid():
            expense = serializer.save()
            return Response(
                ExpenseSerailizer(expense).data,
                status=status.HTTP_200_OK,
            )

        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST,
            )

    def post(self, request, pk):
        expense = self.get_object(pk)

        if request.user != expense.book.user:
            raise PermissionDenied("Permission Denied")

        expense.pk = None
        expense._state.adding = True
        expense.save()

        return Response(
            ExpenseSerailizer(expense).data,
            status=status.HTTP_200_OK,
        )
