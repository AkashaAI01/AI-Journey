import json

Ask_API = '{"name": "Akasha", "age": 19, "city": "Lahore", "skills": ["Python", "AI"]}'

print(type(Ask_API))

person = json.loads(Ask_API)

print(type(person))
print(person ["name"])
print(person ["age"])
print(person ["city"])
print(person["skills"][0])
print(person["skills"][1])

for key, value in person.items():
    print(f"{key}: {value}") 