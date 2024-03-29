# Generated by Django 5.0.1 on 2024-01-13 08:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='название города')),
                ('latitude', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='широта')),
                ('longitude', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='долгота')),
            ],
            options={
                'verbose_name': 'город',
                'verbose_name_plural': 'города',
            },
        ),
        migrations.CreateModel(
            name='WeatherInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature', models.IntegerField(verbose_name='температура')),
                ('atmospheric_pressure', models.IntegerField(verbose_name='атмосферное давление')),
                ('wind_speed', models.IntegerField(verbose_name='скорость ветра')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='weather', to='main.city', verbose_name='')),
            ],
            options={
                'verbose_name': 'информация о погоде',
                'verbose_name_plural': 'информация о погоде',
            },
        ),
    ]
