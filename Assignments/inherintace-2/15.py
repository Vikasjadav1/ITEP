'''
15. Payment Processing System
Problem Statement

Payment methods process payments differently.

Create:

abstract class Payment

Child:

CreditCard
DebitCard
'''

from abc import ABC, abstractmethod

class Payment(ABC):

    @abstractmethod
    def process_payment(self):
        pass


class CreditCard(Payment):

    def process_payment(self):
        amount = int(input("Enter payment amount: "))
        print("Payment of", amount, "processed using Credit Card.")


class DebitCard(Payment):

    def process_payment(self):
        amount = int(input("Enter payment amount: "))
        print("Payment of", amount, "processed using Debit Card.")


print("Choose Payment Method:")
print("1. Credit Card")
print("2. Debit Card")

choice = int(input("Enter your choice: "))

if choice == 1:
    obj = CreditCard()

elif choice == 2:
    obj = DebitCard()

else:
    print("Invalid choice")
    obj = None

if obj:
    obj.process_payment()