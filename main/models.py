from django.db.models import Model, CharField, DecimalField, ForeignKey, CASCADE, IntegerField, DateTimeField


class City(Model):
    name = CharField(max_length=255, verbose_name='название города')
    latitude = DecimalField(max_digits=6, decimal_places=2, verbose_name='широта')
    longitude = DecimalField(max_digits=6, decimal_places=2, verbose_name='долгота')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'город'
        verbose_name_plural = 'города'


class WeatherInfo(Model):
    city = ForeignKey(City, on_delete=CASCADE, verbose_name='', related_name='weather')
    temperature = IntegerField(verbose_name='температура')
    atmospheric_pressure = IntegerField(verbose_name='атмосферное давление')
    wind_speed = IntegerField(verbose_name='скорость ветра')
    created_at = DateTimeField(verbose_name="Время создания", auto_now_add=True)

    def __str__(self):
        return f'{self.city.name} {self.temperature}С'

    class Meta:
        verbose_name = 'информация о погоде'
        verbose_name_plural = 'информация о погоде'
