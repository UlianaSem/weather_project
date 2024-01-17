from django.core.management import BaseCommand
from telebot import TeleBot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import settings
from main.models import WeatherInfo
from main.services import get_data_from_db

bot = TeleBot(settings.TG_BOT, threaded=False)


class Command(BaseCommand):

    def handle(self, *args, **options):

        @bot.callback_query_handler(func=lambda callback: True)
        def check_callback_data(callback):
            message = bot.send_message(callback.message.chat.id, "Введите название города")
            bot.register_next_step_handler(message, get_weather_)

        @bot.message_handler(commands=['start'])
        def start(message):
            markup = InlineKeyboardMarkup()
            button = InlineKeyboardButton(text="Узнать погоду", callback_data="callback")

            markup.add(button)

            bot.send_message(message.chat.id, "Нажмите кнопку, чтобы узнать погоду", reply_markup=markup)

        def get_weather_(message):
            city_name = message.text

            weather_info = get_data_from_db(city_name)

            if not isinstance(weather_info, WeatherInfo):
                bot.send_message(message.chat.id, weather_info.get('error'))

            bot.send_message(message.chat.id, f'В г. {weather_info.city} температура воздуха '
                                              f'{weather_info.temperature} °C, '
                                              f'скорость ветра {weather_info.wind_speed} м/с, атм. давление '
                                              f'{weather_info.atmospheric_pressure} мм рт. ст.')

        bot.enable_save_next_step_handlers(delay=2)
        bot.load_next_step_handlers()
        bot.infinity_polling()
