import requests
import time

def api_call_with_retry(url, max_retries=3, delay=2):
    """
    Call API with automatic retry on failure.
    Waits 'delay' seconds between retries.
    Used in production AI systems everywhere.
    """
    for attempt in range(1, max_retries + 1):
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            return response.json()   # success — return data

        except requests.exceptions.Timeout:
            print(f"⏱ Attempt {attempt}/{max_retries}: Timeout. Retrying...")

        except requests.exceptions.ConnectionError:
            print(f"🔌 Attempt {attempt}/{max_retries}: No connection. Retrying...")

        except requests.exceptions.HTTPError as e:
            if response.status_code == 429:
                print(f"⚠️ Rate limited. Waiting {delay*2}s...")
                time.sleep(delay * 2)   # wait longer for rate limits
            else:
                print(f"❌ HTTP Error {response.status_code}: {e}")
                return None   # don't retry on 4xx errors

        if attempt < max_retries:
            time.sleep(delay)   # wait before retrying

    print(f"❌ All {max_retries} attempts failed.")
    return None

url = "https://jsonplaceholder.typicode.com/users"

data = api_call_with_retry(url)

if data:
    print("\n  📦 API Response: \n")
    print(data)