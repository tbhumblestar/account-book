from django.urls import path
from .views import Users, Login, Logout


urlpatterns = [
    path("", Users.as_view()),
    path("login", Login.as_view()),
    path("logout", Logout.as_view()),
]
