from rest_framework.test import APITestCase
from books.models import Book
from users.models import User


class TestUsers(APITestCase):
    URL = "/users/"
    EMAIL = "test@test.com"
    PASSWORD = "1234"

    def test_post(self):
        response = self.client.post(
            self.URL,
            {
                "email ": self.EMAIL,
                "password": self.PASSWORD,
            },
        )
        data = response.json()

        self.assertEqual(
            response.status_code,
            201,
        )
        self.assertIn(
            "email",
            data,
        )
        self.assertEqual(
            len(Book.objects.all()),
            1,
        )


class TestLogin(APITestCase):
    URL = "/users/login"
    EMAIL = "test@test.com"
    PASSWORD = "1234"

    def setUp(self):
        user = User.objects.create(email=self.EMAIL)
        user.set_password(self.PASSWORD)
        user.save()
        self.user = user

    def test_post(self):
        response = self.client.post(
            self.URL,
            {"email": self.EMAIL, "password": self.PASSWORD},
        )
        data = response.json()

        self.assertEqual(
            response.status_code,
            200,
        )
        self.assertIn(
            "token",
            data,
        )


class TestLogout(APITestCase):
    URL = "/users/logout"
    EMAIL = "test@test.com"
    PASSWORD = "1234"

    def setUp(self):
        user = User.objects.create(email=self.EMAIL)
        user.set_password(self.PASSWORD)
        user.save()
        self.user = user

    def test_post(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.post(self.URL)

        self.assertEqual(
            response.status_code,
            200,
        )
