score = 0
# Question 1
Q1 = input("What is the capital of Pakistan? ")
if Q1.lower() == "islamabad":
    print("Correct!")
    score += 1
else:
    print("Incorrect. The correct anwer is Islamabad.")

#Question 2
Q2 = input("Who is the founder of Pakistan?")
if Q2.lower() == "muhammad ali jinnah":
    print("Correct!")
    score += 1
else:
    print("Incorrect. The correct answer is Muhammad Ali Jinnah.")

#Question 3
Q3 = input("What is the national language of Pakistan? ")
if Q3.lower() == "urdu":
    print("Correct!")
    score += 1
else:
    print("Incorrect. The correct answer is Urdu.")

print(f"Your final score is: {score}/3")
if score == 3:
    print("Excellent!")
elif score == 2:
    print("Good effort! You can do better.")
elif score == 1:
    print("You need to improve.")
else:
    print("Too bad! You need to workhard.")
