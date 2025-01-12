# Weather App - README

## Overview
This Weather App fetches real-time weather data for a specified city using the OpenWeatherMap API. Users can input a city name and view the current temperature, weather conditions, and an icon representing the weather.

## Key Features
1. **Fetch Weather Data**: Retrieve weather details for any city using the OpenWeatherMap API.
2. **Dynamic Display**: Display weather information dynamically on a web page.
3. **Simple Input**: Users can input a city name in the search bar to get weather updates.

## Code Explanation
### 1. **API Configuration**
- The OpenWeatherMap API endpoint (`https://api.openweathermap.org/data/2.5/weather`) is used to fetch weather data.
- The `api_key` is required for authentication.
- Weather icons are retrieved from `https://openweathermap.org/img/wn/{icon}@2x.png`.

### 2. **`get_weather(city)` Function**
- **Input**: Takes the city name as input.
- **Process**: Sends a request to the OpenWeatherMap API with the city name and API key.
- **Output**: Returns weather data (city name, country, temperature, condition, and icon) in a dictionary format.

### 3. **`weather_view(request)` Function**
- **Input**: Accepts an HTTP request.
- **Process**:
  - Retrieves the city name from the query parameters (`request.GET.get("city")`).
  - Calls the `get_weather()` function to fetch weather data for the specified city.
- **Output**: Renders the `weather/weather.html` template with the weather data passed as context.

## Installation and Setup
1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up the OpenWeatherMap API key:
   - Replace `fcc3b6b33d89d96dba7f76fbfd8c2920` with your API key in the code.
4. Run the Django development server:
   ```bash
   python manage.py runserver
   ```
5. Navigate to `http://127.0.0.1:8000` in your browser.

## Usage
1. Enter a city name in the search bar.
2. View the current weather information including temperature, condition, and an icon.

## File Structure
- `views.py`: Contains the logic for fetching and displaying weather data.
- `templates/weather/weather.html`: Template file for displaying weather data on the frontend.

## Notes
- Ensure you have a valid OpenWeatherMap API key.
- Handle cases where the city is not found or the API request fails gracefully.

