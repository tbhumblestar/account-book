from rest_framework.test import APITestCase
from users.models import User
from books.models import Book, Expense
import datetime


class APITestCaseWithUser(APITestCase):
    def setUp(self):
        user = User.objects.create(email="test@test.com")
        user.set_password("1234")
        user.save()
        self.user = user
        self.client.force_authenticate(user=user)

        self.book = Book.objects.create(user=user)
        self.expense = Expense.objects.create(
            date=datetime.date(2023, 1, 1),
            amount=1000,
            memo="memo",
            book=self.book,
        )


class TestMonthly(APITestCaseWithUser):
    URL = "/book/2023/1"

    def test_get(self):
        response = self.client.get(self.URL)

        data = response.json()

        self.assertEqual(
            response.status_code,
            200,
        )
        self.assertIsInstance(
            data,
            dict,
        )
        self.assertEqual(
            data["2023-01-01"],
            1000,
        )


class TestDaily(APITestCaseWithUser):
    URL = "/book/2023/1/1"

    def test_get(self):
        response = self.client.get(self.URL)
        data = response.json()
        element = data[0]

        self.assertIsInstance(
            data,
            list,
        )
        self.assertEqual(
            response.status_code,
            200,
        )
        self.assertIn(
            "pk",
            element,
        )
        self.assertIn(
            "date",
            element,
        )
        self.assertIn(
            "amount",
            element,
        )

    def test_post(self):
        response = self.client.post(self.URL, {"amount": 2000, "memo": "new expense"})
        data = response.json()

        self.assertEqual(
            response.status_code,
            201,
        )
        self.assertEqual(
            len(Expense.objects.filter(book=self.book)),
            2,
        )
        self.assertIn(
            "pk",
            data,
        )
        self.assertIn(
            "date",
            data,
        )
        self.assertIn(
            "amount",
            data,
        )


class TestExpenseDetail(APITestCaseWithUser):
    BASE_URL = "/book/expenses/"

    def test_get(self):
        response = self.client.get(self.BASE_URL + str(self.expense.pk))
        data = response.json()

        self.assertEqual(
            response.status_code,
            200,
        )
        self.assertIn(
            "pk",
            data,
        )
        self.assertIn(
            "date",
            data,
        )
        self.assertIn(
            "amount",
            data,
        )

    def test_patch(self):
        response = self.client.patch(
            self.BASE_URL + str(self.expense.pk),
            {
                "memo": self.expense.memo + "new",
                "amount": self.expense.amount + 1000,
            },
        )
        data = response.json()

        self.assertEqual(
            response.status_code,
            200,
        )
        self.assertIn(
            "pk",
            data,
        )
        self.assertIn(
            "date",
            data,
        )
        self.assertIn(
            "amount",
            data,
        )
        self.assertIn(
            "memo",
            data,
        )
        self.assertNotEqual(
            data.get("memo"),
            self.expense.memo,
        )
        self.assertNotEqual(
            data.get("amount"),
            self.expense.amount,
        )

    def test_post(self):
        response = self.client.post(self.BASE_URL + str(self.expense.pk))
        data = response.json()

        self.assertEqual(
            response.status_code,
            200,
        )
        self.assertIn(
            "pk",
            data,
        )
        self.assertIn(
            "date",
            data,
        )
        self.assertIn(
            "amount",
            data,
        )
        self.assertNotEqual(
            self.expense.pk,
            data.get("pk"),
        )
