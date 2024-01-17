from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from main.models import WeatherInfo
from main.serializers import WeatherInfoSerializer
from main.services import get_data_from_db


class WeatherInfoAPIView(APIView):

    def get(self, request, format=None):
        city_name = self.request.query_params.get('city')

        weather_info = get_data_from_db(city_name)

        if not isinstance(weather_info, WeatherInfo):
            return Response(status=status.HTTP_404_NOT_FOUND, data=weather_info)

        return Response(status=status.HTTP_200_OK, data=WeatherInfoSerializer(weather_info).data)
