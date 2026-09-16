#   BANK MANAGEMENT SYSTEM

#TASK 1  :  BankAccount
class BankAccount:
    def __init__(self, account_number, owner, balance):
        self.account_number = account_number
        self.owner = owner
        self._balance = balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
        else:
            print("Amount must be greater than 0")
            return

    def withdraw(self, amount):
        if amount >= 0:
            if amount <= self._balance :
                self._balance -= amount
            else:
                print("Insufficient Balance")

        else:
            print("Amount must be greater than 0")
        
    def get_balance(self):
        return self._balance

    def display_account(self):
        print(f"Account Number : {self.account_number}")
        print(f"Owner : {self.owner}")
        print(f"Balance : {self.get_balance()}")


account1 = BankAccount(1001, "Ranah", 5000)
account1.display_account()

account1.deposit(1500)
print(account1.get_balance())

account1.withdraw(2000)
print(account1.get_balance())

account1.withdraw(10000)
print(account1.get_balance())

account1.withdraw(-500)
print(account1.get_balance())

   
class SavingsAccount(BankAccount):
    def __init__(self, account_number, owner, balance, interest_rate):
        super().__init__(account_number, owner, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = (self.get_balance() * self.interest_rate )/ 100
        self.deposit( interest)
        print(f"After Interest : {self.get_balance()}")


account2 = SavingsAccount(2001, "Ranah", 10000, 5)
account2.display_account()
account2.add_interest()

class CurrentAccount(BankAccount):
    def __init__(self, account_number, owner, balance, overdraft_limit):
        super().__init__(account_number, owner, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount >= 0:
            new_balance = self.get_balance() - amount

            if new_balance >= -self.overdraft_limit:
                self._balance -= amount
            else:
                print("Insufficient Balance")
        else:
            print("Amount must be greater than 0")
       

account3 = CurrentAccount(3001, "Ranah", 5000, 2000)
account3.withdraw(4000)
print(account3.get_balance())

account3.withdraw(2000)
print(account3.get_balance())

account3.withdraw(1500)
print(account3.get_balance())

account1 = BankAccount(1001, "Ranah", 5000)
account2 = SavingsAccount(2001, "Ranah", 5000, 5)
account3 = CurrentAccount(3001, "Ranah", 5000, 2000)
accounts = [
    account1,
    account2,
    account3
]

for account in accounts:
    account.withdraw(1000)
    print(account.get_balance())