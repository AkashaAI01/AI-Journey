students = ["Ali", "Ahmed", "Sara", "Akasha"]

# simple for loop
for student in students:
    print(f"Hello, {student}!")

# loop with index using enumerate
for i, student in enumerate(students):
    print(f"{i+1}. {student}")

#useful if item is in a list
if "Sara" in students:
    print("Sara is present in the class.")
