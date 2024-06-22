# weather_forecast_app.py
import requests

API_KEY = 'your_api_key'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather?'

def get_weather(city):
    request_url = f"{BASE_URL}q={city}&appid={API_KEY}"
    response = requests.get(request_url)
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        wind = data['wind']
        weather = data['weather'][0]
        return {
            "temperature": main['temp'],
            "pressure": main['pressure'],
            "humidity": main['humidity'],
            "wind_speed": wind['speed'],
            "description": weather['description']
        }
    else:
        return None

def display_weather(weather_data, city):
    if weather_data:
        print(f"Weather in {city}:")
        print(f"Temperature: {weather_data['temperature']}K")
        print(f"Pressure: {weather_data['pressure']}hPa")
        print(f"Humidity: {weather_data['humidity']}%")
        print(f"Wind Speed: {weather_data['wind_speed']}m/s")
        print(f"Description: {weather_data['description']}")
    else:
        print(f"Failed to get weather for {city}")

if __name__ == "__main__":
    city = input("Enter city name: ")
    weather_data = get_weather(city)
    display_weather(weather_data, city)
