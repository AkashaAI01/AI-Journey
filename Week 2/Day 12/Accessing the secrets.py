import os
from dotenv import load_dotenv

# Load .env file — call this ONCE at the top of your program
load_dotenv()

# Now access your keys safely
api_key  = os.getenv("ANTHROPIC_API_KEY")
app_name = os.getenv("APP_NAME")
debug    = os.getenv("DEBUG")

print(f"App: {app_name}")
print(f"Key loaded: {api_key[:10]}...")   # only show first 10 chars — never print full key!
print(f"Debug mode: {debug}")