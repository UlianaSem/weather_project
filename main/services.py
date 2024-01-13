import requests

from config import settings


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
