from loader import bot
from api.api_weather import api_weather
from database.db import log_history
import json


@bot.message_handler(commands=['weather'])
def weather(message):
    log_history(message.from_user.id, message.from_user.full_name, 'weather')
    image_path = 'img/img_w.jpg'
    with open(image_path, 'rb') as file:
        bot.send_photo(message.chat.id, file)
        bot.send_message(message.chat.id, '<b>Введите город</b>', parse_mode='html')
        log_history(message.from_user.id, 'Bot', 'Введите город')
        bot.register_next_step_handler(message, get_weather)


def get_weather(message):
    city = message.text.strip().capitalize()
    log_history(message.from_user.id, message.from_user.full_name, city)
    res = api_weather(city)
    if res.status_code == 200:
        data = json.loads(res.text)
        temp = data["main"]["temp"]
        temp = round(temp, 0)
        if temp >= 25:
            bot.reply_to(message, f'Текущая температура воздуха\nв г. {city}: {temp}°C 🥵')
            log_history(message.from_user.id, 'Bot', f'Текущая температура воздуха\nв г. {city}: {temp}°C 🥵')
        elif temp < 0:
            bot.reply_to(message, f'Текущая температура воздуха\nв г. {city}: {temp}°C 🥶')
            log_history(message.from_user.id, 'Bot', f'Текущая температура воздуха\nв г. {city}: {temp}°C 🥶')
        else:
            bot.reply_to(message, f'Текущая температура воздуха\nв г. {city}: {temp}°C 🌡')
            log_history(message.from_user.id, 'Bot', f'Текущая температура воздуха\nв г. {city}: {temp}°C 🌡')
    else:
        bot.reply_to(message, '<b>Введен несуществующий город!\nПовторите ввод!</b>', parse_mode='html')
        log_history(message.from_user.id, 'Bot', 'Введен несуществующий город! Повторите ввод!')
        bot.register_next_step_handler(message, get_weather)




