#Exercise 1:Safe Integer Input

try:
    number = int(input("Enter a number : "))

except ValueError:
    print("Invalid input! Please enter a number.")
else:
    print("You entered:", number)

#Exercise 2 — Division Calculator
try:
    number1 = int(input("Enter first number: "))
    number2 = int(input("Enter second number: "))
    result = number1 / number2
    print("Result:", result)
except ValueError:
    print("Invalid input!")
except ZeroDivisionError:
    print("Cannot divide by zero!")

#Exercise 3 — try-except-else

try:
    age = int(input("Enter your age: "))
    if age <= 0:
        raise ValueError("Invalid age !")
        
except ValueError as e:
    print(e)
else:
    print("Valid age:", age)


#Exercise 4 — try-except-finally
try:
    with open("data.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("File not found!")
finally:
    print("File operation completed.")

#Exercise 5 — Marks Validation with raise
try:
    marks = int(input("Enter your marks: "))
    if marks < 0 or marks > 100:
        raise ValueError("Invalid marks! Marks must be between 0 and 100.")
except ValueError as e:
    print(e)

#Exercise 6 — Multiple Exceptions-calculator
try:
    number1 = int(input("Enter first number: "))
    number2 = int(input("Enter second number: "))
    add = number1 + number2
    print("Addition:", add)
    subtract = number1 - number2
    print("Subtraction:", subtract)
    multiply = number1 * number2
    print("Multiplication:", multiply)
    division = number1 / number2
    print("Division:", division)
except ValueError:
    print("Invalid input!")
except ZeroDivisionError:
    print("Cannot divide by zero!")

#Exercise 7 — Function + Exception Handling

def get_positive_number():
    while True:
        try:
            number = int(input("Enter a positive number: "))
            if number <= 0:
                print("Number must be greater than 0.")
                continue
            return number
        except ValueError:
            print("Invalid input!")

print(get_positive_number())