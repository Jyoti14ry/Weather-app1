import requests

API_KEY = "your_api_key_here"  # Replace with your OpenWeather API key
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    if not API_KEY or API_KEY == "your_api_key_here":
        print("Error: API key is missing or incorrect.")
        return
    
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"  # Change to "imperial" for Fahrenheit
    }
    
    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        data = response.json()
        
        if data.get("cod") != 200:
            print(f"Error: {data.get('message', 'City not found')}")
            return
        
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        condition = data["weather"][0]["description"]
        
        print(f"Weather in {city}:")
        print(f"Temperature: {temp}°C")
        print(f"Humidity: {humidity}%")
        print(f"Condition: {condition.capitalize()}")
    
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.ConnectionError:
        print("Error: Unable to connect to the weather service. Check your internet connection.")
    except requests.exceptions.Timeout:
        print("Error: The request timed out.")
    except requests.exceptions.RequestException as err:
        print(f"Error: Unable to fetch weather data. {err}")
    except KeyError:
        print("Error: Unexpected data format from API.")

if __name__ == "__main__":
    city_name = input("Enter city name: ")
    if city_name.strip():
        get_weather(city_name)
    else:
        print("Error: City name cannot be empty."
