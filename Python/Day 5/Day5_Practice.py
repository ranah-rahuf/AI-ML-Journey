# 1. Ask the user for a number.If they enter text,print 'Invalid input' instead of crashing.

try:
    number = int(input("Enter a number : "))
except ValueError:
    print("Invalid input")

# 2. Divide 2 no. handle division by zero and invalid input.

try:
    num1 = int(input("Enter first number : "))
    num2 = int(input("Enter second number : "))
    result = num1 / num2
    print(result)
except ValueError:
    print("Invalid input")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

# 3. create a text file called students.txt read file and print every name .

students_file = open("students.txt", "r")
print(students_file.readlines())
students_file.close()

#better solution
students_file = open("students.txt", "r")
for student in students_file.readlines():
    print(student)
students_file.close()

#Even better solution
students_file = open("students.txt", "r")
for student in students_file:
    print(student)
students_file.close()

# 4. Ask the user for a new student name.Append it to the file.
students_file = open("students.txt", "a")
students_file.write("\n" + input("Enter new student name : "))
students_file.close()

# 5. Read the file and count how many students are inside.

students_file = open("students.txt", "r")
students = students_file.readlines()
print(f"Number of students: {len(students)}")
students_file.close()