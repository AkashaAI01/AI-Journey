import requests

# Method 1 check manually

response = requests.get("https://httpbin.org/get", timeout=5)
if response.status_code == 200:
    data = response.json()
    print("Success! ", data)
else:
    print(f"Failed! {response.status_code}")

# Method 2 response.ok

if response.ok:
    print("Request was successfull!")

# Method 3 raise_for_status()

try:
    response.raise_for_status()
    data = response.json()
    print(data)
except requests.exceptions.HTTPError as e:
    print(f"HTTP Error: {e}")