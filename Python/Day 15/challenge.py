marks = [45, 78, 92, 56, 88, 34, 67, 95, 73, 81]

total_students = len(marks)
average_marks = sum(marks) / total_students
highest_mark = max(marks)
lowest_mark = min(marks)

pass_marks = [mark for mark in marks if mark >= 60]
pass_students = len(pass_marks)
fail_marks=[mark for mark in marks if mark < 60]
fail_students = len(fail_marks)

pass_average = sum(pass_marks) / pass_students

print("Total students : ",total_students)
print("Average mark : ",average_marks)
print("Highest mark : ",highest_mark)
print("Lowest mark : ",lowest_mark)
print("Number of passing students : ",pass_students)
print("Number of failing students : ",fail_students)
print("Average of passing marks : " ,pass_average)
