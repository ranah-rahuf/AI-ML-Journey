with open("student.txt", "r") as student_file:
   for student in student_file:
       data=student.split(",")
       print(
           f"Student ID: {data[0]}\n"
           f"Name: {data[1]}\n"
           f"Age: {data[2]}\n"
           f"Course: {data[3]}\n"
           f"Grade: {data[4].strip()}\n"
        )