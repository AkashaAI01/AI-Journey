# 1. make a functions of add, subtrect, multiplication and division
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    """
    Divides a by b.
    Returns error message if b is zero.
    """
    if b == 0:
        return "Division erorr. Number is not divided by zero"
    return a / b

# 2. Grade score
def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

while True:
    print("\n_Calculator full menue_")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Grade")
    print("6. Exit")
    choice = input("\nChoose a number of a function: ")

    if choice == "6":
        print("\nAllah Hafiz ☺")
        break

    elif choice == "5":
        score = float(input("\nEnter your score: "))
        result = get_grade(score)
        print("Grade", result)

    elif choice in ["1", "2", "3", "4"]:
        a = float(input("Enter your first number: "))
        b = float(input("Enter your second number: "))

        if choice == "1":
            result = add(a, b)
        elif choice == "2":
            result = subtract(a, b)
        elif choice == "3":
            result = multiply(a, b)
        elif choice == "4":
            result = divide(a, b)

        print("\nResult:", result)

    else:
        print("\ninvalid input. Please try again and choose a correct number for a funcion.")
        print("Thank you! ")