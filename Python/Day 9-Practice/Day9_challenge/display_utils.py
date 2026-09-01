import student_utils

def display_student(name ,marks ):
    print(f"Student = {name}")
    print(f"Marks = {marks}")

    average_mark = student_utils.calculate_average(marks)
    print(f"Average = {average_mark}")
    print(f"Grade = {student_utils.get_grade(average_mark)}")
    print(f"Status = {student_utils.get_status(average_mark)}")
     