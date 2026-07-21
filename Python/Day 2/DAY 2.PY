# MAD LIBS GAME
color = input("Enter a color: ")
plural_noun = input("Enter a plural noun: ")
celebrity=input("Enter a celebrity name: ")

print("Roses are "+color)
print(plural_noun+" are blue")
print("I love "+celebrity)

#Lists
friends=["levin","kevin","leo","melvin","john","jim"]
print(friends)
print(friends[0])
print(friends[-1])
print(friends[1:])
print(friends[1:3])
friends[0]="Mike"
print(friends)

#Lists functions
lucky_numbers=[4,8,15,16,42,23]
friends.extend(lucky_numbers)
print(friends)
friends.append("creed")
print(friends)
friends.insert(1,"tom")
print(friends)
friends.remove("leo")
print(friends)
print(friends.index("kevin"))
friends.pop()
print(friends)
friends.clear()
print(friends)
month=["Jan","Feb","Mar","Apr","Apr","May"]
print(month.count("Apr"))
month.sort()
lucky_numbers.sort()
print(month)
print(lucky_numbers)
lucky_numbers.reverse()
print(lucky_numbers)
month2=month.copy()
print(month2)

# Tuples
coordinate=(4,5)
print(coordinate)
coordinates=[(4,5),(6,7)]
print(coordinates[1])

# Functions
def say_hi():
    print("hello user!")
say_hi()
def say_hi(name):
    print("hello "+name)
say_hi("Ranah")
def say_hello(name,age):
    print("hello "+name+" ! U R "+age)
say_hello("Ranah","5")
def say_hello(name,age):
    print("hello "+name+" ! U R "+str(age))
say_hello("Ranah",5)

#Return statement 
def cube(num):
    return num*num*num
result=cube(4)
print(result)

#If statements
is_female=True
is_male=False
is_tall=True

if is_female:
    print("You are female")
if is_male:
    print("You are male")
else:
    print("You are not male")
if is_male and is_tall:
    print("You are a tall male")
else:
    print("You are either not male or not tall or both")
if is_male or is_tall:
    print("You are either male or tall or both")
else:
    print("You are neither male nor tall")
if is_female and is_tall:
    print("You are a tall female")
elif is_female and not(is_tall):
    print("You are a short female")
elif not(is_female) and is_tall:
    print("You are a tall male")
else:
    print("You are a short male")

#If statements and comparisons
def max_num(num1,num2,num3):
    if num1 >= num2 and num1 >=num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(max_num(4,5,6))

#Calculator

num1=float(input("Enter 1st number: "))
op=input("enter operator: ")
num2=float(input("enter 2nd number: "))

if op == "+" :
    print(num1+num2)
elif op =="-":
     print(num1-num2)
elif op =="/":
     print(num1/num2)
elif op =="*":
     print(num1*num2)
else:
    print("Invalid")
