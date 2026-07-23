# Try / Except

try:
    number=int(input("Enter a number :"))
    print(number)
except:
    print("Invalid Input!")

try:
    number=int(input("Enter a number :"))
    print(number)
except ValueError:
    print("Invalid input")


try:
    number=int(input("Enter a number :"))
    print(number)
except ValueError as err:
    print(err)


try:
    result=10/0
except ZeroDivisionError:
    print("divided by zero")


try:
    result=10/0
except ZeroDivisionError as err:
    print(err)

# Reading Files

employee_file=open("employees.txt","r")

print(employee_file.readable())

employee_file.close()


employee_file=open("employees.txt","r")

print(employee_file.read())

employee_file.close()


employee_file=open("employees.txt","r")

print(employee_file.readline())

employee_file.close()



employee_file=open("employees.txt","r")

print(employee_file.readline())
print(employee_file.readline())

employee_file.close()


employee_file=open("employees.txt","r")

print(employee_file.readlines())

employee_file.close()



employee_file=open("employees.txt","r")

print(employee_file.readlines()[3])

employee_file.close()

employee_file=open("employees.txt","r")

for employee in employee_file.readlines():
    print(employee)

employee_file.close()

# Writing to files:

# 1. Adding element

employee_file=open("employees.txt","a")

employee_file.write("\nToby=HR")

employee_file.close()

# 2.Overriding the content in employees.txt

employee_file=open("employees.txt","w")

employee_file.write("\nram=salesman\njohny=manager\nToby=HR")

employee_file.close()

# 3.Create new file

html_file=open("index.html","w")

html_file.write("<p> This is HTML</P>")

html_file.close()

#Modules

import useful

print(useful.beatles)
print(useful.get_file_ext("test.txt"))
print(useful.roll_dice(10))
print(useful.feet_in_mile)
print(useful.meters_in_kilometer)