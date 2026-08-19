#Student management system

class Student:
    """Represents a student in the management system."""

    def __init__(self, student_id, name, age, course, marks):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.course = course
        self.marks = marks

    def display_info(self):
        print(f"Student ID: {self.student_id}, Name: {self.name}, Age: {self.age}, Course: {self.course}, Marks: {self.marks}")

class StudentManagementSystem:
    """Manages a collection of students."""

    def __init__(self):
        self.students = {}

    def add_student(self):
        """Add a new student after validating the input."""

        try:
            student_id = int(input("Enter student ID: "))
        except ValueError:
            print("Invalid input! Please enter a number for student ID.")
            return
        
        if student_id <= 0:
            print("Invalid student ID! ID must be greater than 0.")
            return
        
        if student_id in self.students:
            print("Student ID already exists!")
            return
        
        
        name = input("Enter student name: ")

        if not name.strip():
            print("Invalid name! Name cannot be empty.")
            return
        

        try:
           age = int(input("Enter student age: "))
        except ValueError:
            print("Invalid age! Please enter a number.")
            return
        
        if age <= 0:
            print("Invalid age! Age must be greater than 0.")
            return
        

        course = input("Enter student course: ")

        if not course.strip():
            print("Invalid course! Course cannot be empty.")
            return
        

        try:
            marks = int(input("Enter student marks: "))
        except ValueError:
            print("Invalid marks! Please enter a number.")
            return
        
        if marks < 0 or marks > 100:
            print("Invalid marks! Marks must be between 0 and 100.")
            return

        student = Student(student_id, name, age, course, marks)

        self.students[student_id] = student

        print("Student added successfully!")

    def view_students(self):
        """Display information for all students."""

        if not self.students:
            print("No students found.")
            return
        
        for student in self.students.values():
            student.display_info()


    def search_student(self):
        """Search for a student by ID."""

        try:
            student_id = int(input("Enter student ID to search: "))
        except ValueError:
            print("Invalid input! Please enter a number for student ID.")
            return
        
        if student_id <= 0:
            print("Invalid student ID! ID must be greater than 0.")
            return
        
        if student_id in self.students:
            print("Student found!")  
            self.students[student_id].display_info()
        else:
            print("Student not found.")  

    def update_student(self):
        """Update information for an existing student."""

        try:
            student_id = int(input("Enter student ID to update: "))
        except ValueError:
            print("Invalid input! Please enter a number for student ID.")
            return
        
        if student_id <= 0:
            print("Invalid student ID! ID must be greater than 0.")
            return
        
        if student_id not in self.students:
            print("Student not found.")
        else:
            print("1. Update Name")
            print("2. Update Age")
            print("3. Update Course")
            print("4. Update Marks")
            print("5. Cancel")

            try:
                choice = int(input("Enter your choice: "))
            except ValueError:
                print("Please enter a number.")
                return
            
            if choice <= 0 or choice > 5:
                print("Invalid choice!")
                return

            if choice == 1:

                new_name = input("Enter new name: ")

                if not new_name.strip():
                    print("Invalid name! Name cannot be empty.")
                    return
                
                self.students[student_id].name = new_name
                print("Name updated successfully.")

            elif choice == 2:
                try:
                    new_age = int(input("Enter new age: "))
                except ValueError:
                    print("Invalid input! Please enter a number for age.")
                    return
                
                if new_age <= 0:
                    print("Invalid age! Age must be greater than 0.")
                    return
                
                self.students[student_id].age = new_age
                print("Age updated successfully.")

            elif choice == 3:

                new_course = input("Enter new course: ")

                if not new_course.strip():
                    print("Invalid course! Course cannot be empty.")
                    return
                
                self.students[student_id].course = new_course
                print("Course updated successfully.")

            elif choice == 4:
                try:
                    new_mark = int(input("Enter new mark: "))
                except ValueError:
                    print("Invalid input! Please enter a number for marks.")
                    return
                
                if new_mark < 0 or new_mark > 100:
                    print("Invalid marks! Marks must be between 0 and 100.")
                    return
                
                self.students[student_id].marks = new_mark
                print("Marks updated successfully.")

            elif choice == 5:

                print("Update cancelled.")


    def delete_student(self):
        """Delete a student by ID after confirmation."""

        try:
            student_id = int(input("Enter student ID to delete: "))
        except ValueError:
            print("Invalid input! Please enter a number for student ID.")
            return
        
        if student_id <= 0:
            print("Invalid student ID! ID must be greater than 0.")
            return
        
        if student_id not in self.students:
            print("Student not found.")
            return
        
        confirmation=input(
            "Are you sure you want to delete this student? (yes/no): "
            ).strip().lower()
        
        if confirmation == "yes":
            del self.students[student_id]
            print("Student deleted successfully.")
        elif confirmation == "no":
            print("Delete operation cancelled.")
        else:
            print("Invalid choice! Please enter 'yes' or 'no'.")


   
system=StudentManagementSystem()

while True:
    print("\nStudent Management System")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a number.")
        continue

    if choice == 1:
        system.add_student()
    elif choice == 2:
        system.view_students()
    elif choice == 3:
        system.search_student()
    elif choice == 4:
        system.update_student()
    elif choice == 5:
        system.delete_student()
    elif choice == 6:
        break
    else:
        print("Invalid choice! Please try again.")


