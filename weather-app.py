import requests
import os
import json

def get_coordinates(api_key, city, state):
    """
    Fetch coordinates from OpenWeather Geocoding API for a given city and state name.

    Parameters:
        api_key (str): OpenWeather API key.
        city (str): Name of the city.
        state (str): State code (e.g., 'NY' for New York).

    Returns:
        tuple: (latitude, longitude) if city is found, else None.
    """
    # Define the Geocoding API endpoint
    geocode_url = "http://api.openweathermap.org/geo/1.0/direct"
    # Format the query with city and state
    query = f"{city},{state},US"  # Assuming the search is within the United States
    # Parameters for the API request
    params = {
        'q': query,
        'limit': 1,
        'appid': api_key
    }
    # Make the API request
    response = requests.get(geocode_url, params=params)
    response.raise_for_status()  # Raise an exception if the request fails
    # Parse the response JSON
    data = response.json()
    # Check if the city is found
    if not data:
        print("City not found. Please check the city and state name.")
        return None
    # Return the latitude and longitude
    return data[0]['lat'], data[0]['lon']

def get_weather_data(api_key, lat, lon, units='imperial'):
    """
    Fetch current weather data from OpenWeather API.

    Parameters:
        api_key (str): OpenWeather API key.
        lat (float): Latitude.
        lon (float): Longitude.
        units (str): Units of measurement. Default is 'imperial'.

    Returns:
        dict: Weather data.
    """
    # Define the One Call API endpoint
    base_url = "https://api.openweathermap.org/data/3.0/onecall"
    # Parameters for the API request
    params = {
        'lat': lat,
        'lon': lon,
        'appid': api_key,
        'exclude': 'minutely,hourly,daily,alerts',
        'units': units
    }
    # Make the API request
    response = requests.get(base_url, params=params)
    response.raise_for_status()  # Raise an exception if the request fails
    # Return the weather data
    return response.json()

def print_current_weather(weather_data):
    """
    Prints the current weather information in a friendly format.

    Parameters:
        weather_data (dict): The weather data returned by the get_weather_data function.
    """
    # Extract current weather data
    current = weather_data['current']
    # Print the weather information
    print(f"\nCurrent Weather for Now:")
    print(f"Temperature: {current['temp']}°F, feels like {current['feels_like']}°F")
    print(f"Condition: {current['weather'][0]['description'].capitalize()}")
    print(f"Humidity: {current['humidity']}%")
    print(f"Wind Speed: {current['wind_speed']} mph")
    print(f"Visibility: {current['visibility'] / 1609:.2f} miles")  # Convert meters to miles

def main():
    """
    Main function to fetch and display weather information for a specified city and state.

    - Retrieves the API key from environment variables.
    - Prompts user for city and state input.
    - Fetches coordinates and weather data.
    - Prints the current weather information.
    """
    # Retrieve the API key from environment variables
    api_key = os.getenv('WEATHER_API_KEY')
    if not api_key:
        raise ValueError("WEATHER_API_KEY environment variable not set.")
    
    # Prompt user for city and state
    city = input("Enter the city name: ")
    state = input("Enter the state code (e.g., NY for New York): ")
    
    # Fetch coordinates for the specified city and state
    coordinates = get_coordinates(api_key, city, state)
    if coordinates:
        lat, lon = coordinates
        # Fetch weather data for the retrieved coordinates
        weather_data = get_weather_data(api_key, lat, lon)
        if weather_data:
            # Print the current weather information
            print_current_weather(weather_data)
        else:
            print("Failed to retrieve weather data.")
    else:
        print("Failed to retrieve coordinates.")

if __name__ == "__main__":
    main()
