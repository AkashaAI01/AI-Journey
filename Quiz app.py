import random

# Create a list of 5 questions
questions = [
    {
        "question": "What is the capital of Pakistan?",
        "answer": "islamabad",
        "hint": "Faisal Masjid"
    },
    {
        "question": "When we celebrate our Independence Day? only tell me the date...",
        "answer": "14",
        "hint": "Azadi"
    },
    {
        "question": "Who see the dream of Pakistan?",
        "answer": "allama iqbal",
        "hint": "National poet"
    },
    {
        "question": "What is the Pakistan's national game?",
        "answer": "hockey",
        "hint": "mostly marny ka lia use hota in fights"
    },
    {
        "question": "Biggest mountain in pakistan?",
        "answer": "k2",
        "hint": "ending whith digit...."
    }
]

def ask_question(q):
    attempt = 0
    max_attempt = 3

    while max_attempt > attempt:
        user_answer = input(f"\n{q['question']} ").lower()
        if user_answer == q["answer"].lower():
            print("Correct!")
            return True
        else:
            attempt += 1
            remaining = max_attempt - attempt
            if remaining > 0:
                print(f"Not quit. Try again Hint: {q['hint']}. You have Remaining {remaining} attempt(s) left.")
            else:
                print(f"Your all attempts are fail! the correct answer is {q['answer']}.")
    return False

# Create a grade book
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

def run_quiz():
    random.shuffle(questions)

    score = 0

    print("=== Welcome to the quiz. ===")
    print(f"You'll answer {len(questions)} questions. 3 chances for each.\n")

    for q in questions:
        correct = ask_question(q)
        if correct:
            score +=1

# Show the final results 
    percentage, grade = get_grade(score, len(questions))
    print("\n === Quiz completed! ===")
    print(f"score: {score}/{len(questions)}")
    print(f"percentage: {percentage: .1f}:")
    print(f"Grade: {grade}")

if __name__ == "__main__":
    run_quiz()