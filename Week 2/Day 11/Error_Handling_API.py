import requests

def call_api(url, params=None):
    """
    Makes a safe API call with full error handling
    Returns pased data and none of failure.
    """
    try:
        response = requests.get(url, params=params, timeout=10)

        # Check http status
        response.raise_for_status()

        return response.json()

    except requests.exceptions.ConnectionError:
        print("Error: No internet connection. Please check your connection.")

    except requests.exceptions.TimeoutError:
        print("Error: Run time out. Your server is too slow.")

    except requests.exceptions.HTTPError as e:
        print(f" ❌ HTTP Error: {response.status_code}: {e}")
        if response.status_code == 401:
            print("  ➡ Check your API key.")
        elif response.status_code == 429:
            print(" Rate limited. Wait for retrying.")
        elif response.status_code == 404:
            print(" Url not found. Please check the last line.")

    except requests.exceptions.RequestException as e:
        print(f" ❌ Unexpected error: {e}")

    return None

Data = call_api("https://jsonplaceholder.typicode.com/users/4")

if Data:
    print(f"\n Got Data : {Data['name']}.")
else:
    print("Could not retrieved data.")