#!/usr/bin/env python3
"""
Simple Weather App
A command-line weather application that fetches current weather data using OpenWeatherMap API.
"""

import os
import sys
import requests
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class WeatherApp:
    """Main Weather Application class"""

    BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

    def __init__(self):
        """Initialize the weather app with API key"""
        self.api_key = os.getenv('OPENWEATHER_API_KEY')
        if not self.api_key:
            print("Error: OPENWEATHER_API_KEY not found in environment variables.")
            print("Please create a .env file with your API key.")
            sys.exit(1)

    def get_weather(self, city):
        """
        Fetch weather data for a given city

        Args:
            city (str): Name of the city

        Returns:
            dict: Weather data or None if request fails
        """
        params = {
            'q': city,
            'appid': self.api_key,
            'units': 'metric'  # Use metric units (Celsius)
        }

        try:
            response = requests.get(self.BASE_URL, params=params, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as e:
            if response.status_code == 404:
                print(f"Error: City '{city}' not found.")
            else:
                print(f"HTTP Error: {e}")
            return None
        except requests.exceptions.RequestException as e:
            print(f"Error fetching weather data: {e}")
            return None

    def display_weather(self, weather_data):
        """
        Display formatted weather information

        Args:
            weather_data (dict): Weather data from API
        """
        if not weather_data:
            return

        city = weather_data['name']
        country = weather_data['sys']['country']
        temp = weather_data['main']['temp']
        feels_like = weather_data['main']['feels_like']
        humidity = weather_data['main']['humidity']
        pressure = weather_data['main']['pressure']
        description = weather_data['weather'][0]['description'].capitalize()
        wind_speed = weather_data['wind']['speed']

        # Convert timestamp to readable format
        timestamp = weather_data['dt']
        time = datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')

        print("\n" + "="*50)
        print(f"Weather in {city}, {country}")
        print("="*50)
        print(f"Time: {time}")
        print(f"Condition: {description}")
        print(f"Temperature: {temp}°C (Feels like {feels_like}°C)")
        print(f"Humidity: {humidity}%")
        print(f"Pressure: {pressure} hPa")
        print(f"Wind Speed: {wind_speed} m/s")
        print("="*50 + "\n")

    def run(self):
        """Main application loop"""
        print("Welcome to the Weather App!")
        print("Type 'quit' or 'exit' to close the app.\n")

        while True:
            city = input("Enter city name: ").strip()

            if city.lower() in ['quit', 'exit']:
                print("Thank you for using Weather App. Goodbye!")
                break

            if not city:
                print("Please enter a valid city name.")
                continue

            weather_data = self.get_weather(city)
            self.display_weather(weather_data)


def main():
    """Entry point of the application"""
    app = WeatherApp()
    app.run()


if __name__ == "__main__":
    main()
