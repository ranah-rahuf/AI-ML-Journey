#Exercise 1
class Car:
    pass

car1=Car()
car2=Car()
print(car1)

#Exercise 2:

class Student:
    def __init__(self, name, course, age):
        self.name = name
        self.course = course
        self.age = age

    def display_info(self):
        print(f"Name : {self.name}")
        print(f"Course : {self.course}")
        print(f"Age : {self.age}")

    def study(self):
        print(f"{self.name} is studying {self.course}")

    def change_course(self, new_course):
        self.course=new_course

     
student1 = Student( "Ranah", "CSD", 24)
student2 = Student("John", "CS", 26)

student1.display_info()
student2.display_info()

student1.study()
student2.study()

student1.change_course("AI/ML")
student1.display_info()

#Exercise 3 - Encapsulation

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount


    def withdraw(self, amount):
        if amount <= self.__balance :
            self.__balance -= amount
        else:
            print("Insufficient Balance")

    def get_balance(self):
        return self.__balance

account = BankAccount("Ranah", 1000)

account.deposit(500)
print(account.get_balance())

account.withdraw(300)
print(account.get_balance())

account.withdraw(2000)
print(account.get_balance())

#Exercise  4 - Inheritance

class Student:
    def __init__(self, name, course):
        self.name = name
        self.course = course

    def display_info(self):
        print(f"Name : {self.name}")
        print(f"Course : {self.course}")

class AIStudent(Student):
    def __init__(self, name, course, specialization):
        super().__init__(name, course)
        self.specialization = specialization

    def show_specialization(self):
        print(f"Specialization : {self.specialization}")
        

student = AIStudent("Ranah", "CSD", "AI/ML")
student.display_info()
student.show_specialization()

#Exercise 5 - Method overriding
class Student:
    def __init__(self, name):
        self.name = name
    def study(self):
        print(f"{self.name} is studying")


class AIStudent(Student):
   
    def study(self):
        print(f"{self.name} is studying AI/ML")

student = Student("Ranah")
ai_student = AIStudent("Ranah")

student.study()
ai_student.study()


