from PracticeClass import Book

book1=Book("I don't love you anymore","Rithvik Singh" ,"120")
book2=Book("In the Silence You Left Behind","Sumitra Manda" ,"140")
book3=Book("King of Sloth","Ana Huang" ,"100")
book4=Book("Can we strangers again?","Shrijeet shandilya" ,"180")
book5=Book("Don't believe everything you think","Joseph nguyen" ,"88")

print("==========LIBRARY==========")
print("BOOK 1 :")
print("Title : "+book1.title)
print("Author : "+book1.author)
print("Pages : "+book1.pages)
print("\n")
print("BOOK 2 :")
print("Title : "+book2.title)
print("Author : "+book2.author)
print("Pages : "+book2.pages)
print("\n")
print("BOOK 3 :")
print("Title : "+book3.title)
print("Author : "+book3.author)
print("Pages : "+book3.pages)
print("\n")
print("BOOK 4 :")
print("Title : "+book4.title)
print("Author : "+book4.author)
print("Pages : "+book4.pages)
print("\n")
print("BOOK 5 :")
print("Title : "+book5.title)
print("Author : "+book5.author)
print("Pages : "+book5.pages)

#Using Loops:
books=[book1 , book2 ,book3 ,book4 ,book5 ]

for index, book in enumerate(books, start=1):
    print(f"Book {index}")
    print("Title:", book.title)
    print("Author:", book.author)
    print("Pages:", book.pages)
    print()

# Car

class Car:
    def __init__(self ,brand ,color ,year ):
        self.brand=brand
        self.color=color
        self.year=year

car1=Car("BMW" ,"Black" ,"2026")
car2=Car("Porsche" ,"Guards Red" ,"2026")

print("Car 1 :")
print("Brand : "+car1.brand)
print("Color : "+car1.color)
print("Year : "+car1.year)
print("\nCar 2 :")
print("Brand : "+car2.brand)
print("Color : "+car2.color)
print("Year : "+car2.year)