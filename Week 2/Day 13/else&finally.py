while True:
    try:
        number = int(input("Enter a numer: "))
        result = 100/number

    except ValueError:
        print("Please enter a valid integer.")

    except ZeroDivisionError:
        print("Number is not divided by zero.")
    else:
        print(f"Result: {result}")
        break
    finally:
        print("Your code will run afer clean the error.")