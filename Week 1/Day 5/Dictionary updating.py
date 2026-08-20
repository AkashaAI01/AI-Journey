#Creating a dictionary
person = {
    "name": "Akasha",
    "age": 25,
}
print(person)

#Add new keys to dictionary
person["city"] = "Lahore"
person["email"] = "akasha@example.com"
print(person)

#update existing keys
person["name"] = "Abdullah"
print(person)

#Del existing key
del person["email"]
print(person)

#check number of keys in a set
print(len(person))
print(list(person.keys()))

#check number of values in a set
print(list(person.values()))

#check if key exists
if "city" in person:
    print(f"{person['name']} is from {person['city']}")
