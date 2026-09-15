class Student:
    def __init__(self, name, course, mark):
        self.name = name
        self.course = course
        self.__mark = mark

    def display_info(self):
        print(f"Name : {self.name}")
        print(f"course : {self.course}")

    def get_marks(self):
        return self.__mark

    def get_grade(self):
        if self.__mark >= 90:
            return "A"
        elif self.__mark >= 80:
            return "B"
        elif self.__mark >= 70:
            return "C"
        elif self.__mark >= 60:
            return "D"
        else:
            return "F"

    def study(self):
        print("Student is studying")

class AIStudent(Student):
    def __init__(self, name, course, mark, specialization):
        super().__init__(name, course, mark)
        self.specialization = specialization

    def show_specialization(self):
        print(f"Specialization : {self.specialization}")

    def study(self):
        print("AI Student is studying AI/ML")

class CSStudent(Student):
    def __init__(self, name, course, mark, specialization):
        super().__init__(name, course, mark)
        self.specialization = specialization

    def show_specialization(self):
        print(f"Specialization : {self.specialization}")

    def study(self):
        print("CS Student is studying programming")

student1 = Student("Rahul", "CSD", 75)
student2 = AIStudent("Ranah", "CSD", 90, "AI/ML")
student3 = CSStudent("John", "CS", 85, "Software Development")

student1.display_info()
print(f"Marks : {student1.get_marks()}")
print(f"Grade : {student1.get_grade()}")
student2.display_info()
student2.show_specialization()
print(f"Marks : {student2.get_marks()}")
print(f"Grade : {student2.get_grade()}")
student3.display_info()
student3.show_specialization()
print(f"Marks : {student3.get_marks()}")
print(f"Grade : {student3.get_grade()}")

students = [
    student1,
    student2,
    student3
 ]

for student in students:
    student.study()