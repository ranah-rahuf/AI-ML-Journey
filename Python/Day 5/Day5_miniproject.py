# Student Record Manager
#Menu:1. Add Student
#      2. View Students
#      3. Exit

print("Student Record Manager")
print("Menu:")
print("1. Add Student")
print("2. View Students")
print("3. Exit")

choice = input("Enter your choice (1-3): ")
if choice == '1':
    name = input("Enter student name: ")
    students=open("students.txt", "a")
    students.write(name + "\n")
    students.close()
    print(f"Student {name} added successfully.")

elif choice == '2':
    students=open("students.txt", "r")
    print("List of Students:")
    for student in students:
        print(student.strip())
    students.close()
elif choice == '3':
    print("Exiting the program.")
    exit()
else:
    print("Invalid choice. Please select a valid option.")


# Mentor challenge : Password Checker

password=input("Enter password : ")
if len(password)<8:
    print("Weak password : Password must be at least 8 characters long.")
else:
    print("Strong password")
