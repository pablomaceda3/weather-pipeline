import requests
from datetime import datetime


class WeatherDataCollector:
    def __init__(self, city_name: str, api_key: str):
        self.city_name = city_name
        self.api_key = api_key

    def create_url(self):
        return f"https://api.openweathermap.org/data/2.5/weather?q={self.city_name}&appid={self.api_key}"

    def fetch_weather_data(self):
        try:
            url = self.create_url()
            response = requests.get(url)

            response.raise_for_status()

            data = response.json()
            print(f"Data fetched at {datetime.now()}")
            return data
        except requests.exceptions.RequestException as e:
            print(f"Error fetching weather data: {e}")
            return None