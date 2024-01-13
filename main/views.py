from datetime import timedelta

from django.utils import timezone
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from main.models import WeatherInfo, City
from main.serializers import WeatherInfoSerializer
from main.services import get_weather


class WeatherInfoAPIView(APIView):

    def get(self, request, format=None):
        city_name = self.request.query_params.get('city')
        city = get_object_or_404(City, name=city_name.title())
        now = timezone.now()

        weather_info = WeatherInfo.objects.filter(city=city).order_by('-created_at').first()

        if weather_info is None or now - weather_info.created_at > timedelta(minutes=30):
            weather = get_weather(city.latitude, city.longitude)

            if weather is None:
                return Response(status=status.HTTP_404_NOT_FOUND, data={"error": "Ошибка запроса погоды"})

            weather_info = WeatherInfo.objects.create(city=city, **weather)

        return Response(status=status.HTTP_200_OK, data=WeatherInfoSerializer(weather_info).data)
