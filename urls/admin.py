from django.contrib import admin
from .models import Url


@admin.register(Url)
class UrlAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "url",
        "expired_at",
    )
