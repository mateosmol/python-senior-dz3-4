"""Завдання 1"""
class BankAccount():
    def __init__(self, account_number, balance):
        self.balance = balance
        self.account_number = account_number

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount < self.balance:
            self.balance -= amount
        else:
            print("Недостатньо коштів для зняття!")

"""Демонстрація"""
account = BankAccount(123456789, 0)
print(account.account_number)
account.deposit(200)
print(account.balance)
account.withdraw(100)
print(account.balance)
account.withdraw(100)
