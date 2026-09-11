#Student Grade Processor

def student_report(*marks, **student):

    average = sum(marks) / len(marks)

    student["average"] = average

    if average >= 90 :
        student["grade"] = "A"
    elif average >= 80 :
        student["grade"] = "B"
    elif average >= 70 :
        student["grade"] = "C" 
    elif average >= 60 :
        student["grade"] = "D"
    else :
        student["grade"] = "F"

    return student


result = student_report(
    85, 90, 78, 92,
    name="Ranah",
    course="CSD"
)

print(result)