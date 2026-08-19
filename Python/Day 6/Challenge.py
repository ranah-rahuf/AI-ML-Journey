class Teacher:
    def __init__(self ,name ,subject ):
        self.name=name
        self.subject=subject
    def teach(self):
        print(f"{self.name} is teaching {self.subject}")

teacher1=Teacher("Rahul","Mathematics")
teacher1.teach()

# 2. 
class Vehicle:
    def move(self):
        print("Vehicle is moving")

class Car(Vehicle):
    def stop(self):
        print("stop")
    def move(self):
        print("Car is moving on the road")
class Bike(Vehicle):
    def ring_bell(self):
        print("Ring Ring!")
car1=Car()
bike1=Bike()
car1.move()
bike1.move()


