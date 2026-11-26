'''
21. Online Subscription Plans
Problem Statement

Streaming app has multiple subscription plans.

Create:

abstract class Subscription

Child:

BasicPlan
StandardPlan
PremiumPlan

Each has different:

price
screen limits
'''
from abc import ABC,abstractmethod

class Subscription(ABC):
    def __init__(self,price,screen_limit):
        self.__price=price
        self.__screen_limit=screen_limit

    def get_price(self):
        return self.__price

    def get_screen_limit(self):
        return self.__screen_limit
        
    @abstractmethod
    def plan(self):
        pass

class BasicPlan(Subscription):
    def plan(self):
        print("Basic Plan")
        print("Price:", self.get_price())
        print("Screen Limit:", self.get_screen_limit())



class StandardPlan(Subscription):
    def plan(self):
        print("Standard Plan")
        print("Price:", self.get_price())
        print("Screen Limit:", self.get_screen_limit())


class PremiumPlan(Subscription):
    def plan(self):
        print("Premium Plan")
        print("Price:", self.get_price())
        print("Screen Limit:", self.get_screen_limit())

print("1 basic plan ")
print("2 standard plan ")
print("3 premium plan ")
choice=int(input("enter plan :"))

if choice==1:
    obj=BasicPlan(499,1)
elif choice==2:
    obj=StandardPlan(799,3)
elif choice==3:
    obj=PremiumPlan(999,5)
else:
    print("invalid choice.....")
    obj=None

if obj:
    obj.plan()