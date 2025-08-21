import requests

API_KEY = "your_api_key_here"  # Replace with your OpenWeather API key
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    try:
        url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()

        if data.get("cod") != 200:
            print("City not found!")
            return

        print(f"Weather in {city}: {data['weather'][0]['description']}")
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Humidity: {data['main']['humidity']}%")
    except Exception as e:
        print(f"Error fetching weather: {e}")

if __name__ == "__main__":
    city = input("Enter city name: ")
    get_weather(city)
