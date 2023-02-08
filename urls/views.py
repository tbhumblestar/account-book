from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound
from urls.models import Url
from urls.serializers import UrlSerializer
from config.var import var
from urls.utils import encode, decode

base_url_for_shorten = var["cors"]["domain"] + "/short/"


# urls?encoded={encoded}
# GET POST
class Urls(APIView):
    def get_object(self, pk):
        try:
            return Url.objects.get(pk=pk)
        except Url.DoesNotExist:
            raise NotFound("Url not found")

    def get(self, request):
        encoded = request.query_params.get("encoded")
        decoded_pk = decode(encoded)
        url = self.get_object(pk=decoded_pk)

        if url.expired_at > timezone.now():
            return Response(
                UrlSerializer(url).data,
                status=status.HTTP_200_OK,
            )

        else:
            url.delete()
            raise NotFound("Url is expired")

    def post(self, request):
        serializer = UrlSerializer(data=request.data)

        if serializer.is_valid():
            url = serializer.save(
                expired_at=timezone.now() + timezone.timedelta(days=3)
            )
            shorten_url = base_url_for_shorten + encode(url.pk)
            return Response(
                {"url": shorten_url},
                status=status.HTTP_201_CREATED,
            )

        else:
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
            )
