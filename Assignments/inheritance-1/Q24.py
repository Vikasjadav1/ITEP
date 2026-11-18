
from abc import ABC, abstractmethod

class ATM(ABC):
    @abstractmethod
    def check_balance(self):
        pass

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass


class SBIATM(ATM):
    def __init__(self, balance):
        self.balance = balance

    def check_balance(self):
        print("SBI Balance:", self.balance)

    def deposit(self, amount):
        self.balance += amount
        print("Amount deposited in SBI.")

    def withdraw(self, amount):
        if self.balance - amount >= 1000:
            self.balance -= amount
            print("SBI Withdrawal Successful.")
        else:
            print("Minimum balance of 1000 required.")


class HDFCATM(ATM):
    def __init__(self, balance):
        self.balance = balance

    def check_balance(self):
        print("HDFC Balance:", self.balance)

    def deposit(self, amount):
        self.balance += amount
        print("Amount deposited in HDFC.")

    def withdraw(self, amount):
        if self.balance - amount >= 5000:
            self.balance -= amount
            print("HDFC Withdrawal Successful.")
        else:
            print("Minimum balance of 5000 required.")



sbi = SBIATM(10000)
sbi.check_balance()
sbi.deposit(2000)
sbi.withdraw(3000)
sbi.check_balance()

print("-------------------")


hdfc = HDFCATM(20000)
hdfc.check_balance()
hdfc.deposit(5000)
hdfc.withdraw(4000)
hdfc.check_balance()
