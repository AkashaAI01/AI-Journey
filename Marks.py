Name = input("Enter your name: ")
Marks = int(input("Enter your marks: "))

if Marks >= 90:
    grade = "A"
elif Marks >= 80:
    grade = "B"
elif Marks >= 70:
    grade = "C"
else:
    grade = "Fail!"

print(Name, "Your grade is:", grade)