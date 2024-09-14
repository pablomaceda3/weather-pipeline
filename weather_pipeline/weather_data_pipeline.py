import time

from weather_data_collector import WeatherDataCollector
from weather_data_transformer import WeatherDataTransformer


class WeatherDataPipeline:
    def __init__(self, api_key, city_name, interval=60):
        self.collector = WeatherDataCollector(city_name=city_name, api_key=api_key)
        self.interval = interval

    def run(self):
        while True:
            # Fetch raw weather data
            raw_data = self.collector.fetch_weather_data()
            
            # Transform the raw data into a usable format
            transformed_data = WeatherDataTransformer.transform(raw_data)
            
            composite_data = WeatherDataTransformer.compose(transformed_data)
            
            # You could send this data to a Kafka stream, save to a database, etc.
            # For now, it's just printed to the console

            # Wait for the next poll
            time.sleep(self.interval)