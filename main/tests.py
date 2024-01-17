from django.test import TestCase
from django.urls import reverse
from rest_framework import status

from main.models import WeatherInfo, City
from main.services import get_weather, get_data_from_db


class ServicesTest(TestCase):

    def setUp(self):
        self.city = City.objects.create(name="Москва", latitude=55.75, longitude=37.62)
        self.weather = WeatherInfo.objects.create(
            city=self.city, temperature=25, atmospheric_pressure=741, wind_speed=4
        )

    def test_get_data_from_db(self):
        self.assertEqual(get_data_from_db("Москва"), self.weather)

    def test_get_weather(self):
        self.assertEqual(tuple(get_weather(56.85, 60.61).keys()),
                         ('temperature', 'atmospheric_pressure', 'wind_speed'))


class WeatherInfoAPIViewTest(TestCase):

    def setUp(self):
        self.city = City.objects.create(name="Екатеринбург", latitude=56.85, longitude=60.61)

    def test_get(self):
        response = self.client.get(
            reverse('weather:weather') + '?city=Екатеринбург'
        )

        resp_json = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(resp_json['city'], "Екатеринбург")
        self.assertEqual(tuple(resp_json.keys()), ('city', 'temperature', 'atmospheric_pressure', 'wind_speed'))
