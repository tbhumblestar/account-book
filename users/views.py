from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from books.models import Book
from users.serializers import *


class UserCommon(APIView):
    def get_response_with_token(self, user):
        token = TokenObtainPairSerializer().get_token(user)
        refresh_token = str(token)
        access_token = str(token.access_token)

        response = Response(
            {
                "access": access_token,
                "refresh": refresh_token,
            },
            status=status.HTTP_200_OK,
        )
        response.set_cookie(
            "access",
            access_token,
        )
        response.set_cookie(
            "refresh",
            refresh_token,
        )

        return response


# users/
# POST
class Users(UserCommon):

    permission_classes = [AllowAny]
    serializer_class = SignupSerializer

    def post(self, request):
        serializer = SignupSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            Book.objects.create(user=user)
            response = self.get_response_with_token(user)
            return response
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST,
            )


# users/login
# POST
class Login(UserCommon):

    permission_classes = [AllowAny]
    serializer_class = LoginSerializer

    def get_object(self, email):
        try:
            return User.objects.get(email=email)
        except User.DoesNotExist:
            raise AuthenticationFailed("Email does not exist")

    def post(self, request):
        serializers = LoginSerializer(data=request.data)

        if serializers.is_valid():
            self.get_object(request.data.get("email"))

            user = authenticate(
                request,
                email=request.data.get("email"),
                password=request.data.get("password"),
            )

            if not user:
                raise AuthenticationFailed("Password wrong")

            response = self.get_response_with_token(user)
            return response

        else:
            return Response(
                serializers.errors,
                status=status.HTTP_400_BAD_REQUEST,
            )


# users/logout
# POST
class Logout(APIView):
    def post(self, request):
        response = Response(status=status.HTTP_202_ACCEPTED)
        response.delete_cookie("access")
        response.delete_cookie("refresh")
        return response
