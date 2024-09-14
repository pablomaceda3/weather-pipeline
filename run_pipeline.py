from api_key import api_key
from weather_pipeline import WeatherDataPipeline

def main():
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