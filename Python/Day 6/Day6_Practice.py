# 1.
from PracticeClass import Studentpractice

student1=Studentpractice("Johny", 14 ,"Accounting")
student2=Studentpractice("Jim", 18 ,"BBA")
student3=Studentpractice("kim", 20 ,"BTech")

print("Details of Student 1:")
print("Name :"+student1.name)
print("Age :"+str(student1.age))
print("Course :"+student1.course)

print("\nDetails of Student 2:")
print("Name :"+student2.name)
print("Age :"+str(student2.age))
print("Course :"+student2.course)

print("\nDetails of Student 3:")
print("Name :"+student3.name)
print("Age :"+str(student3.age))
print("Course :"+student3.course)

# 2.

from PracticeClass import Book

book1=Book("Apple","John" ,"78")
book2=Book("10 days","louis" ,"120")

print("BOOK 1 :")
print("Title : "+book1.title)
print("Author : "+book1.author)
print("Pages : "+book1.pages)
print("\n")
print("BOOK 2 :")
print("Title : "+book2.title)
print("Author : "+book2.author)
print("Pages : "+book2.pages)

# 3.

from PracticeClass import Mobile

mobile1=Mobile("Samsung" ,"Galaxy","7k")
mobile2=Mobile("Vivo" ,"Y300","22k")
print("MOBILE 1 :")
print("Brand : "+mobile1.brand)
print("Model : "+mobile1.model)
print("Price : "+mobile1.price)
print("\n")
print("MOBILE 2 :")
print("Brand : "+mobile2.brand)
print("Model : "+mobile2.model)
print("Price : "+mobile2.price)

# 4.create a constructor

from PracticeClass import Laptop

b=input("Enter Brand of Laptop :")
r=input("Enter RAM :")
p=input("Enter Price :")

Laptop1=Laptop(b ,r ,p )

print("Brand :"+Laptop1.brand)
print("RAM :"+Laptop1.ram)
print("Price :"+Laptop1.price)


