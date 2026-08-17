# Stdents Data
students = [
    {"name": "ALi", "age": 16, "grade": "A", "city": "Lahore"},
    {"name": "Ahamad", "age": 17, "grade": "B", "city": "Lahore"},
    {"name": "Usama", "age": 14, "grade": "F", "city": "Karachi"},
]

# Print all students data
print("All Students: ")

for student in students:
    print(student)

# Search any student through name
search = input("\nEnter a student name to search: ")

found = False
for student in students:
    if student["name"].lower() == search.lower():
        print("\n Student record found")
        print("Name: ", student["name"])
        print("Age: ", student["age"])
        print("Grade: ", student["grade"])
        print("City: ", student["city"])

        found = True
        break

if not found:
    print("Student record doesn't match")

#Adittional bonus to add new stdent record
addstudent = input("Do you want to add new student? (Yes/No)")
if addstudent.lower() == "Yes".lower():
    print("\n Enter your data")
    name = input("Student name: ")
    age = int(input("Student age: "))
    grade = input("Student grade: ")
    city = input("Student city: ")

    new_student = {
    "name": name,
    "age": age,
    "grade": grade,
    "city": city
    }

    students.append(new_student)
    print("\n New student added successfuly!")
    print(new_student)

    print("\n Updated Student List: ")
    for student in students:
        print(student)
     
elif addstudent.lower() == "No".lower():
    print("Got it!")

else:
    print("Invalid command. Only enter (Yes or No)")