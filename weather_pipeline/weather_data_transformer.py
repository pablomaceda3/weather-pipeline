from datetime import datetime


class WeatherDataTransformer:
    @staticmethod
    def kelvin_to_celsius(kelvin):
        return kelvin - 273.15

    @staticmethod
    def kelvin_to_fahrenheit(kelvin):
        return kelvin * 9/5 - 459.67

    @staticmethod
    def mps_to_kmh(mps):
        return mps * 3.6

    @staticmethod
    def transform(raw_data):
        if not raw_data:
            return None
        
        temp_kelvin = raw_data['main']['temp']
        humidity = raw_data['main']['humidity']
        wind_speed_mps = raw_data['wind']['speed']
        
        # Convert units and prepare transformed data
        transformed_data = {
            'temperature_celsius': WeatherDataTransformer.kelvin_to_celsius(temp_kelvin),
            'temperature_fahrenheit': WeatherDataTransformer.kelvin_to_fahrenheit(temp_kelvin),
            'humidity': humidity,
            'wind_speed_kmh': WeatherDataTransformer.mps_to_kmh(wind_speed_mps),
            'weather_condition': raw_data['weather'][0]['description'],
            'timestamp': datetime.now().isoformat()
        }
        
        print(f"Transformed Data at {transformed_data['timestamp']}:")
        print(transformed_data)
        print("-" * 40)
        
        return transformed_data

    @staticmethod
    def calculate_heat_index(temp_celsius, humidity):
        if temp_celsius >= 26:  # Only for high temps
            return -8.784 + 1.611 * temp_celsius + 2.338 * humidity - 0.146 * temp_celsius * humidity
        return temp_celsius

    @staticmethod
    def calculate_wind_chill(temp_celsius, wind_speed_kmh):
        if temp_celsius <= 10 and wind_speed_kmh >= 4.8:
            return 13.12 + 0.6215 * temp_celsius - 11.37 * wind_speed_kmh ** 0.16 + 0.3965 * temp_celsius * wind_speed_kmh ** 0.16
        return temp_celsius

    @staticmethod
    def compose(transformed_data):
        if not transformed_data:
            return None
        
        composed_data = {
            'heat_index': WeatherDataTransformer.calculate_heat_index(transformed_data['temperature_celsius'], transformed_data['humidity']),
            'wind_chill': WeatherDataTransformer.calculate_wind_chill(transformed_data['temperature_celsius'], transformed_data['wind_speed_kmh']),
        }

        print(f"Composed Data at {datetime.now().isoformat()}:")
        print(composed_data)
        print("-" * 40)
        return composed_data