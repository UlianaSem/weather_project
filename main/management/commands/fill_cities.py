from django.core.management import BaseCommand

from main.models import City


class Command(BaseCommand):

    CITIES = []

    def handle(self, *args, **options):
        with open('city_coordinates.txt', 'r', encoding='utf-8') as file:
            cities = file.readlines()

        for city in cities:
            city_name, coordinates = city.strip().split(' — ')
            latitude, longitude = coordinates.split(', ')

            self.CITIES.append(City(name=city_name, latitude=latitude, longitude=longitude))

        City.objects.bulk_create(self.CITIES)
