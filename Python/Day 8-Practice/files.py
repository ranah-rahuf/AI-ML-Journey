#Read the file.
fruits_file=open("practice.txt","r")
print(fruits_file.readable())
print(fruits_file.read())
fruits_file.close()

#Append new information.
fruits_file=open("practice.txt","a")
fruits_file.write("\nPotato - Vegetable")
fruits_file.close()

#Count lines.
fruits_file=open("practice.txt","r")
count=0
for fruit in fruits_file:
    count+=1
print(count)

#Search for a name.

fruits_file=open("practice.txt","r")
if "Tomato - Vegetable" in fruits_file.read():
    print("search found")
else:
    print("search not found")
fruits_file.close()