import json

def load_or_create(filename, default=None):
    """
    Load JSON file if it exists, or return default if it doesn't.
    This pattern is used in EVERY project that saves data.
    """
    if default is None:
        default = []

    try:
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
        print(f"✅ Loaded {filename}")
        return data

    except FileNotFoundError:
        print(f"📝 {filename} not found — starting fresh")
        return default

    except json.JSONDecodeError:
        print(f"⚠️ {filename} is corrupted — starting fresh")
        return default

# Usage — you used this pattern in Day 11 already!
history = load_or_create("data.json", default=[])