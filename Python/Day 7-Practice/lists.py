# 1.Largest element
numbers=[3,45,43,25,67,12]
numbers.sort()
print(numbers[-1])# By using this method it changes the original number order

# 1.better version
numbers=[3,45,43,25,67,12]
print(max(numbers))

# 1. By using loop:
numbers=[3,45,43,25,67,12]
largest=numbers[0]
for number in numbers:
    if number>largest:
        largest=number
print(largest)


# 2. Second largest
numbers=[3,45,43,25,67,12]
numbers.sort()
print(numbers[-2])

# 2. without changing the original list
temp = numbers.copy()

temp.sort()

print(temp[-2])

# 2.without using built-in functions
numbers = [3,45,43,25,67,12]

largest = numbers[0]
second = numbers[0]

for number in numbers:

    if number > largest:
        second = largest
        largest = number

    elif number > second and number != largest:
        second = number

print(second)

# 3. Remove duplicates
months=["jan","feb","jan","mar","feb"]
newmonths=[]
for month in months:
    if month not in newmonths:
        newmonths.append(month)
print(newmonths)

# 4. Sum of list
numbers=[1,2,3,4,5,6,7,8,9]
total=0
for number in numbers:
    total+=number
print(total)

# 5.Find even numbers
numbers=[1,2,3,4,5,6,7,8,9]
evennumbers=[]
for number in numbers:
    if number%2==0:
        evennumbers.append(number)
print(evennumbers)

# 6.Challenge 1 :input -numbers = [10, 20, 30, 40, 50] amd output-50 40 30 20 10
numbers = [10, 20, 30, 40, 50]
for i in range(len(numbers)):
    print(numbers[len(numbers)-1-i])

#cleaner version
for i in range(len(numbers)-1, -1, -1):
    print(numbers[i])

# 7.Challenge 2 :input -numbers = [1 ,2 ,3 ,4 ,5] and output- 1 4 9 16 25
numbers = [1, 2, 3, 4, 5]
squared_numbers = []
for i in range(len(numbers)):
    squared_numbers.append(numbers[i]*numbers[i])
print(squared_numbers)

#cleaner version
for number in numbers:
    squared_numbers.append(number * number)
print(squared_numbers)
# 8. Challenge 3:input-numbers = [5,10,15,20,25] and find average ,average =15

numbers = [5,10,15,20,25]
total=0
for i in range(len(numbers)):
    total+=numbers[i]
average=total/len(numbers)
print(average)

