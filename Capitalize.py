# Ask the name from the user
Name = input("What is your name? ")

# Remove white space from the beginning and end of the name 
Name = Name.strip()

# Capitalize the user's name
Name = Name.capitalize()

# Say hello to user 
print(f"Hello, {Name}!")
