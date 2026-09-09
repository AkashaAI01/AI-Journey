import json

def load_and_parse(filename, key):
    try:
        with open(filename, 'r') as f:
            data = json.load(f)

        value = data[key]
        return value

    except FileNotFoundError:
        print(f"❌ The file '{filename}' was not found.")
        print("Please enter a valid filename.")

    except json.JSONDecodeError as e:
        print(f"❌ Error: file is not a valid JSON. {e}")
        print(" The file may be currepted")

    except KeyError as e:
        print(f"❌ Key not found in the file: {e}")
        print("Check the key name and try again.")

    except PermissionError:
        print(f"❌ No permission to read the file '{filename}'.")
        print("Please check the file permissions and try again.")

    except Exception as e:
        print(f" ❌ An unexpected error occurred: '{type(e).__name__}': {e}")

    return None

result = load_and_parse("data.json", "username")
if result:
    print(f"✅ Got: {result}") 