import json

Students = [
    {"name": "Ali", "grade": "B", "score": 87},
    {"name": "Akasha", "grade": "A", "score": 93},
    {"name": "Ahmad", "grade": "F", "score": 49}
]

with open ("record.json", "w") as f:
    json.dump(Students, f, indent=4)

print("Record.json file saved saved successfully!")