
---

# Weather Fetcher 🌦️

Weather Fetcher is a Python script designed to fetch and display current weather information for a specified city and state within the United States. It utilizes the OpenWeather API to obtain geocoding and weather data.

## Features ⭐

- 🌟 **Intuitive Interface**: Simple and user-friendly command-line interface.
- 📱 **Responsive Design**: Enjoy a seamless experience on both desktop and mobile devices.
- ⚡ **Swift Responsiveness**: Fast and reliable performance.
- 🛠️ **Effortless Setup**: Easily install and configure with minimal effort.
- 🎨 **Customization**: Modify and extend the script to fit your specific needs.
- 🧩 **Code Syntax Highlighting**: Enhanced readability with syntax highlighting.
- 📚 **Comprehensive Documentation**: Detailed and easy-to-follow documentation.

## Requirements 📋

- Python 3.x
- `requests` library

## Installation 🚀

1. **Clone the repository or download the script**:
   ```bash
   git clone https://github.com/curlyphries/open-weather-map.git
   cd open-weather-map
   ```

2. **Install the required Python packages**:
   ```bash
   pip install requests
   ```

3. **Set up your OpenWeather API key**:
   - Obtain an API key from [OpenWeather](https://home.openweathermap.org/users/sign_up).
   - Set the API key as an environment variable:
     ```bash
     export WEATHER_API_KEY='your_api_key_here'
     ```

## Usage 📦

1. **Run the script**:
   ```bash
   python weather_fetcher.py
   ```

2. **Input the city and state code** when prompted:
   ```
   Enter the city name: [City Name]
   Enter the state code (e.g., NY for New York): [State Code]
   ```

3. **View the current weather information** displayed in the terminal.

## Functions 🔧

### `get_coordinates(api_key, city, state)`

Fetches the latitude and longitude for the given city and state using the OpenWeather Geocoding API.

- **Parameters**:
  - `api_key` (str): Your OpenWeather API key.
  - `city` (str): The name of the city.
  - `state` (str): The state code (e.g., 'NY' for New York).

- **Returns**:
  - A tuple (latitude, longitude) if the city is found.
  - `None` if the city is not found.

### `get_weather_data(api_key, lat, lon, units='imperial')`

Fetches the current weather data for the given latitude and longitude using the OpenWeather API.

- **Parameters**:
  - `api_key` (str): Your OpenWeather API key.
  - `lat` (float): Latitude.
  - `lon` (float): Longitude.
  - `units` (str, optional): Units of measurement. Default is 'imperial'.

- **Returns**:
  - A dictionary containing the weather data.

### `print_current_weather(weather_data)`

Prints the current weather information in a user-friendly format.

- **Parameters**:
  - `weather_data` (dict): The weather data returned by the `get_weather_data` function.

## Example 🌟

```bash
$ python weather_fetcher.py
Enter the city name: Denver
Enter the state code (e.g., NY for New York): CO

Current Weather for Now:
Temperature: 75.0°F, feels like 75.0°F
Condition: Clear sky
Humidity: 30%
Wind Speed: 5.0 mph
Visibility: 10.00 miles
```

## Error Handling ❗

- The script checks if the `WEATHER_API_KEY` environment variable is set.
- It raises an exception if the environment variable is not set.
- It handles HTTP request errors and prints relevant messages if the city is not found or if weather data retrieval fails.

## License 📄

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing 🤝

Contributions are welcome! Please open an issue or submit a pull request for any changes or improvements.

