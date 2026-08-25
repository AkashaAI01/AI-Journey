import requests
from colorama import Fore, Back, Style, init
from dotenv import load_dotenv
import os

# initializing colorama
init()

# <<<<< Test 1 colorama >>>>>>>>>>>>>
print(Fore.YELLOW + "\n<<< Starting libraries tests... >>>\n" + Style.RESET_ALL)
print(Fore.GREEN + "\n<<< SUCCESS colorama activated! >>>\n" + Style.RESET_ALL)
print(Fore.BLUE + "<<< INFO All libraries are loaded successfully. >>>\n" + Style.RESET_ALL)

# <<<<< Test 2 requests >>>>>>>>>>>>>
print(Fore.CYAN + "<<< Testing the request library! >>> \n" + Style.RESET_ALL)

try:
    response = requests.get("https://httpbin.org/get", timeout=5)
    print(f"Status code: {response.status_code}")
    print(f"Success: {response.status_code == 200}")
    data = response.json()
    print(f"Your IP: {data['origin']}")
    print(Fore.GREEN + "Successful requests working... \n" + Style.RESET_ALL)

except requests.exceptions.ConnectionError:
    print(Fore.RED + "No internet connection. \n" + Style.RESET_ALL)
except requests.exceptions.Timeout:
    print(Fore.RED + "Error request timed out...... \n" + Style.RESET_ALL)

# <<< Test 3 Python_dotenv library >>>>>>>>>>>
print(Fore.CYAN + "Testing dotenv library... \n" + Style.RESET_ALL)

load_dotenv()
name = os.getenv("MY_NAME")
learning = os.getenv("LEARNING")
Weather_API = os.getenv("WEATHER_API_KEY") 
print(f"Name: {name}")
print(f"Learning: {learning}")
print(f"Weather API KEY: {Weather_API}")
print(Fore.GREEN + "Successful Dotenv working! \n" + Style.RESET_ALL)

# <<<<<<<<<< Summary >>>>>>>>>>>>>
print(Fore.YELLOW + "=" * 45 + Style.RESET_ALL)
print(Fore.GREEN + "All 3 libraries working correctly...." + Style.RESET_ALL)
print(Fore.YELLOW + "=" * 45 + Style.RESET_ALL)
print("\n Requests : Call APIs from python.")
print(" Python_Dotenv : Load secrets from .env file.")
print(" Colorama : Colored terminal output.\n")