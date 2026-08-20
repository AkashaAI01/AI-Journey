person = {
    "name": "Akasha",
    "age": 19,
    "city": "Lahore",
}

# looping through keys only
for key in person.keys():
    print(key)

# looping through values only
for value in person.values():
    print(value)

# looping through both keys and values
for key, value in person.items():
    print(f"{key}: {value}")

# using enumerate 
for index, (key, value) in enumerate(person.items()):
    index += 1
    print(f"{index}. {key}= {value}")