import requests
from urllib.parse import quote
from config_data.config import WEATHER_API_KEY


def api_weather(city):
    api_key = WEATHER_API_KEY
    city_encoded = quote(city)  # Кодируем город для URL
    base_url = f'https://api.openweathermap.org/data/2.5/weather?q={city_encoded}&appid={api_key}&units=metric'

    print(f"[DEBUG] Запрос: {base_url}")
    response = requests.get(base_url)
    print(f"[DEBUG] Ответ: {response.status_code}, {response.text}")

    return response