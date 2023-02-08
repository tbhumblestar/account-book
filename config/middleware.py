import jwt
from django.utils import timezone
from django.utils.dateparse import parse_datetime
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from users.models import User
from config.var import var


class JWTAuthentication(BaseAuthentication):
    def authenticate(self, request):
        token = request.headers.get("Authorization")
        if not token:
            return None
        token = token.split(" ")[1]

        try:
            decoded = jwt.decode(
                token,
                var["jwt"]["secret"],
                algorithms="HS256",
            )
        except:
            raise AuthenticationFailed("invalid token")

        pk = decoded.get("pk")
        expired_at = decoded.get("expired_at")

        if not pk or not expired_at:
            raise AuthenticationFailed("invalid token")

        if parse_datetime(expired_at) < timezone.now():
            raise AuthenticationFailed("invalid token")

        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise AuthenticationFailed("User not found")

        return (user, None)
