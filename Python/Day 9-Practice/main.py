import calculator

print(calculator.add(5, 3))  # Output: 8
print(calculator.subtract(5, 3))  # Output: 2
print(calculator.multiply(5, 3))  # Output: 15
print(calculator.divide(5, 3))  # Output: 1.6666666666666667
print(calculator.square(5))  # Output: 25

#Import specific functions only
from calculator import add, multiply, square
print(add(10, 5))
print(multiply(10, 5))
print(square(10))

#give a module a shorter name:
import calculator as calc
print(calc.add(5, 3))  # Output: 8
print(calc.subtract(5, 3))  # Output: 2
print(calc.multiply(5, 3))  # Output: 15
print(calc.divide(5, 3))  # Output: 1.6666666666666667
print(calc.square(5)) 

import greetings
print(greetings.greet("Ranah"))

#combine modules:

import student_util
import calculator

name=input("Enter your name : ")

mark1=int(input("Enter mark1 : "))
mark2=int(input("Enter mark2 : "))
mark3=int(input("Enter mark3 : "))

print(f"Student : {name}")

print(f"Marks : {mark1}, {mark2}, {mark3}")

print(f"Average : {student_util.calculate_average(mark1, mark2, mark3 )}")

print(f"Grade : {student_util.get_grade(mark1)}")

print(f"5 + 3 = {calculator.add(5, 3)}")
print(f"5 x 3 = {calculator.multiply(5, 3)}")



