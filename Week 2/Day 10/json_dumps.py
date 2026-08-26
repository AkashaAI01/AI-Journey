import json

person = {
    "name": "Ak",
    "class": 10,
    "score": 95,
    "grade": "A+",
    "course": ["AI", "Python"],
    "pass": True,
    "failed": None
}

Data = json.dumps(person)
print(f"\n {type(Data)}")
print(Data)
print("=" * 25 + "\n")


Structured_Data = json.dumps(person, indent=4)
print(Structured_Data)
print("=" * 25)
print("\n")

sorted_json = json.dumps(person, indent=4, sort_keys=True)
print("Sorted form of json")
print(sorted_json)