def calculate_average(mark1, mark2, mark3):
    average = (mark1 + mark2 + mark3)/3
    return average

def is_pass(mark):
    if mark < 60:
        return "fail"
    else:
        return "pass"

def get_grade(mark):
    if mark >= 90 and mark <=100:
        return "A"
    elif mark >= 80 and mark <=89:
        return "B"
    elif mark >= 70 and mark <=79:
        return "C"
    elif mark >= 60 and mark <=69:
        return "D"
    else:
        return "F"
    