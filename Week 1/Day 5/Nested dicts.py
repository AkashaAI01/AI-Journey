# creating a neted dictionary
person = {
    "name": "Akasha",
    "grades": {
        "Math": 78,
        "ENG": 90,
        "PAk": 48
    }
}

# Accessing nested value
print(person["grades"]["Math"])

#message
messages = [
    {"role": "user",    "content": "Hello!"},
    {"role": "assistent",    "content": "Hi! how can I help you"},
    {"role": "user",    "content": "What is python?"},
]

for message in messages:
    print(f"{message['role']}: {message['content']}")