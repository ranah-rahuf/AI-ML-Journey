# Student data Validator
while True:
        print("1.Enter Student Details: ")
        print("2.Exit")

        try:
            choice = input("Enter your choice: ")
            if choice not in ["1", "2"]:
                print("Invalid choice! Please enter 1 or 2.")
                continue
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

        if choice == "2":
            break

        try:
            student_id = int(input("Enter student ID: "))
        except ValueError:
            print("Invalid input! Please enter a number for student ID.")
            continue
        
        if student_id <= 0:
            print("Invalid student ID! ID must be greater than 0.")
            continue   
        name = input("Enter student name: ")

        if not name.strip():
            print("Invalid name! Name cannot be empty.")
            continue

        try:
           age = int(input("Enter student age: "))
        except ValueError:
            print("Invalid age! Please enter a number.")
            continue
        
        if age <= 0:
            print("Invalid age! Age must be greater than 0.")
            continue
        

        course = input("Enter student course: ")

        if not course.strip():
            print("Invalid course! Course cannot be empty.")
            continue

        try:
            marks = int(input("Enter student marks: "))
        except ValueError:
            print("Invalid marks! Please enter a number.")
            continue
        
        if marks < 0 or marks > 100:
            print("Invalid marks! Marks must be between 0 and 100.")
            continue

        print(
            f"Student id : {student_id}\n " 
            f"name : {name}\n"
            f"age : {age}\n"
            f"course : {course}\n"
            f"marks : {marks}\n"
        )
            