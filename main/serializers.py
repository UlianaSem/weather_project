from rest_framework.serializers import ModelSerializer, SerializerMethodField

from main.models import WeatherInfo, City


class WeatherInfoSerializer(ModelSerializer):
    city = SerializerMethodField()

    class Meta:
        model = WeatherInfo
        fields = ['city', 'temperature', 'atmospheric_pressure', 'wind_speed', ]

    def get_city(self, instance):
        return City.objects.get(id=instance.city.id).name
