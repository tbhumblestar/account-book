from django.urls import path
from .views import Urls

urlpatterns = [
    path("", Urls.as_view()),
]
