# JSON

#Writing JSON
import json 

student = {
    "id": 1,
    "name": "John Doe",
    "age": 20,
    "course": "Computer Science",
    "marks": 85
}

with open("student.json", "w") as file:
    json.dump(student, file, indent=4)

#Reading JSON

import json


with open("student.json", "r") as file:
    student = json.load(file)
print(student)
print(student["name"])