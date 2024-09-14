import os

from weather_pipeline.weather_data_pipeline import WeatherDataPipeline

def main():
    api_key = os.getenv("WEATHER_API_KEY")
    print("Starting Weather Pipeline for Austin, TX...")
    city_name = "Austin"
    interval = 60
    pipeline = WeatherDataPipeline(
        api_key=api_key, 
        city_name=city_name, 
        interval=interval
        )
    pipeline.run()


if __name__ == "__main__":
    main()