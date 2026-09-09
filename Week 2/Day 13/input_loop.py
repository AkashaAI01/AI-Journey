def get_valid_number(prompt, min_val=None, max_val=None):
    """Keep asking user for a number until they give a valid one."""
    while True:
        try:
            value = int(input(prompt))
            if min_val is not None and value < min_val:
                print(f"❌ Must be at least {min_val}. Try again.")
                continue
            if max_val is not None and value > max_val:
                print(f"❌ Must be at most {max_val}. Try again.")
                continue
            return value   # valid — exit the loop

        except ValueError:
            print("❌ Please enter a whole number.")

# Usage:
age = get_valid_number("Enter your age: ", min_val=1, max_val=120)
score = get_valid_number("Enter score (0-100): ", min_val=0, max_val=100)