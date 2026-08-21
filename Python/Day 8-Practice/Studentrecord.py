def student_exists(student_id):
    try:
        with open("student.txt", "r") as student_file:
            for student in student_file:
                data = student.strip()
                if not data:
                    continue  # Skip empty lines

                data = data.split(",")
                if student_id == int(data[0]):
                    return True
                
    except FileNotFoundError:
        return False
    
    return False
   
def add_student():
    try:
        student_id = int(input("Enter Student ID: "))
    except ValueError:
        print("Invalid input! Please enter a number.")
        return

    if student_id <= 0:
        print("Invalid Student ID! ID must be greater than 0.")
        return

    if student_exists(student_id):
        print("Student ID already exists!")
        return

    
    name = input("Enter Student Name: ").strip()
    if not name:
        print("Invalid name! Name cannot be empty.")
        return

    try:
        age = int(input("Enter Student Age: "))
    except ValueError:
        print("Invalid age! Please enter a number.")
        return

    if age <= 0:
        print("Invalid age! Age must be greater than 0.")
        return

    
    course = input("Enter Course name: ").strip()

    if not course:
        print("Invalid course! Course cannot be empty.")
        return

    try:
        mark = float(input("Enter Student Mark: "))
    except ValueError:
        print("Invalid mark! Please enter a number.")
        return

    if mark < 0 or mark > 100:
        print("Invalid mark! Mark must be between 0 and 100.")
        return

    with open("student.txt", "a") as student_file:
        student_file.write(f"{student_id},{name},{age},{course},{mark}\n")
        print("Student added successfully!")

def view_students():
    with open("student.txt", "r") as student_file:
        for student in student_file:
            print(student.strip())

def search_student():
    try:
        search_id = int(input("Enter Student ID to search: "))
    except ValueError:
        print("Invalid input! Please enter a number.")
        return

    if search_id <= 0:
        print("Invalid Student ID! ID must be greater than 0.")
        return

    found = False

    with open("student.txt", "r") as student_file:
        for student in student_file:
            
            data = student.strip()
            if not data:
                continue  # Skip empty lines

            data=data.split(",")

            if search_id == int(data[0]):
                print("Student Found!")
                print(f"Student ID: {data[0]}")
                print(f"Name: {data[1]}")
                print(f"Age: {data[2]}")
                print(f"Course: {data[3]}")
                print(f"Mark: {data[4]}")

                found = True
                break

    if not found:
        print("Student not found.")
            
            
while True:
    print("1. Add Student")
    print("2. View Student")
    print("3. Search Student")
    print("4.Exit")

    try:
        choice = int(input("Enter Your Choice:"))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    if choice == 1:
        add_student()
    elif choice == 2:
        view_students()
    elif choice == 3:
        search_student()
    elif choice == 4:
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")