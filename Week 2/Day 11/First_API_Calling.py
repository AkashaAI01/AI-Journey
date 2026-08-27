import requests
import json

print("\n   It is my fisrt real API calling through python..... ")

url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url, timeout=10)

print(f"\n Status code: {response.status_code}")
print(f"\n Success {response.ok}")

users = response.json()

print("\n  _____ User Data _____")
for user in users:
    print(f" Name     : {user['name']}")
    print(f" Email    : {user['email']}")
    print(f" Phone    : {user['phone']}")
    print(f" Website  : {user['website']}")
    print(f" City     : {user['address']['city']}")
    print(f" Company  : {user['company']['name']}")

print("\n  _____ Full json response _____")
print(json.dumps(user, indent=4))