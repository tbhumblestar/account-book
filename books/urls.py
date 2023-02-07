from django.contrib import admin
from django.urls import path, include
from books.views import Daily, ExpenseDetail, Monthly

urlpatterns = [
    path("<int:year>/<int:month>", Monthly.as_view()),
    path("<int:year>/<int:month>/<int:date>", Daily.as_view()),
    path("expenses/<int:pk>", ExpenseDetail.as_view()),
]
