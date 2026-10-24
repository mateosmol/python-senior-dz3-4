"""Завдання 3"""

class BankAccount:
    def __init__(self, owner, account_number, balance=0):
        self.owner = owner
        self.account_number = account_number
        self.balance = balance

    def __str__(self):
        return f"{self.owner}: {self.balance} грн"


class Bank:
    def __init__(self):
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    def deposit(self, account, amount):
        if amount > 0:
            account.balance += amount
            print(f"Deposited {amount} грн to {account.owner}")
        else:
            print("Invalid amount")

    def withdraw(self, account, amount):
        if amount <= 0:
            print("Invalid amount")
        elif account.balance >= amount:
            account.balance -= amount
            print(f"Withdrawn {amount} грн from {account.owner}")
        else:
            print("Not enough money")

    def transfer(self, sender, receiver, amount):
        if amount <= 0:
            print("Invalid amount")
        elif sender.balance >= amount:
            sender.balance -= amount
            receiver.balance += amount
            print(
                f"Transferred {amount} грн "
                f"from {sender.owner} to {receiver.owner}"
            )
        else:
            print("Not enough money")

    def show_accounts(self):
        for account in self.accounts:
            print(account)


"""Демонстрація"""

account1 = BankAccount("Alex", "1001", 1000)
account2 = BankAccount("Max", "1002", 500)

bank = Bank()

bank.add_account(account1)
bank.add_account(account2)

bank.show_accounts()

print()

bank.deposit(account1, 300)
bank.withdraw(account2, 200)
bank.transfer(account1, account2, 500)

print()

bank.show_accounts()
