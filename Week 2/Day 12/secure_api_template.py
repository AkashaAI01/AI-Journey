"""
Secure API Project Template
----------------------------
Use this structure for EVERY project that uses API keys.
Project structure:
    my-project/
    ├── .env           ← your secrets (NEVER commit)
    ├── .gitignore     ← protects .env from Git
    ├── requirements.txt
    └── main.py        ← this file
"""

import os
import sys
import requests
from dotenv import load_dotenv

# ── Step 1: Load .env file ───────────────────────────────────
load_dotenv()

# ── Step 2: Load and validate required keys ──────────────────
def load_config():
    """Load all required environment variables. Exit if any are missing."""
    config = {
        "api_key":    os.getenv("WEATHER_API_KEY"),
        "app_name":   os.getenv("APP_NAME", "MyApp"),
        "debug":      os.getenv("DEBUG", "False") == "True",
        "timeout":    int(os.getenv("TIMEOUT", "10")),
    }

    # Validate required keys — exit with helpful message if missing
    required = ["api_key"]
    for key in required:
        if config[key] is None:
            print(f"❌ Missing required env var: {key.upper()}")
            print("   Add it to your .env file and try again.")
            sys.exit(1)

    return config

# ── Step 3: Use config in your API calls ─────────────────────
def call_api(config):
    """Make a secure API call using key from environment."""
    try:
        response = requests.get(
            "https://api.example.com/data",
            headers={"Authorization": f"Bearer {config['api_key']}"},
            params={"query": "Lahore"},
            timeout=config["timeout"]
        )
        response.raise_for_status()
        return response.json()

    except requests.exceptions.ConnectionError:
        print("❌ No internet connection.")
    except requests.exceptions.Timeout:
        print("❌ Request timed out.")
    except requests.exceptions.HTTPError as e:
        print(f"❌ HTTP Error: {e}")
    return None

# ── Step 4: Main entry point ──────────────────────────────────
def main():
    config = load_config()

    if config["debug"]:
        print(f"[DEBUG] App: {config['app_name']}")
        print(f"[DEBUG] Key: {config['api_key'][:8]}...")   # never print full key!

    data = call_api(config)
    if data:
        print("Data received successfully!")

if __name__ == "__main__":
    main()