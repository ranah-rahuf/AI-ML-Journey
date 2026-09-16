#Task 1 — Working with Numerical Data

marks = [78, 85, 92, 67, 88, 74, 95, 81] 
 
print(f"Total : {sum(marks)}")

average_mark = sum(marks) / len(marks)
print(f"Average : {average_mark}")

highest_mark = max(marks)
print(f"Highest mark : {highest_mark}")

lowest_mark = min(marks)
print(f"Lowest mark : {lowest_mark}")

number_of_students = len(marks)
print(f"Number of students : {number_of_students}")


#Task 2: List Comprehension

marks = [78, 85, 92, 67, 88, 74, 95, 81]

new_list = [mark for mark in marks if mark >= 80 ]
print(new_list)

#Task 3: Transform the Data

marks = [78, 85, 92, 67, 88, 74, 95, 81]

new_list = [mark + 5 for mark in marks if mark >= 80 ]
print(new_list)

#Task 4: Dictionary Data

student = {
    "name": "Ranah",
    "course": "CSD",
    "marks": [85, 90, 78, 92]
}

print(f"Name : {student["name"]}")

average_mark = sum(student["marks"]) / len(student["marks"])
print(f"Average : {average_mark}")

highest_mark = max(student["marks"])
print(f"Highest : {highest_mark}")

#Task 5: Data Processing Function

def analyze_marks(marks):
    total = sum(marks)
    average = total / len(marks)
    highest = max(marks)
    lowest  = min(marks)
   

    return {"total" : total,
            "average" : average,
            "highest" : highest,
            "lowest" : lowest
            }


marks = [85, 90, 78, 92]

print(analyze_marks(marks))

#Task 6: ML-Style Data Processing

marks = [45, 78, 92, 56, 88, 34, 67, 95, 73, 81]

pass_marks = [mark for mark in marks if mark >= 60]
students = len(pass_marks)
average = sum(pass_marks) / students

print("Passing Marks : ",pass_marks)
print("Number of Passing Students : ",students)
print("Average Passing Mark : ",average)