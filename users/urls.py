from django.urls import path
from .views import Users, Login, Logout
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path("", Users.as_view()),
    path("login", Login.as_view()),
    path("logout", Logout.as_view()),
    path("token/refresh/", TokenRefreshView.as_view()),
]
