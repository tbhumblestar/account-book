from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("users/", include("users.urls")),
    path("book/", include("books.urls")),
    path("urls/", include("urls.urls")),
]
