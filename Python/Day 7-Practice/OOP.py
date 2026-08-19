# Create a Student class
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

#add method:
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Create multiple objects
student1 = Student("Alice", 20)
student2 = Student("Bob", 22)
student1.display_info()
student2.display_info()

#Challenge 1:
class BankAccount:
    def __init__(self ,name ,balance):
        self.name=name
        self.balance=balance
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit: {amount}\nCurrent balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print(f"Withdraw: {amount}\nCurrent balance: {self.balance}")
    def display_balance(self):
        print(f"Account holder: {self.name}\nBalance: {self.balance}")

name1=input("Enter account holder name: ")
balance1=float(input("Enter initial balance: "))
account1 = BankAccount(name1, balance1)
account1.display_balance()
account1.deposit(2000)
account1.withdraw(1000)
