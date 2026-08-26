from dotenv import load_dotenv
import os

load_dotenv() # reads .env file and loads all variables
api_key = os.getenv("ANTHROPIC_API_KEY")
print(f"Key loaded: {api_key[:10]}...") # only show first 10 chars