Numbers = [10, 20, 30, 40,50]

# Slicing: list[Start : Stop]
print(Numbers[1:4])
print(Numbers[:3])
print(Numbers[2:])

# list comprehension build a new list
scores = [23, 34, 78, 87, 56, 90]

# Get only passing scores (>= 50)
passing = [s for s in scores if s >= 50]
print(sorted(passing))

# Double the value
doubled = [s * 2 for s in scores]
print(doubled)