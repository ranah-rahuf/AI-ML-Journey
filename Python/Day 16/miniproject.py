students = [
    {"name": "Ranah", "marks": [85, 90, 78, 92]},
    {"name": "John", "marks": [65, 72, 68, 75]},
    {"name": "Anu", "marks": [95, 88, 91, 97]},
    {"name": "Rahul", "marks": [45, 55, 60, 50]}
]

def analyze_student(student):
    print("Name :",student["name"])
    average_mark = sum(student["marks"]) / len(student["marks"])
    print("Average mark : ",average_mark)
    print("Highest mark : ",max(student["marks"]))
    print("Lowest mark : ",min(student["marks"]))
    if average_mark >= 90:
        print("Grade : A")
    elif average_mark >= 80:
        print("Grade : B")
    elif average_mark >= 70:
        print("Grade : C")
    elif average_mark >= 60:
        print("Grade : D")
    else :
        print("Grade : F")
    
    
for student in students:

    analyze_student(student)
    
    print("------------------")
