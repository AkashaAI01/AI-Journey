import json
from colorama import Fore, Back, Style, init

init()

# Create a json text
Raw_data = '''
{
    "city": "Lahore",
    "country": "Pakistan",
    "temperature": {
        "celsius": 45,
        "fahrenheit": 95
    },
    "weather": "Sunny",
    "humidity": 45,
    "wind_speed": 12,
    "forecast": ["Sunny", "Claudy", "Rainy"],
    "is_daytime": true,
    "air_quality": null
}
'''

Weather = json.loads(Raw_data)

print(f"City        : {Weather['city']}, {Weather['country']}")
print(f"Temperature : {Weather['temperature']['celsius']}°C")
print(f"Weather     : {Weather['weather']}")
print(f"Humidity    : {Weather['humidity']}")
print(f"Wind_Speed  : {Weather['wind_speed']}")
print(f"fore cast   : 3 Days")
print(Fore.CYAN + f"Yesterday : {Weather['forecast'][0]}\n    Today : {Weather['forecast'][1]}\n    Tomorrow : {Weather['forecast'][2]}" + Style.RESET_ALL)
print(f"Is_Daytime  : {Weather['is_daytime']}")
print(f"Air_Quality : {Weather['air_quality']}")

print(Fore.GREEN + "\n     Successfully completed weather API through json...... " + Style.RESET_ALL)
print(Fore.RED + "          Thak gia ra baba bs bs ho gai.\n" + Style.RESET_ALL)