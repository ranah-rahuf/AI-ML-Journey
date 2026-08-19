# # 1. Calculator function
# def calculator(a, b, operation):
#     if operation == 'add':
#         return a + b
#     elif operation == 'subtract':
#         return a - b
#     elif operation == 'multiply':
#         return a * b
#     elif operation == 'divide':
#         if b != 0:
#             return a / b
#         else:
#             return "Error: Division by zero"
#     else:
#         return "Invalid operation"

# a=input("Enter first number: ")
# b=input("Enter second number: ")
# operation=input("Enter operation (add, subtract, multiply, divide): ")

# print(calculator(int(a), int(b), operation)) 

# # 2. Prime number function
# def is_prime(n):
#     if n<=1:
#         return False
#     for i in range(2,int(n**0.5)+1):
#         if n%i==0:
#             return False
#     return True

# print(is_prime(int(input("Enter a number to check if it's prime: "))))

# #cleaner version 
# def is_prime(number):

#     if number <= 1:
#         return False

#     for i in range(2, number):
#         if number % i == 0:
#             return False

#     return True 
# print(is_prime(7))

# # 3. Factorial

# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1)

# print(factorial(int(input("Enter a number to find its factorial: "))))

# # 4. Fibonacci
# def fibonacci(n):
#     fib_sequence=[0 ,1 ]
#     for i in range(2, n):
#         next_number=fib_sequence[i - 1] + fib_sequence[i - 2]
#         fib_sequence.append(next_number)
#     return fib_sequence
# print(fibonacci(int(input("Enter the number of terms for Fibonacci sequence: "))))


# 5. Challenge 1:count vowels:

def count_vowels(word):
    count=0
    for letter in word:
        if letter in "AEIOUaeiou":
                count+=1
    return count

print(count_vowels("programming"))

# 6. Challenge 2: Largest number
def largest(a ,b ,c ):
     return max(a ,b ,c )
print(largest(10,30,20))

# without built-in function
def largest(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
print(largest(10,30,20))

# 7. Challenge 3- reverse a word

def reverse(word):
     reverse=""
     for letter in word:
          reverse=letter + reverse
     return reverse
print(reverse("Python"))

# 8. Count even numbers
def count_even(numbers):
     count=0
     for number in numbers:
          if number%2==0:
               count+=1
     return count

numbers=[2, 5, 8, 9, 10]
print(count_even(numbers))
