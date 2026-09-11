#student JSON record manager 

import json

def display_student(student):
    print(f"ID: {student['id']}")
    print(f"Name: {student['name']}")
    print(f"Age: {student['age']}")
    print(f"Course: {student['course']}")
    print(f"Marks: {student['marks']}")
    print()

def add_student(students):
    student = {}
    try:
        student["id"] = int(input("Enter Student ID : "))
        if  any(s["id"] == student["id"] for s in students):
            print("Student ID already exists. Please enter a unique ID.")
            return None
    except ValueError:
        print("Invalid input for Student ID.")
        return None

    student["name"] = input("Enter student name : ")

    if student["name"].strip() == "":
        print("Student name cannot be empty.")
        return None
    try:
        student["age"] = int(input("Enter age : "))
        if student["age"] <= 0:
            print("Age must be a positive integer.")
            return None
    except ValueError:
        print("Invalid input for age. Please enter a valid integer.")
        return None

    student["course"] = input("Enter course : ")

    if student["course"].strip() == "":
        print("Course name cannot be empty.")
        return None

    try:
        student["marks"] = float(input("Enter marks :"))
        if student["marks"] < 0 or student["marks"] > 100:
            print("Marks must be between 0 and 100.")
            return None
    except ValueError:
        print("Invalid input for marks. Please enter a valid number.")
        return None

    return student
   
def view_students(students):

    for student in students:
        display_student(student)
    if not students:
        print("No students found.")

def search_student(students, student_id):
    found = False
    for student in students:
        if student["id"] == student_id:
            display_student(student)

            found = True
            break
    if not found:
        print("Student not found.")

def update_student(students, student_id):
    found = False
    for student in students:
        if student["id"] == student_id:

            new_name = input("Enter new name : ")
            if new_name.strip() == "":
                print("Student name cannot be empty.")
                return

            try:
                new_age = int(input("Enter new age : "))
                if new_age <= 0:
                    print("Age must be a positive integer.")
                    return
            except ValueError:
                print("Invalid input for age. Please enter a valid integer.")
                return
    

            new_course = input("Enter course : ")
            if new_course.strip() == "":
                print("Course name cannot be empty.")
                return
            
            try:
                new_marks = float(input("Enter marks :"))
                if new_marks < 0 or new_marks > 100:
                    print("Marks must be between 0 and 100.")
                    return
                
            except ValueError:
                print("Invalid input for marks. Please enter a valid number.")
                return
            
            student["name"] = new_name
            student["age"] = new_age
            student["course"] = new_course
            student["marks"] = new_marks
            
            found = True
            break
        
    if found:
        with open("students.json","w") as file:
            json.dump(students ,file ,indent=4 )
        print("Student details updated successfully .")
    else:
        print("Student not found.")

def delete_student(students, student_id):

    found = False


    for student in students:
        if student["id"] == student_id:
            students.remove(student)
        
            found = True
            break
    if found :
        with open("students.json","w") as file:
            json.dump(students ,file ,indent=4 )
        print("Student deleted successfully .")

    else:
        print("Student not found.")


try:
    with open("students.json", "r") as file:
        students = json.load(file)
except FileNotFoundError:
    students = []
    print("No existing student records found. Starting fresh.")
except json.JSONDecodeError:
    students = []
    print("Invalid JSON data. Starting with an empty student list.")


while True:
    print("===== Student JSON Record Manager =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    try:
        choice = int(input("Enter your choice : "))
        if choice < 1 or choice > 6:
            raise ValueError("Invalid choice. Please enter a number between 1 and 6.")
    except ValueError as e:
        print(e)
        continue

    if choice == 1:
        student = add_student(students)

        if student is not None:
            students.append(student)

            with open("students.json", "w") as file:
               json.dump(students, file, indent=4)

            print("Student added successfully!")
    

    elif choice == 2:
        view_students(students)


    elif choice == 3:
        try:
            student_id = int(input("Enter student ID to search: "))
            search_student(students, student_id)
        except ValueError:
            print("Invalid input. Please enter a valid student ID.")

    elif choice == 4:
        try:
            student_id = int(input("Enter student ID to update: "))
            update_student(students, student_id)
        except ValueError:
            print("Invalid input . Please enter a valid student ID .")
            

    elif choice == 5:
        try:
            student_id = int(input("Enter student ID to delete: "))
            delete_student(students, student_id)
        except ValueError:
            print("Invalid input . Please enter a valid student ID .")

    elif choice == 6:
        print("Exiting the program. Goodbye!")
        break

    

