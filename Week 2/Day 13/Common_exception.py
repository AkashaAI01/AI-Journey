import json

# ValueError — wrong type conversion
try:
    Age = int("twenty")
except ValueError as e:
    print(f"Value Error: {e}")

# KeyError — accessing missing dict key
try:
    data = {"name": "Akasha"}
    print(data["email"])
except KeyError:
    print("Key Error: 'email' key not found.")

     # Better solution: use .get() to avoid this entirely
    email = data.get("email", "Not provided")

# FileNotFoundError
try:
    with open("missing.json") as f:
        data = json.load(f)
except FileNotFoundError:
    print("File not found.")
    data = {}

# AttributeError — calling method on None
try:
    value = None
    result = value.strip()
except AttributeError:
    print("Attribute Error: The value is None. Cannot call 'strip()'.")
    result = ""