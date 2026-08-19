# Grading System
def grade(marks):
    if  90 <= marks <= 100:
        return "A"
    elif 80 <= marks:
        return "B"
    elif 70 <= marks:
        return "C"
    elif 60 <= marks:
        return "D"
    else:
        return "F"
    