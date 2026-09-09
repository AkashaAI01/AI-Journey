import requests

from colorama import Fore, Back, Style, init

init()

# Get latitude and longitude of a city
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

    Data = response.json()
    if "results" not in Data:
        return None

    location = Data["results"][0]

    return(
        location["latitude"],
        location["longitude"],
        location["name"],
        location.get("country", "Unknown")
    )

# Get weather forcast by creating a function
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

# Main program
while True:
    city = input("\n\n Enter a city name (or 'quit' to exit): ").strip()

    if city.lower() == "quit":
        print(Fore.CYAN + "\n Wheather app closed.")
        print("     Good bye!" + Style.RESET_ALL)
        break

    if not city:
        print(Fore.YELLOW + "❌ Please Enter a city name" + Style.RESET_ALL)
        continue

    try:
        location = get_coordinates(city)

        if location is None:
            print(Fore.LIGHTMAGENTA_EX + f"\n  City {city} is not found." + Style.RESET_ALL)
            print("   Please try again")
            continue

        latitude, longitude, city_name, country = location
        print(f"   📍 City    : {city_name}")
        print(f"   🌍 Country : {country}")

        Data = get_weather(latitude, longitude)

        current = Data["current"]
        daily = Data["daily"]

        # Show current weather
        print(Fore.RED + "=" * 40)
        print(Fore.CYAN + "         🌤 WEATHER INFORMATION ")
        print(Fore.RED + "=" * 40)

        print(Fore.YELLOW + f"\n         Current weather of {city}" + Style.RESET_ALL)
        print(f"         Temperature : {current['temperature_2m']}°C")
        print(f"         Humidity    : {current['relative_humidity_2m']}%")
        print(f"         Wind Speed  : {current['wind_speed_10m']}km/h")
        print(f"         Time        : {current['time']}")

        # 7 days forecast
        print(Fore.YELLOW + f"\n\n                  7 days forcast of {city}" + Style.RESET_ALL)

        for i in range(len(daily["time"])):

            date = daily["time"][i]
            max_temp = daily["temperature_2m_max"][i]
            min_temp = daily["temperature_2m_min"][i]
            weather_code = daily["weather_code"][i]

            print(f"\n {date} | "
                f"Max Temperature : {max_temp}°C | "
                f"Min Temperature : {min_temp}°C | "
                f"Weather Code : {weather_code}"
            )

    except requests.exceptions.ConnectionError:
        print(Fore.RED + "\n Error: No internet connection." + Style.RESET_ALL)

    except requests.exceptions.Timeout:
        print(Fore.RED + "\n Error: Requested timeout. Please try again...." + Style.RESET_ALL)

    except requests.exceptions.RequestException as e:
        print(Fore.RED + f"\n API Error: {e}" + Style.RESET_ALL)

    except (KeyError, IndexError):
        print(Fore.RED + "\n Error: Unexpacted data recieved from API." + Style.RESET_ALL)