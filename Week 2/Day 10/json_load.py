import json

with open("record.json", "r") as f:
    students = json.load(f)

print(f"\n {type(students)}")
print(f"\n <<< {len(students)} >>> \n")

for student in students:
    print(f"{student['name']}: {student['grade']} ({student['score']})")