'''
23. Banking Withdrawal System
Problem Statement

Withdrawal rules vary by account type.

Create:

abstract class Account

Child:

SavingsAccount
CurrentAccount
'''
from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def set_balance(self, balance):
        self.__balance = balance

    @abstractmethod
    def withdraw(self):
        pass


class SavingsAccount(Account):
    def withdraw(self):
        withdraw_amount = int(input("Enter amount: "))

        if withdraw_amount <= 0:
            print("Invalid amount")

        elif self.get_balance() - withdraw_amount < 2000:
            print("Insufficient balance: Minimum 2000 required")

        else:
            balance = self.get_balance() - withdraw_amount
            self.set_balance(balance)
            print(f"Withdrawal successful: {withdraw_amount}")
            print("Remaining balance:", self.get_balance())


class CurrentAccount(Account):
    def withdraw(self):
        withdraw_amount = int(input("Enter amount: "))

        if withdraw_amount <= 0:
            print("Invalid amount")

        elif self.get_balance() - withdraw_amount < 5000:
            print("Insufficient balance: Minimum 5000 required")

        else:
            balance = self.get_balance() - withdraw_amount
            self.set_balance(balance)
            print(f"Withdrawal successful: {withdraw_amount}")
            print("Remaining balance:", self.get_balance())


# Main Program

print("----- Bank Account System -----")
print("1. Savings Account")
print("2. Current Account")

choice = int(input("Enter your choice: "))

balance = int(input("Enter initial balance: "))

if choice == 1:
    obj = SavingsAccount(balance)

elif choice == 2:
    obj = CurrentAccount(balance)

else:
    print("Invalid choice")
    obj = None

if obj:
    print("\nInitial Balance:", obj.get_balance())
    obj.withdraw()