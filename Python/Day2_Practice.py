# 1. Print a list.
months=["jan","feb","mar","apr","may"]
print(months)
# 2. Print the first element.
print(months[0])
# 3. Print the last element.
print(months[-1])
# 4. Add an item.
months.append("jun")
print(months)
# 5. Remove an item.
months.remove("jan")
print(months)
# 6. Replace an item.
months[3]="dec"
print(months)
# 7. Create a tuple.
tuple=(3,5,6,8,9)
print(tuple)
# 8. Input age → Adult/Minor.
age = int(input("Enter your age: "))
if age < 18:
    print("minor")
else:
    print("adult")
# 9. Input marks → Pass/Fail.
mark=int(input("enter your mark:"))
passmark=int(input("Enter Pass Mark:"))

if mark > passmark:
    print("Pass")
else:
    print("fail")

# 10. Print whether a number is positive or negative.
number=float(input("Enter a number:"))
if number<0:
    print("Negative")
elif number>0:
    print("positive")
else:
    print("zero")

# 11. Lists Create a list of Fruits.Print First item,Last item,Entire list.Modify List Add an item,Remove an item,Replace an item.
fruits=["Apple","Orange","Mango","kiwi"]
print(fruits[0])
print(fruits[-1])
print(fruits)

fruits.append("Banana")
print(fruits)
fruits.remove("Orange")
print(fruits)
fruits[0]="Jackfruit"
print(fruits)
