from rest_framework.test import APITestCase
from urls.models import Url
from django.utils import timezone
from urls.utils import decode, encode
from users.models import User


class TestUrls(APITestCase):
    BASE_URL = "/urls/"
    TEST_URL = "http://127.0.0.1:8000/book/expense/1"

    def setUp(self):
        user = User.objects.create(email="test@test.com")
        user.set_password("1234")
        user.save()
        self.client.force_authenticate(user=user)

        self.url = Url.objects.create(
            url=self.TEST_URL,
            expired_at=timezone.now() + timezone.timedelta(days=3),
        )

    def test_get(self):
        response = self.client.get(self.BASE_URL + f"?encoded={encode(self.url.pk)}")
        data = response.json()

        self.assertEqual(
            response.status_code,
            200,
        )
        self.assertIn(
            "id",
            data,
        )
        self.assertIn(
            "expired_at",
            data,
        )
        self.assertIn(
            "url",
            data,
        )

    def test_post(self):
        response = self.client.post(self.BASE_URL, {"url": self.TEST_URL})
        data = response.json()

        self.assertEqual(
            response.status_code,
            201,
        )
        self.assertEqual(
            len(Url.objects.all()),
            2,
        )
        self.assertIn(
            "url",
            data,
        )
