
# raise with built-in exceptions

def set_age(age):
    """Set user age between 0 to 120"""
    if not isinstance(age, int):
        raise TypeError("Age must be an integer.")
    if age < 0 or age > 120:
        raise ValueError("Age must be between 0 and 120.")
    return age

try:
    set_age("twenty")
except TypeError as e:
    print(f"Type Error: {e}")

try:
    set_age(-5)
except ValueError as e:
    print(f"Value Error: {e}")

try: 
    set_age(130)
except ValueError as e:
    print(f"Value Error: {e}")

try: 
    set_age(20)
except Exception as e:
    print(f"Unexpected Error: {e}")
else:
    print(f"Age set successfully.")
# raise inside except — re-raise after logging
try:
    result = 10/0
except ZeroDivisionError as e:
    print(f"Zero division error: {e}")
    raise # Re-raise the exception to propagate it further