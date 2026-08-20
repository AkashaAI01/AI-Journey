# scope __ veriables inside stay inside
def calculate():
    result = 100
    return result

print(calculate())

# add grades 
def get_grade(score):
    """
    Take a score (0-100) and returns the letter grade.
    A=90+, B=80+, C=70+, D=60+, F=below then 60
    """
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

print(get_grade(78))
print(get_grade(80))
print(get_grade(34))