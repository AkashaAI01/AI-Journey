import os
import sys
import json
import requests
from datetime import datetime
from dotenv import load_dotenv
from colorama import Fore, Back, Style, init

# intializing
init()
load_dotenv()

# Constants
api_key = os.getenv("OPENWEATHER_API_KEY")
default_city = os.getenv("DEFAULT_CITY", "Lahore")
units = os.getenv("UNITS", "metric")
timeout = int(os.getenv("REQUEST_TIMEOUT", 10))
base_url = "https://api.openweathermap.org/data/2.5/weather"
history_file = "weather_history.json"
temp_unit = "°C" if units == "metric" else "°F"

# Weather emojis 
weather_emoji = {
    "Clear":        "☀",
    "Cloads":       "☁",
    "Rain":         "🌧",
    "Drizzle":      "🌦",
    "Thunderstorm": "⛈",
    "Snow":         "❄",
    "Mist":         "🌫",
    "Fog":          "🌫",
    "Haze":         "🌫",
    "Dust":         "💨",
    "Sand":         "🌬",
    "Tornado":      "🌪"
}

# Check the API key exists before starting the program 
def validate_config():
    if not api_key:
        print(f"{Fore.RED} Open weather API key not found in .env file {Style.RESET_ALL}")
        print("  1. Get a free key at open weather.org")
        print("  2. Add OPENWEATHER_API_KEY=your_key in .env file.")
        sys.exit(1)

# History Fumctions _______
def load_history():
    try:
        with open(history_file, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print(f"{Fore.YELLOW} History file is crupted starting a fresh file. {Style.RESET_ALL}")
        return []

def save_history(history):
    try:
        with open(history_file, "w", encoding="utf-8") as f:
            json.dump(history, f, indent=2, ensure_ascii=False)
    except (OSError, PermissionError) as e:
        print(f"{Fore.RED} history could not saved: {e} {Style.RESET_ALL}")

# Fetch the weather data 
def fetch_weather(city):
    params = {
        "q": city,
        "appid": api_key,
        "units": units
    }
    try:
        response = requests.get(base_url, params=params, timeout=timeout)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError:
        code = response.status_code
        if code == 401:
            print(f"{Fore.RED} Invalid API key check your key and try again. {Style.RESET_ALL}")
        elif code == 404:
            print(f"{Fore.RED} City could not found. {Style.RESET_ALL}")
        elif code == 429:
            print(f"{Fore.RED} Rate limit reach wait for a minute and then try again... {Style.RESET_ALL}")
        else:
            print(f"{Fore.RED} Server error please try again later. {Style.RESET_ALL}")

    except requests.exceptions.ConnectionError:
        print(f"{Fore.RED} Your internet is disconected plz check your internet and try again. {Style.RESET_ALL}")

    except requests.exceptions.Timeout:
        print(f"{Fore.RED} Requested timeout please try again. {Style.RESET_ALL}")

    except requests.exceptions.RequestException as e:
        print(f"{Fore.RED} Unexpected error: {e} {Style.RESET_ALL}")

    return None

# Display the weather data
def display_weather(data):
    city = data["name"]
    country = data["sys"]["country"]
    temp = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]
    temp_min = data["main"]["temp_min"]
    temp_max = data["main"]["temp_max"]
    humidity = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"]
    description = data["weather"][0]["description"].title()
    condition = data["weather"][0]["main"]
    visibility = data.get("visibility", 0) / 1000
    emoji = weather_emoji.get(condition, "🌡")

    print(Fore.CYAN + "=" * 45)
    print(f"🌎 {city}, {country}  ".center(45))
    print("=" * 45 + Style.RESET_ALL)
    print(Fore.WHITE + f" 🌡 Temperature  : " + Fore.YELLOW + f" {temp}{temp_unit}" + Style.RESET_ALL)
    print(Fore.WHITE + f" 🌡 Feels like   : " + Fore.YELLOW + f" {feels_like}{temp_unit}" + Style.RESET_ALL)
    print(Fore.WHITE + f" 📊 Min / Max   : " + Fore.YELLOW + f" {temp_min}{temp_unit} / {temp_max}{temp_unit}" + Style.RESET_ALL)
    print(Fore.WHITE + f" 💧 Humidity    : " + Fore.BLUE + f" {humidity}%" + Style.RESET_ALL)
    print(Fore.WHITE + f" 💨 Wind speed  : " + Fore.GREEN + f" {wind_speed}" + Style.RESET_ALL)
    print(Fore.WHITE + f" 👁 Visibility   : " + Fore.GREEN + f" {visibility: .1f} km" + Style.RESET_ALL)
    print(Fore.WHITE + f" {emoji} condition    : " + Fore.MAGENTA + description + Style.RESET_ALL)
    print(Fore.CYAN + "=" * 45 + Style.RESET_ALL + "\n")

# Display the search history
def display_history(history):
    print(Fore.BLUE + "=" * 80)
    print("📃 Weather History".center(80))
    print("=" * 80 + Style.RESET_ALL)

    if not history:
        print(Fore.YELLOW + " Search history is empty. Search the weather of any city." + Style.RESET_ALL + "\n")
        return
    for i, entry in enumerate(history[-10:], 1):
        print(
            Fore.WHITE + f" {i:>3}. " +
            Fore.YELLOW + f" {entry.get('city', '?'):<20} " +
            Fore.CYAN + f" {entry.get('temp', '?'):<10} " +
            Fore.GREEN + f" {entry.get('description', '?'):<20} " +
            Fore.BLUE + f" {entry.get('searched_at', '?')}" +
            Style.RESET_ALL
        )

    print(Fore.BLUE + "_" * 80 + Style.RESET_ALL)

# Handle the search history
def handle_search(history):
    city = input(Fore.YELLOW + f"\n Enter a city name (Or press enter for {default_city}: ) " + Style.RESET_ALL).strip()
    if not city:
        city = default_city

    print(Fore.BLUE + f"  🔎 Fetching weather for {city}........ " + Style.RESET_ALL)

    data = fetch_weather(city)
    if data is None:
        return

    display_weather(data)

    # Save the searched data to history
    history.append({
        "city":        f"{data['name']}, {data['sys']['country']}",
        "temp":        f"{data['main']['temp']}{temp_unit}",
        "description": data["weather"][0]["description"].title(),
        "humidity":    f"{data['main']['humidity']}%",
        "wind":        f"{data['wind']['speed']} m/s",
        "searched_at": datetime.now().strftime("%Y-%m-%d %H:%M"),
    })
    save_history(history)

# Create a main menu of the program
def print_menu():
    print(Fore.CYAN + f"\n  _=======================_")
    print(" ||  🌤  Weather CLI Bot   ||")
    print(" ||-----------------------||")
    print(" || 1. 🔎 Search City     ||")
    print(" || 2. 📃 Print History   ||")
    print(" || 3. 🧹 Clear History   ||")
    print(" || 4. 🚪 Exit            ||")
    print(" ||_______________________||" + Style.RESET_ALL)

# Main program entry point
def main():
    validate_config()
    history = load_history()

    print(Fore.GREEN + " ✅ Weather bot started! API keys are loaded. " + Style.RESET_ALL)

    try:
        while True:
            print_menu()
            choice = input("\n" + Fore.CYAN + " Choose (1 - 4): ")
            if choice == "1":
                handle_search(history)
            elif choice == "2":
                display_history(history)
            elif choice == "3":
                confirm = input(" Clear all history (Yes / No): ").lower().strip()
                if confirm == "yes":
                    history.clear()
                    save_history(history)
                    print(Fore.GREEN + " ✅ History Cleared. " + Style.RESET_ALL)
            elif choice == "4":
                break
                
            else:
                print(Fore.RED + " ❌ Invalid input. Please enter a valid number 1, 2, 3 or 4. " + Style.RESET_ALL)

    finally:
        print("\n" + Fore.CYAN + "👋 Thanks for using Weather Bot! Goodbye." + Style.RESET_ALL)

# Run the program
if __name__ == "__main__":
        main()