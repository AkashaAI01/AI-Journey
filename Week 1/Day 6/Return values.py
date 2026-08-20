# creating a function
def add(x, y):
    result = x + y
    return result

total = add(4, 9)
print(total)
print(add(5, 13))

# Default parameters
def greet(name="friend"):
    return f"Hello! {name}"
print(greet("Akasha"))
print(greet())

# returning a dictionary 
def get_student(name, grade):
    return {"name": name, "grade": grade}

student = get_student("Akasha", "A")
print(student["name"])