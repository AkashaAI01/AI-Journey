import requests

# Get request _ Retrive data
response = requests.get("https://httpbin.org/get", timeout=5)

# Check if succesful (200 = ok)
print(response.status_code)

# Get json response as a python dict
data = response.json()
print (data ['origin'])

# post request and send data 
response = requests.post(
    "https://httpbin.org/post",
    json = {"name": "Ahmad", "course": "AI engineering"}
)
print(response.status_code)