import random
from datetime import datetime

# Create list of questions:
questions = [
    {
        "question": "Who see the dream of Pakistan? ",
        "hint": "National poet.",
        "answer": "Allama Iqbal"
    },
    {
        "question": "What is our national game? ",
        "hint": "Commonly use in fights",
        "answer": "Hockey"
    },
    {
        "question": "When we celebrate the independence day? only tell me the day... ",
        "hint": "Azadi",
        "answer": "14"
    },
    {
        "question": "What is name of highest mountain in Pakistan? ",
        "hint": "Ends with digit",
        "answer": "k2"
    },
    {
        "question": "What is the capital of Pakistan? ",
        "hint": "Faisal masjid",
        "answer": "Islamabad"
    }
]

# Ask any Question from the user 
def ask_question(q):
    attempt = 0
    max_attempt = 3
    while max_attempt > attempt:
        user_answer = input(f"\n{q['question']} ").title()
        if user_answer == q["answer"].title():
            print("Correct!")
            return True
        else:
            attempt += 1
            remaining = max_attempt - attempt
            if remaining > 0:
                print(
                    f"Not quite. Try again! \n"
                    f"Hint: {q['hint']} \n"
                    f"You have {remaining} attempts left.\n"
                )
            else:
                print(
                    f"Your all attempts are failed. \n"
                    f"The correct answer is {q['answer']}. \n"
                )

    return False

# Calculate percentage and grade 
def get_grade(score, total):
    percentage = (score / total) * 100
    if percentage >= 90:
        grade = "A"
    elif percentage >= 80:
        grade = "B"
    elif percentage >= 70:
        grade = "C"
    elif percentage >= 60:
        grade = "D"
    else:
        grade = "F"

    return percentage, grade

# Save the quize result into the file 
def save_result(name, score, percentage, grade):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M")

    with open("quiz_result.txt", "a") as file:
        file.write(
            f"Date: {current_time} |"
            f"Name: {name} |"
            f"Score: {score}/5 |"
            f"Percentage: {percentage:.1f}% |"
            f"Grade: {grade} \n"
        )
    print("\n Your result has been added successfully! \n")

# Show previous quiz results 
def show_results():
    try:
        with open ("quiz_result.txt", "r") as file:
            results = file.read()
            print(
                f"\n========== Quiz Results =========="
                f"\n {results} \n"
                f"================================\n"
            )
    except FileNotFoundError:
        print("\n Record doesn't found.")

# Now its a time to run the quiz 
def run_quiz():
    # Ask user to inpur thier name
    name = input("\n Enter your name: ").strip().title()

    random.shuffle(questions)

    score = 0

    print(f"\n ===== Welcome {name} to quiz! =====")
    print(f"You will attempt {len(questions)} questions. 3 chance for each.\n")

    for q in questions:
        correct = ask_question(q)
        if correct:
            score +=1

    # calculate the result:
    percentage, grade = get_grade(score, len(questions))

    print("\n === Quiz completed! === \n")
    print(f"Name: {name}")
    print(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print(f"Score: {score}/5")
    print(f"Percentage: {percentage:.1f}")
    print(f"Grade: {grade}")

    # Save result
    save_result(name, score, percentage, grade)
    choice = input("Do you want to see the result? Yes/No \n").lower()
    if choice == "yes":
        show_results()
    else:
        print("Ok. Thanks for your participation. \n")
        print("See you next time. Good bye \n")

if __name__ == "__main__":
    run_quiz()