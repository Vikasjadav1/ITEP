'''
5. Online Shopping Discount System
Problem Statement

Different customer types receive different discounts.

Create:

abstract class Customer

Child:

RegularCustomer
PremiumCustomer
VIPCustomer

Rules:

Regular → 5%
Premium → 10%
VIP → 20%
'''

from abc import ABC,abstractmethod
class Cutomer(ABC):
    @abstractmethod
    def discount(self):
        pass

class RegularCustomer(Cutomer):
    def discount(self):
        bill=int(input("enter bill :"))
        bonus=bill*5/100
        final_bill=bill-bonus
        print(f"total bill : {bill} ")
        print(f"5 % discount : {bonus}")
        print(f"final bill after discount  : {final_bill}")

class PremiumCustomer(Cutomer):
    
    def discount(self):
        bill=int(input("enter bill :"))
        bonus=bill*10/100
        final_bill=bill-bonus
        print(f"total bill : {bill} ")
        print(f"10 % discount : {bonus}")
        print(f"final bill after discount  : {final_bill}")

class VIPCustomer(Cutomer):
    def discount(self):
        bill=int(input("enter bill :"))
        bonus=bill*20/100
        final_bill=bill-bonus
        print(f"total bill : {bill} ")
        print(f"20 % discount : {bonus}")
        print(f"final bill after discount  : {final_bill}")

obj=None
print("1 Regular customer ")
print("2 premium cutomer ")
print("3 VIP customer")
choice = int(input("enter choice : "))
if choice==1:
    obj=RegularCustomer()
elif choice==2:
    obj=PremiumCustomer()
elif choice==3:
    obj=VIPCustomer()
else:
    print("invalid choice..........")

obj.discount()