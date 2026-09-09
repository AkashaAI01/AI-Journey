
try:
    number = int(input("Enter a number: "))
    result = 10 / number
    print(f"Result: {result}")
except ZeroDivisionError:
    print("Error: You cannot divide by zero.")
except ValueError:
    print("Error: Invalid input. Please enter a valid integer.")

print("program continues normally after the error.")

try:
    result = int("Not a number")
except ValueError as e:
    print(f"Error: {e}")

try:
    data = {"name": "Ahmad"}
    print(data["age"])
except KeyError as e:
    print(f"Missing key: {e}")