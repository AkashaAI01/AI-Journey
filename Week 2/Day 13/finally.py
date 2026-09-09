file = None

try:
    file = open("data.txt", "r")

except FileNotFoundError:
    print("file not found")

finally:
    if file:
        file.close()
        print("File closed successfully!")