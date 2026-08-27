import json
from colorama import Fore, Back, Style, init
init()

# ==============================================
#     Create a student record in dictionory
# ==============================================

Students = [
    {
        "name": "Akasha", 
        "score": 97,
        "grade": "A+",
        "city": "Lahore",
        "Pass": "Pass",
        "failed": "-"
    },
    {
        "name": "Ali",
        "score": 73,
        "grade": "C",
        "city": "Islamabad",
        "Pass": "Pass",
        "failed": "-"
    },
    {
        "name": "Ahmad", 
        "score": 80,
        "grade": "B",
        "city": "Karachi",
        "Pass": "Pass",
        "failed": "-"
    },
    {
        "name": "Minha",
        "score": 90,
        "grade": "A",
        "city": "Multan",
        "Pass": "Pass",
        "failed": "-"
    },
    {
        "name": "Bisma",
        "score": 44,
        "grade": "F",
        "city": "Peshawar",
        "Pass": "-",
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

# __________________________________________________________
# ==========================================================
#   Creating main while true loop for perform any task
# __________________________________________________________
# ==========================================================

while True:
    print("\n" + Fore.BLUE + "========= Student Record System =========" + Style.RESET_ALL)
    print("    1. Show all students")
    print("    2. Search student record")
    print("    3. Add new student")
    print("    4. Top score holder")
    print("    5. Exit")
    choice = input("\n What do you want to do: (Choose any number to perform task) ")
    if choice == "5":
        print("\n  Good bye. Thanks for your time. \n")
        break


#    =======================================================
#       1. Show the Students Record in the form of table
#    =======================================================
    
    elif choice == "1":
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

#    ================================
#         2. Search a student 
#    ================================
    
    elif choice == "2":
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

#    ==========================
#       3. Add new student 
#    ==========================

    elif choice == "3":
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

                print("\n" + Fore.GREEN + "New student added successfully." + Style.RESET_ALL)
                
            elif add_student == "no":
                print("\n  Ok Thanks for coming.\n")
                break

            else:
                print("\n  Error: Invalid input (Enter only yes or no)\n")

#    ==================================================
#       4. Find the student who have highest marks
#    ==================================================
    elif choice == "4":
        top = max(Students, key = lambda s: s["score"])

        print("\n Top scoring student.\n")
        print(f"Name      : {top['name']}")
        print(f"City      : {top['city']}")
        print(f"Score     : {top['score']}")
        print(f"Grade     : {top['grade']}")
        print(f"Pass/Fail : {top['Pass']}")

    else:
        print("\n" + Fore.RED + "  Error: Invalid input! Choose any number (1, 2, 3, 4 or 5) " + Style.RESET_ALL)

print("=" * 50)
print(Fore.RED + "     _____ It is the enddddddddd! _____" + Style.RESET_ALL)
print("=" * 50)