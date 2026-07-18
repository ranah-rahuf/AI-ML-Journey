# 1. Create a dictionary:
student = {
    "name": "Ranah",
    "age": 21,
    "course": "AI/ML"
}

print(student["name"])
print(student["age"])
print(student["course"])

# 2.print 1 to 5 using while loop
i=1
while i<=5:
    print(i)
    i+=1

# 3. print Python,AI,Machine Learning,Data Science
subjects = ["Python", "AI", "Machine Learning", "Data Science"]
for subject in subjects:
    print(subject)

# 4. Print numbers 1–20 using for loop
for num in range(1, 21):
    print(num)

# 5. Calculate the sum of numbers from 1 to 10
total = 0
for num in range(1, 11):
    total+=num
print("The sum of numbers from 1 to 10 is:", total)