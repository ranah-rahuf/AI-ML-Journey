# Exercise 3 : Create a list containing 3 students ,sav ethme into students.json 
#Then read the file and display every student's information.

import json

students = [
    {
        "id": 1,
        "name": "John",
        "age": 20,
        "course": "Computer Science",
        "marks": 85
    },
    {
        "id": 2,
        "name": "Johny",
        "age": 22,
        "course": "Mathematics",
        "marks": 90
    },
    {
        "id": 3,
        "name": "Alice",
        "age": 21,
        "course": "Physics",
        "marks": 88
    }
]

with open("students.json", "w") as file:
    json.dump(students, file, indent=4)

with open("students.json", "r") as file:
    students = json.load(file)
for student in students:
    print(f"ID: {student['id']}")
    print(f"Name: {student['name']}")
    print(f"Age: {student['age']}")
    print(f"Course: {student['course']}")
    print(f"Marks: {student['marks']}")
    print()

#Exercise 4 : Search the list by student ID and display the matching student.

student_id = int(input("Enter student ID to search: "))

found = False
for student in students:
    if student["id"] == student_id:
        print(student)
        found = True
        break

if not found:
    print("Student not found.")


# Exercise 5 : Update JSON by student ID and save the updated list back to the file.
student_id = int(input("Enter student ID to update: "))

found = False
for student in students:
    if student["id"] == student_id:
        student["name"] = input("Enter new name: ")
        student["age"] = int(input("Enter new age: "))
        student["course"] = input("Enter new course: ")
        student["marks"] = int(input("Enter new marks: "))
        found = True
        break

if found:
    with open("students.json", "w") as file:
        json.dump(students, file, indent=4)
    print(students)
else:
    print("Student not found.")

# Exercise 6 : Try opening a JSON file that doesn't exist.Then create an invalid JSON file and try reading it.


try:
    with open("nonexistent.json", "r") as file:
        data = json.load(file)
except FileNotFoundError:
    print("File not found.")


try:
    with open("invalid.json", "r") as file:
        data = json.load(file)
except json.JSONDecodeError:
    print("Invalid JSON format.")

# Exercise 7 :Calculate Number of students,Average marks,Highest marks and Lowest marks

number_of_students = len(students)

total_marks = sum(student["marks"] for student in students)
average_marks = total_marks / number_of_students
Highest_marks = max(student["marks"] for student in students)
Lowest_marks = min(student["marks"] for student in students)

print("Total students:", number_of_students)
print("Average marks:", average_marks)
print("Highest marks:", Highest_marks)
print("Lowest marks:", Lowest_marks)