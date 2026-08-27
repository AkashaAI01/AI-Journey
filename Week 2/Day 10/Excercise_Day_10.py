import json
from colorama import Fore, Back, Style, init

# ==============================================
#     Create a student record in dictionory
# ==============================================

Students = [
    {
        "name": "Akasha", 
        "score": 97,
        "grade": "A+",
        "city": "Lahore",
        "Pass": "Passed",
        "failed": "Null"
    },
    {
        "name": "Ali",
        "score": 73,
        "grade": "C",
        "city": "Islamabad",
        "Pass": "Passed",
        "failed": "Null"
    },    
    {
        "name": "Ahmad", 
        "score": 80,
        "grade": "B",
        "city": "Karachi",
        "Pass": "Passed",
        "failed": "Null"
    },
    {
        "name": "Minha",
        "score": 90,
        "grade": "A",
        "city": "Multan",
        "Pass": "Passed",
        "failed": "Null"
    },
    {
        "name": "Bisma",
        "score": 44,
        "grade": "F",
        "city": "Peshawar",
        "Pass": "Null",
        "failed": "Failed"
    }
]

# Use try except function to avoid from crash the program

try:
    with open ("Student_Records.json", "r") as f:
        Students = json.load(f)

    print(Fore.GREEN + "Student Records loaded!" + Style.RESET_ALL)

except FileNotFoundError:
    with open("Student_Records.json", "w") as f:
        json.dump(Students, f, indent=4)

    print("\n" + Fore.YELLOW + "New student record updated!" + Style.RESET_ALL)

# =======================================================
#     Show the Students Record in the form of table
# =======================================================

print("\n" + "=" * 80)
print(f"{'Name':<15}{'City':<15}{'Score':<10}{'Grade':<10}{'Pass':<10}{'Fail':<10}")
print("=" * 80)

for student in Students:
    print(
        f"{student['name']:<15}"
        f"{student['city']:<15}"
        f"{student['score']:<10}"
        f"{student['grade']:<10}"
        f"{student['Pass']:<10}"
        f"{student['failed']:<10}"
    )
print("\n" + "=" * 80)

# ================================
#        Search a student 
# ================================

search = input("Enter a student name: ").lower()

found = False

for student in Students:
    if student["name"].lower() == search:
        print("\n" + Fore.CYAN + " Student record found." + Style.RESET_ALL)
        print(f"\n Name  : {student['name']}")
        print(f" City  : {student['city']}")
        print(f" score : {student['score']}")
        print(f" Grade : {student['grade']}")
        print(f" Pass  : {student['Pass']}")
        print(f" Fail  : {student['failed']}\n")

        found = True
        break

if not found:
    print("\n Student not found.")

# ==========================
#     Add new student 
# ==========================
while True:
    add_student = input("Do you want to add new student? (yes/no) ").lower().strip()
    if add_student == "yes":
        name = input("Name : ")
        score = int(input("Score : "))
        grade = input("Grade : ")
        city = input("City: ")
        Pass = input("Pass : ")
        failed = input("Fail : ")

        new_student = {
            "name": name,
            "score": score,
            "grade": grade,
            "city": city,
            "Pass": Pass,
            "failed": failed
        }

        Students.append(new_student)

        with open("Student_Records.json", "w") as f:
            json.dump(Students, f, indent=4)

        print("\n New student added successfully.")
    elif add_student == "no":
        print("\nOk Thanks for coming.\n")
        break

    else:
        print("\nError: Invalid input (Enter only yes or no)\n")

# ==================================================
#      Find the student who have highest marks
# ==================================================
top = max(Students, key = lambda s: s["score"])

print("\n Top scoring student.\n")
print(f"Name      : {top['name']}")
print(f"City      : {top['city']}")
print(f"Score     : {top['score']}")
print(f"Grade     : {top['grade']}")
print(f"Pass/Fail : {top['Pass']}")

print("=" * 50)
print(Fore.RED + "     _____ It is the enddddddddd! _____" + Style.RESET_ALL)
print("=" * 50)