'''
2. Bank Account Simulation
Problem

Design a banking system using OOP.

Requirements

Each account should contain:

account number
holder name
balance
Functionalities
Deposit money
Withdraw money
Prevent withdrawal if balance insufficient
Display account summary
Maintain bank-wide interest rate as class variable
Add static method to validate minimum balance rule
Concepts Practiced
object state management
static methods
class variables
validations
'''

class Account:
    __inetrest=3
    def __init__(self,acc_no,holder_name,balance,):
        self.__acc_no=acc_no
        self.__holder_name=holder_name
        self.__balance=balance

    def deposit(self,amount):
        if amount<=0:
            print("invalid amount.............")
        else:
            self.__balance+=amount
            print(f"{amount} deposit sucessfull")

    def withdraw(self,amount):
        if amount<=0:
            print("invalid amount........... ")
        elif self.__balance>=amount:
            self.__balance-=amount
            print(f"{amount} withdraw successfully.......")
        else:
            print("unsufficient balance")

    def display(self):
        print(f"Holer name : {self.__holder_name}")
        print(f"Account number : {self.__acc_no}")
        print(f"Balance : {self.__balance}")
        print(f"Interest Rate : {Account.__inetrest}%")

    @staticmethod
    def validate_balance(balance):
        return balance >= 100

acc=Account(484989498895,"vikas",100)
acc.deposit(8)
acc.display()
acc.withdraw(-2)
acc.display()

print(Account.validate_balance(500))