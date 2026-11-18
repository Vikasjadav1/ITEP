'''
22. Payment Gateway

Abstract class Payment.

Derived:

CreditCard
UPI
Wallet

Implement payment processing.
'''

from abc import ABC,abstractmethod

class Makepayment(ABC):
    @abstractmethod
    def payment(self):
        pass


class CreditCard(Makepayment):
    def payment(self,payment):
        print(f"payment using credit card  : {payment}")

class UPI(Makepayment):
    def payment(self,payment):
        print(f"payment using upi : {payment}")

class Wallet(Makepayment):
    def payment(self,payment):
        print(f"payment using wallet  : {payment}")



print("1 for using cerdit card")
print("2 for using UPI")
print("3 for credit wallet")

choice=int(input("enter choice.."))

pay=None
if choice==1:
    pay=CreditCard()
elif choice==2:
    pay=UPI()
elif choice==3:
    pay=Wallet()

pay.payment(200000)

