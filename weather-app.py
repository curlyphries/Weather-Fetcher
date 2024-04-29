import requests
import os
import json

def get_coordinates(api_key, city, state):
    """Fetch coordinates from OpenWeather Geocoding API for a given city and state name."""
    geocode_url = "http://api.openweathermap.org/geo/1.0/direct"
    query = f"{city},{state},US"  # Assuming the search is within the United States
    params = {
        'q': query,
        'limit': 1,
        'appid': api_key
    }
    response = requests.get(geocode_url, params=params)
    response.raise_for_status()  # This will raise an exception if the request fails
    data = response.json()
    if not data:
        print("City not found. Please check the city and state name.")
        return None
    return data[0]['lat'], data[0]['lon']

def get_weather_data(api_key, lat, lon, units='imperial'):
    """Fetch current weather data from OpenWeather API."""
    base_url = "https://api.openweathermap.org/data/3.0/onecall"
    params = {
        'lat': lat,
        'lon': lon,
        'appid': api_key,
        'exclude': 'minutely,hourly,daily,alerts',
        'units': units
    }
    response = requests.get(base_url, params=params)
    response.raise_for_status()  # This will raise an exception if the request fails
    return response.json()

def print_current_weather(weather_data):
    """Prints the current weather information in a friendly format."""
    current = weather_data['current']
    print(f"\nCurrent Weather for Now:")
    print(f"Temperature: {current['temp']}°F, feels like {current['feels_like']}°F")
    print(f"Condition: {current['weather'][0]['description'].capitalize()}")
    print(f"Humidity: {current['humidity']}%")
    print(f"Wind Speed: {current['wind_speed']} mph")
    print(f"Visibility: {current['visibility'] / 1609:.2f} miles")  # Convert meters to miles

def main():
    api_key = os.getenv('WEATHER_API_KEY')
    if not api_key:
        raise ValueError("WEATHER_API_KEY environment variable not set.")

    city = input("Enter the city name: ")
    state = input("Enter the state code (e.g., NY for New York): ")
    coordinates = get_coordinates(api_key, city, state)
    if coordinates:
        lat, lon = coordinates
        weather_data = get_weather_data(api_key, lat, lon)
        if weather_data:
            print_current_weather(weather_data)
        else:
            print("Failed to retrieve weather data.")
    else:
        print("Failed to retrieve coordinates.")

if __name__ == "__main__":
    main()
