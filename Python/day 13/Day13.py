#Class and objeccts:

#Exercise 1
class Car:
    pass

car1=Car()
car2=Car()
print(car1)

#Attributes:

class Car:
    pass

car1 = Car()
car2 = Car()

car1.brand = "Toyota"
car1.model = "Camry"

car2.brand = "BMW"
car2.model = "M3"

print(car1.brand)
print(car1.model)

print(car2.brand)
print(car2.model)

#methods:
class Student:
    def __init__(self, name, course, age):
        self.name = name
        self.course = course
        self.age = age

    def introduce(self):
        print("Hello, my name is", self.name)

student1=Student("Tara", "CS", 23)
student1.introduce()

#Class variable and Instance Variable:
class Student:
    college = "ABC College"  #class variable

    def __init__(self, name):
        self.name = name     #Instance variable 


student1 = Student("Ranah")
student2 = Student("John")

student1.college = "XYZ College"
print(student1.name)
print(student2.name)

print(student1.college)
print(student2.college)
print(Student.college)

#Encapsulation:
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance


account = BankAccount("Ranah", 1000)

account.deposit(500)

print(account.get_balance())

#Inheritance
class Student:
    def study(self):
        print("Student is studying")


class CSStudent(Student):
    pass

student = CSStudent()
student.study()

#Method Overriding
class Student:
    def study(self):
        print("Student is studying")


class AIStudent(Student):
    def study(self):
        print("AI Student is studying Machine Learning")

student = AIStudent()
student.study()

#Polymorphism
class Student:
    def study(self):
        print("Student is studying")


class AIStudent(Student):
    def study(self):
        print("AI Student is studying AI/ML")


class CSStudent(Student):
    def study(self):
        print("CS Student is studying programming")

students = [
    Student(),
    AIStudent(),
    CSStudent()
]

for student in students:
    student.study()
