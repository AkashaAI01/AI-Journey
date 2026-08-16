import os
os.system('cls')
shopping = []
while True:
    command = input("Choose any command (add, remove, list, or quit):").lower()
    if command.lower() == "add":
        product = input("\n" "Pick up any item: ")
        shopping.append(product)
        print(f"{product} added to shopping list. Pick up next item. \n")
    elif command.lower() == "remove":
        product = input("\n" "Which item do you want to remove? ").lower()
        if product in shopping:
            shopping.remove(product)
            print(f"{product} removed from shopping list." "\n")
        else:
            print(f"{product} is not in the shopping list." "\n")
    elif command.lower() == "list":
        if len(shopping) == 0:
            print("\n" "Your shopping list is empty." "\n")
        else:
            print("\n" "Your shopping list:")
            for number, item in enumerate(shopping, start=1):
                print(f"{number}. {item}")
    elif command.lower() == "quit":
        print("\n" "Final shopping list.")
        if len(shopping) == 0:
            print("Your shopping list is empty.")
        else:
            for number, item in enumerate(shopping, start=1):
                print(f"{number}. {item}")
        break

    else:
        print("\n" "Invalid command. Please choose from add, remove, list, or quit.")