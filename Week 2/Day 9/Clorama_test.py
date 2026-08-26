from colorama import Fore, Back, Style, init

init()

# text color 
print(Fore.GREEN + "Successful message!" + Style.RESET_ALL)
print(Fore.RED + "Error message" + Style.RESET_ALL)
print(Fore.YELLOW + "Warning message" + Style.RESET_ALL)
print(Fore.CYAN + "Info message" + Style.RESET_ALL)

# Backgroud colors 
print(Back.YELLOW + Fore.WHITE + "Highlited text" + Style.RESET_ALL)

print(Fore.CYAN + "You: " + Style.RESET_ALL)
