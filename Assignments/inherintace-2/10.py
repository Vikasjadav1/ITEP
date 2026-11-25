'''
10. Loan Interest Calculator
Problem Statement

Banks offer different interest rates.

Create:

abstract class Loan

Child:

HomeLoan
CarLoan
EducationLoan
Formula

Interest=
100
P×R×T
'''

from abc import ABC, abstractmethod

class Loan(ABC):
    def __init__(self, p, r, t):
        self.p = p
        self.r = r
        self.t = t

    @abstractmethod
    def calculate_interest(self):
        pass


class HomeLoan(Loan):
    def calculate_interest(self):
        interest = (self.p * self.r * self.t) / 100
        print("Home Loan Interest:", interest)


class CarLoan(Loan):
    def calculate_interest(self):
        interest = (self.p * self.r * self.t) / 100
        print("Car Loan Interest:", interest)


class EducationLoan(Loan):
    def calculate_interest(self):
        interest = (self.p * self.r * self.t) / 100
        print("Education Loan Interest:", interest)


p = float(input("Enter Principal Amount: "))
r = float(input("Enter Rate of Interest: "))
t = float(input("Enter Time in years: "))

print("\n1. Home Loan")
print("2. Car Loan")
print("3. Education Loan")

choice = int(input("Enter your choice: "))

if choice == 1:
    loan = HomeLoan(p, r, t)
elif choice == 2:
    loan = CarLoan(p, r, t)
elif choice == 3:
    loan = EducationLoan(p, r, t)
else:
    print("Invalid Choice!")
    exit()

loan.calculate_interest()