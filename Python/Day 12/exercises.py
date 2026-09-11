#Exercise 1

def calculate_average(n1, n2, n3):
    return (n1 + n2 + n3) / 3

average = calculate_average(80, 90, 70)
print(average)

#Exercise 2

def calculate_average(*numbers):
    return sum(numbers) / len(numbers)

average=calculate_average(80, 90, 70, 60, 100)
print(average)

#Exercise 3

def student_info(**details):
    return details

details = student_info(name="Ranah", age=21, course="CSD")
print(details)
print(details["name"])

#Exercise 4 

cube = lambda x: x * x * x 

print(cube(4))

#Exersie 5

numbers = [10, 20, 30, 40, 50]

twice = list(map(lambda x: x * 2, numbers))
print(twice)

#Exercise 6

numbers = [10, 15, 20, 25, 30, 35, 40]

output = list(filter(lambda x: x > 20, numbers))

print(output)

#Challenge : Combining filter() + map()

numbers = [5, 10, 15, 20, 25, 30]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))   #filter → select what I want

new_numbers = list(map(lambda x: x * 10, even_numbers))   #map → transform what I selected

print(new_numbers)

#Challenge : Combining *args + **kwargs

def process_students(*marks, **details):
    average = sum(marks) / len(marks)

    details["Average"] = average
    return details
   

result = process_students(
    80, 90, 70, 85,
    name="Ranah",
    course="CSD"
)

print(result)




