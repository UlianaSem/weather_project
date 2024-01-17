from datetime import timedelta

import requests
from django.shortcuts import get_object_or_404
from django.utils import timezone

from config import settings
from main.models import WeatherInfo, City


def get_data_from_db(city_name):
    """
    Получает данные о городе из БД и проверяет есть ли данные о погоде за последние 30 минут
    :param city_name: название города
    :return: объект WeatherInfo или словарь с сообщением об ошибке
    """
    city = get_object_or_404(City, name=city_name.title())
    now = timezone.now()

    weather_info = WeatherInfo.objects.filter(city=city).order_by('-created_at').first()

    if weather_info is None or now - weather_info.created_at > timedelta(minutes=30):
        weather = get_weather(city.latitude, city.longitude)

        if weather is None:
            return {"error": "Ошибка запроса погоды"}

        weather_info = WeatherInfo.objects.create(city=city, **weather)

    return weather_info


def get_weather(latitude, longitude):
    """
    Получает данные о погоде с API яндекса
    :param latitude: широта
    :param longitude: долгота
    :return: dict
    """
    url = 'https://api.weather.yandex.ru/v2/forecast'
    query = {
        "lat": latitude,
        "lon": longitude,
    }
    header = {
        "X-Yandex-API-Key": settings.YANDEX_KEY
    }

    response = requests.get(url, params=query, headers=header)

    if response.status_code == 200:
        weather = response.json().get('fact')

        return {'temperature': weather.get('temp'),
                'atmospheric_pressure': weather.get('pressure_mm'),
                'wind_speed': weather.get('wind_speed')}
