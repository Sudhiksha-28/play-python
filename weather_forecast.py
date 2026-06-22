# This is sample program to fetch and display a 7-day weather forecast using the Open-Meteo API.
# It demonstrates how to make API requests, handle JSON data, and format output for better readability
#Imports
import requests
from datetime import datetime

# Function to fetch and display weather forecast for given latitude and longitude
def get_weather_forecast(latitude, longitude):
    # Open-Meteo API URL for daily forecast
    url = f"https://api.open-meteo.com/v1/forecast"
    
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "daily": ["temperature_2m_max", "temperature_2m_min", "precipitation_probability_max", "weathercode"],
        "timezone": "auto" # Automatically use the local timezone of the coordinates
    }
    
    # Mapping Open-Meteo weather codes to human-readable descriptions
    weather_codes = {
        0: "Clear sky",
        1: "Mainly clear", 2: "Partly cloudy", 3: "Overcast",
        45: "Fog", 48: "Depositing rime fog",
        51: "Light drizzle", 53: "Moderate drizzle", 55: "Dense drizzle",
        61: "Slight rain", 63: "Moderate rain", 65: "Heavy rain",
        71: "Slight snow fall", 73: "Moderate snow fall", 75: "Heavy snow fall",
        77: "Snow grains",
        80: "Slight rain showers", 81: "Moderate rain showers", 82: "Violent rain showers",
        85: "Slight snow showers", 86: "Heavy snow showers",
        95: "Thunderstorm", 96: "Thunderstorm with slight hail", 99: "Thunderstorm with heavy hail"
    }

    try:
        print("request parameters: {}", params)
        response = requests.get(url, params=params)
        response.raise_for_status() # Raise an error for bad status codes
        data = response.json()
        print("✅ Weather data fetched successfully! {}",data)
        
        daily = data["daily"]
        
        print(f"\n--- 7-Day Weather Forecast (Lat: {latitude}, Lon: {longitude}) ---")
        
        # Loop through the next 7 days of forecast data
        for i in range(len(daily["time"])):
            print(f"\nDay {i + 1}:")
            raw_date = daily["time"][i]
            # Format date to a nicer readability (e.g., "Mon, Jun 15")
            formatted_date = datetime.strptime(raw_date, "%Y-%m-%d").strftime("%a, %b %d")
            
            max_temp = daily["temperature_2m_max"][i]
            min_temp = daily["temperature_2m_min"][i]
            rain_chance = daily["precipitation_probability_max"][i]
            code = daily["weathercode"][i]
            
            condition = weather_codes.get(code, "Unknown conditions")
            
            print(f"{formatted_date}: {condition}")
            print(f"  🌡️ Temperature: Low {min_temp}°C to High {max_temp}°C")
            print(f"  🌧️ Rain Chance: {rain_chance}%")
            print("-" * 40)
            
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")

if __name__ == "__main__":
    # Example coordinates: New York City (Latitude: 40.7128, Longitude: -74.0060)
    # You can change these to any coordinates you want!
    target_lat = 40.7128
    target_lon = -74.0060
    
    get_weather_forecast(target_lat, target_lon)
    target_lat = 140.7128
    target_lon = -34.0060
    get_weather_forecast(target_lat, target_lon)
   
