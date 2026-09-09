import json
import os
import time
from colorama import Fore, Back, Style, init

init()

File_name = "students.json"

                # -------------------------------------------------------------
                # Create a function to load student records from the json file.
                # -------------------------------------------------------------

def load_students():
    try:
        with open(File_name, "r") as f:
            students = json.load(f)

            if not isinstance(students, list):
                print(f"{Fore.RED}Error: The JSON file does not contain a list of students.{Style.RESET_ALL}")
                return []
            return students
    except FileNotFoundError:
        print(f"{Fore.YELLOW}File not found. Creating a new file.{Style.RESET_ALL}")
        return []
    except json.JSONDecodeError:
        print(f"{Fore.RED}Error: The JSON file is corrupted.{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}Creating a new file.{Style.RESET_ALL}")
        return []
    except PermissionError:
        print(f"{Fore.RED}Error: Permission denied to read the file.{Style.RESET_ALL}")
        return []
    except OSError:
        print(f"{Fore.RED}Error: A system error accurred while opening the file.{Style.RESET_ALL}")
        return []

                # ----------------------------------------------
                # Save the student data in the file with 3 tries 
                # ----------------------------------------------

def student_save(students, max_retries=3, delay=2):
    for attempt in range(1, max_retries + 1):
        try:
            with open(File_name, "w") as f:
                json.dump(students, f, indent=4)
            print(f"{Fore.GREEN} ✅ Student records saved successfully.{Style.RESET_ALL}")
            return True
        
        except PermissionError:
            print(f"{Fore.RED}Error: Permission denied to write to the file. \n   ⚠ Attempt {attempt}/{max_retries}. {Style.RESET_ALL}")
        except OSError:
            print(f"{Fore.RED}Error: A system error occurred while writing to the file. \n   ⚠ Attempt {attempt}/{max_retries}. {Style.RESET_ALL}")

        if attempt < max_retries:
                print(f"\n{Fore.YELLOW}Retrying in {delay} seconds...{Style.RESET_ALL}")
                time.sleep(delay)

    print(f"\n{Fore.RED}Failed to save student records after multiple attempts.{Style.RESET_ALL}")
    return False

                # ---------------------------------------------------
                # Get a valid number between 0 to 100 from the user.
                # ---------------------------------------------------

def get_valid_number(get_number):
    while True:
        try:
            score = float(input(get_number))
            if 0 <= score <= 100:
                return score
            else:
                print(f"\n{Fore.YELLOW}Error: Please enter a number between 0 and 100.{Style.RESET_ALL}")
        except ValueError:
            print(f"\n{Fore.RED}Error: Invalid input. Please enter a valid number.{Style.RESET_ALL}")
        except KeyboardInterrupt:
            print(f"\n {Fore.RED}Operation cancelled by user.{Style.RESET_ALL}")

                # ------------------------------------
                # Add new student data in the record.
                # ------------------------------------

def add_student(students):
    try:
        name = input("Enter student name: ").strip()
        if not name:
            print(f"\n{Fore.RED}Error: Student name cannot be empty.{Style.RESET_ALL}")
            return
        score = get_valid_number("Enter student score (0-100): ")
        city = input("Enter student city: ").strip()
        if not city:
            print(f"\n{Fore.RED}Error: Student city cannot be empty.{Style.RESET_ALL}")
            return

        student = {
            "name": name,
            "score": score,
            "city": city,
        }
        students.append(student)
        print(f"\n{Fore.GREEN}  {name} added successfully ✅ {Style.RESET_ALL}")
    except KeyboardInterrupt:
        print(f"\n{Fore.RED} Operation cancelled by user.{Style.RESET_ALL}")
    except Exception as e:
        print(f"\n{Fore.RED} An unexpected error occurred: {e}{Style.RESET_ALL}")

                # -------------------------
                # Display all the students
                # -------------------------

def display_students(students):
    if not students:
        print(f"\n{Fore.YELLOW}No student records found.{Style.RESET_ALL}")
        return

    print("\n" + "=" * 45)
    print(f"          Student Records")
    print("=" * 45 + "\n")
    for index, student in enumerate(students, start=1):
        print(
            f"{Fore.BLUE}{index}. Name: {student['name']} | "
            f"Score: {student['score']} | "
            f"City: {student['city']}{Style.RESET_ALL}"
        )
    print("\n" + "_" * 45 + "\n")

                # -----------------------------------------------------
                # Search a student by their name and display the data 
                # -----------------------------------------------------

def search_student(students):
    try:
        if not students:
            print(f"\n{Fore.YELLOW} No student records found.{Style.RESET_ALL}")
            return

        S_name = input("Enter a student name to search: ").strip().lower()
        if not S_name:
            print(f"\n{Fore.YELLOW}Error: Enter a student name.{Style.RESET_ALL}")
            return

        found_students = []
        for student in students:
            if S_name in student['name'].strip().lower():
                found_students.append(student)

        if found_students:
            print(f"\n{Fore.LIGHTWHITE_EX}  🔎 Search Results.... {Style.RESET_ALL}\n")
            for student in found_students:
                print(
                    f"{Fore.BLUE}Name: {student['name']} | "
                    f"Score: {student['score']} | "
                    f"City: {student['city']}{Style.RESET_ALL}"
                )
        else:
            print(f"\n{Fore.YELLOW} ❌ No student found with the name '{S_name}'.{Style.RESET_ALL}")

    except KeyboardInterrupt:
        print(f"\n{Fore.RED} Operation cancelled by user.{Style.RESET_ALL}")
    except Exception as e:
        print(f"\n{Fore.RED} An unexpected error occurred: {e}{Style.RESET_ALL}")

                # ----------------------------------
                # Delete the student data by name
                # ----------------------------------

def delete_student(students):
    try:
        if not students:
            print(f"\n{Fore.YELLOW} No student records found. {Style.RESET_ALL}")
            return
            display_students(students)

        while True:
            try:
                choice = int(input(f"\n Enter a student number to delete (1-{len(students)}): "))
                if 1 <= choice <= len(students):
                    deleted = students.pop(choice - 1)
                    print(f"   🗑️  {deleted['name']}  \n  Deleted successfully")
                    return
                else:
                    print(
                        f"{Fore.YELLOW} ⚠ Invalid input."
                        f" Please enter a number between 1-{len(students)} {Style.RESET_ALL}"
                        )
            except ValueError:
                print(f"{Fore.RED} ❌ Invalid input. ")
                print(f" Please enter a valid integer between 1-{len(students)} {Style.RESET_ALL}")

    except Exception:
        print(f"{Fore.RED} Error: Something wents wrong while deleting the student record.")

                # ---------------------------------------
                # Find the student who has highest score 
                # ---------------------------------------

def find_top_student(students):
    try:
        if not students:
            print(f"{Fore.YELLOW} Student record could not found. {Style.RESET_ALL}")
            return

        top_student = max(
            students,
            key=lambda student: student['score']
        )

        print(f"\n{Fore.MAGENTA}  🏆 Top student {Style.RESET_ALL}")
        print(f"   Name: {top_student['name']}")
        print(f"   City: {top_student['city']}")
        print(f"   Score: {top_student['score']}")

    except KeyError:
        print(f"{Fore.RED} Error: Invalid student data found.{Style.RESET_ALL}")
    except Exception:
        print(f"{Fore.RED} ❌ Could not calculate the top student.{Style.RESET_ALL}")


# ==============================================================================================================
#                                           Main program
# ==============================================================================================================

def main():

    students = load_students()

    try:
        while True:

            print("\n" + "=" * 45)
            print(f"{Fore.CYAN}     Bullet proof student record system.{Style.RESET_ALL}")
            print("=" * 45)

            print(f"\n{Fore.BLUE} 1. Add Students")
            print(" 2. Display Students")
            print(" 3. Search students")
            print(" 4. Find topper")
            print(" 5. Delete students")
            print(" 6. Save students")
            print(f" 7. Exit {Style.RESET_ALL} \n")

            try:
                choice = int(input("Choose a number to perform action between(1-7): "))
            except ValueError:
                print(f"\n{Fore.YELLOW} Invalid input.")
                print(f" Please enter a valid integer between (1-7){Style.RESET_ALL}")
                continue

            if choice == 1:
                add_student(students)

            elif choice == 2:
                display_students(students)

            elif choice == 3:
                search_student(students)

            elif choice == 4:
                find_top_student(students)

            elif choice == 5:
                delete_student(students)

            elif choice == 6:
                student_save(students)
            elif choice == 7:
                print(f"\n{Fore.GREEN}  💾 Saving students records..... {Style.RESET_ALL}")
                student_save(students)

                print("  👋 Exiting program...")
                break
            else:
                print(f"{Fore.YELLOW}Invalid choice. Please select between 1-7. {Style.RESET_ALL}")

    except KeyboardInterrupt:
        print(f"{Fore.RED} ❌ Program interrupted by the user. {Style.RESET_ALL}")
    except Exception:
        print(f"{Fore.RED} An un expected error occured. \n Program closed safely. {Style.RESET_ALL}")

    finally:
        print("\n" + "=" * 45)
        print(f"{Fore.CYAN} Thankyou for using student record system.")
        print(f"Goooooooood bye thak giaaaaaaa 😥 {Style.RESET_ALL}")
        print("=" * 45)


                # -------------------------------------------------
                #            Starting the program
                # -------------------------------------------------

if __name__ == "__main__":
    main()