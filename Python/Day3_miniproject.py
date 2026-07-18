# Student Marks Manager

#Ask the user:Name,Marks in 3 subjects and then Calculate Total and Average

name = input("Enter student's name: ")
marks1 = float(input("Enter marks in subject 1: "))
marks2 = float(input("Enter marks in subject 2: "))
marks3 = float(input("Enter marks in subject 3: "))

total = marks1 + marks2 + marks3
average = total / 3

print("\n=====Student Report=====")
print("Name: ", name)
print("Subject 1: ", marks1)
print("Subject 2: ", marks2)   
print("Subject 3: ", marks3)
print("Total: ", total)
print("Average: ", average)

if average >= 50:
    print("Result: Pass")
else:
    print("Result: Fail")

print("========================")