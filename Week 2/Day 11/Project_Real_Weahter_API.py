import requests


# ============================================
# Get latitude and longitude of a city
# ============================================

def get_coordinates(city):

    geocoding_url = "https://geocoding-api.open-meteo.com/v1/search"

    params = {
        "name": city,
        "count": 1,
        "language": "en",
        "format": "json"
    }

    response = requests.get(
        geocoding_url,
        params=params,
        timeout=10
    )

    response.raise_for_status()

    data = response.json()

    if "results" not in data:
        return None

    location = data["results"][0]

    return (
        location["latitude"],
        location["longitude"],
        location["name"],
        location.get("country", "Unknown")
    )


# ============================================
# Get weather forecast
# ============================================

def get_weather(latitude, longitude):

    weather_url = "https://api.open-meteo.com/v1/forecast"

    params = {
        "latitude": latitude,
        "longitude": longitude,

        "current": "temperature_2m,relative_humidity_2m,wind_speed_10m",

        "daily": "temperature_2m_max,temperature_2m_min,weather_code",

        "timezone": "auto"
    }

    response = requests.get(
        weather_url,
        params=params,
        timeout=10
    )

    response.raise_for_status()

    return response.json()


# ============================================
# Main Program
# ============================================

while True:

    city = input("\nEnter city name (or 'quit' to exit): ").strip()

    # Quit program
    if city.lower() == "quit":
        print("👋 Weather App closed. Goodbye!")
        break

    # Empty input
    if not city:
        print("❌ Please enter a city name.")
        continue

    try:

        # Get coordinates
        location = get_coordinates(city)

        if location is None:
            print(f"❌ City '{city}' was not found.")
            continue

        latitude, longitude, city_name, country = location

        # Get weather
        data = get_weather(latitude, longitude)

        current = data["current"]
        daily = data["daily"]


        # ====================================
        # Current Weather
        # ====================================

        print("\n===================================")
        print("       🌤️ WEATHER INFORMATION")
        print("===================================")

        print(f"City        : {city_name}")
        print(f"Country     : {country}")

        print("\n--- Current Weather ---")

        print(f"Temperature : {current['temperature_2m']}°C")
        print(f"Humidity    : {current['relative_humidity_2m']}%")
        print(f"Wind Speed  : {current['wind_speed_10m']} km/h")
        print(f"Time        : {current['time']}")


        # ====================================
        # 7 Day Forecast
        # ====================================

        print("\n--- 7 Day Forecast ---")

        for i in range(len(daily["time"])):

            date = daily["time"][i]

            max_temp = daily["temperature_2m_max"][i]
            min_temp = daily["temperature_2m_min"][i]

            weather_code = daily["weather_code"][i]

            print(
                f"{date} | "
                f"Min: {min_temp}°C | "
                f"Max: {max_temp}°C | "
                f"Weather Code: {weather_code}"
            )


    except requests.exceptions.ConnectionError:

        print("❌ No internet connection.")

    except requests.exceptions.Timeout:

        print("❌ Request timed out. Please try again.")

    except requests.exceptions.RequestException as e:

        print(f"❌ API Error: {e}")

    except (KeyError, IndexError):

        print("❌ Unexpected data received from API.")