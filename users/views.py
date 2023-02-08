from django.contrib.auth.hashers import check_password
from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import AllowAny
import jwt
from books.models import Book
from users.serializers import *
from config.var import var


# users/
# POST
class Users(APIView):

    permission_classes = [AllowAny]
    serializer_class = SignupSerializer

    def post(self, request):
        serializer = SignupSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            Book.objects.create(user=user)
            return Response(
                UserSerializer(user).data,
                status=status.HTTP_201_CREATED,
            )
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST,
            )


# users/login
# POST
class Login(APIView):

    permission_classes = [AllowAny]
    serializer_class = LoginSerializer

    def get_object(self, email):
        try:
            return User.objects.get(email=email)
        except User.DoesNotExist:
            raise AuthenticationFailed("Email does not exist")

    def post(self, request):
        serializer = LoginSerializer(data=request.data)

        if serializer.is_valid():
            user = self.get_object(serializer.data.get("email"))
            password_check = check_password(
                serializer.data.get("password"), user.password
            )
            if not password_check:
                raise AuthenticationFailed("Password wrong")

            expired_at = str(
                timezone.now() + timezone.timedelta(days=var["jwt"]["expired_days"])
            )
            encoded = jwt.encode(
                {
                    "pk": user.pk,
                    "expired_at": expired_at,
                },
                var["jwt"]["secret"],
                algorithm="HS256",
            )

            return Response(
                {"token": encoded},
                status=status.HTTP_200_OK,
            )

        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST,
            )


# users/logout
# POST
class Logout(APIView):
    def post(self, request):
        return Response(
            status=status.HTTP_200_OK,
        )
