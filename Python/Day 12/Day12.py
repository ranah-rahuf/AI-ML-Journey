#FUNCTIONS:

#PART 1

#basic foundation:
def greet():
    print("Hello!")

greet()
#with parameters
def greet(name):
    print("Hello!", name)

greet("Ranah")

#returning values
def add(a, b):
    return a + b

result = add(10, 20)

print(result)

#returning values comparison 
def add(a, b):
    print(a + b)

def add(a, b):   #this version is generally more useful because we can reuse the result:
    return a + b

result = add(10, 20)

if result > 25:
    print("Large")

#Default parameters
def greet(name="Student"):
    print("Hello", name)

greet()
greet("Ranah")


#PART 2 — *args
#used when we don't know about the number of parameters

def display_numbers(*numbers):
    print(numbers)

display_numbers(80, 90, 70)
display_numbers(80, 90, 70, 85, 95)

#*args allows a function to accept a variable number of positional arguments.
# Inside the function, args behaves like a tuple.

#can use normal python operations on it

def calculate_total(*numbers):
    return sum(numbers)

print(calculate_total(10, 20, 30, 40))

#PART 3 - **kwargs

#**kwargs  allows a function to accept a variable number of keyword arguments.
#Inside the function, kwargs behaves like a dictionary.

def show_student(**details):
    print(details)

show_student(name="Ranah", age=21, course="CSD")

# *args vs **kwargs:
def example(*args, **kwargs):
    print(args)
    print(kwargs)

example(10, 20, name="Ranah", course="CSD")

#PART 4 - Lambda

#anonymous functions
def square(x):
    return x * x

sq = square(5)
print(sq)

#instead we can write
square = lambda x: x * x
print(square(5))

#PART 5 - map()

#Apply function to every item

numbers = [1, 2, 3, 4, 5]

squares = list(map(lambda x: x * x, numbers))

print(squares)

#PART 6 - filter()

#Keep only the items that satisfy a condition

numbers = [1, 2, 3, 4, 5, 6]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print(even_numbers)

