import requests

# GET request — retrieve data (most common)
response = requests.get("https://api.example.com/data")

# POST request — send data
response = requests.post("https://api.example.com/create", json={"name": "Ahmad"})

# GET with query parameters
response = requests.get("https://api.example.com/weather", params={"city": "Lahore"})

# GET with headers (API key authentication)
response = requests.get(
    "https://api.example.com/data",
    headers={"Authorization": "Bearer YOUR_API_KEY"},
    timeout=5        # stop waiting after 5 seconds
)

# What the response object contains:
print(response.status_code)   # 200 = success, 404 = not found
print(response.text)          # raw response as string
print(response.json())        # parse JSON → Python dict (most used)
print(response.headers)       # response headers dict
print(response.url)           # the exact URL that was called