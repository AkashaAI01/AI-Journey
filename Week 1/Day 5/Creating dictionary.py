#Creating a dictionary
person = {
    "name": "Akasha",
    "age": 25,
    "city": "Lahore",
    "is_student": True
}

#Assessing by key
print(person["name"])
print(person["age"])

# Safe access with get
print(person.get("email"))
print(person.get("email", "Not found"))
