from django.urls import path

from main.apps import MainConfig
from main.views import WeatherInfoAPIView

app_name = MainConfig.name


urlpatterns = [
    path('weather', WeatherInfoAPIView.as_view(), name="weather"),
]
