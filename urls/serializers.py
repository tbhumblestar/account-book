from rest_framework import serializers
from .models import Url


class UrlSerializer(serializers.ModelSerializer):
    expired_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Url
        fields = "__all__"
