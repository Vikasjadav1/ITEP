'''
8. Online Food Delivery

Parent:

FoodItem

Derived:

Pizza
Burger
Sandwich

Calculate total bill.
'''

from abc import ABC,abstractmethod
class FoodItem(ABC):
    @abstractmethod
    def total_bill(self):
        pass


class Pizza(FoodItem):
    def total_bill(self,bill):
        discount_bill=bill-(bill*25/100)
        after_gst=discount_bill+(discount_bill*18/100)
        print(f"total bill : {bill}")
        print(f"total bill after 25% discount : {discount_bill}")
        print(f"total bill after gst : {after_gst}")


class Burger(FoodItem):
    def total_bill(self,bill):
        discount_bill=bill-(bill*5/100)
        after_gst=discount_bill+(discount_bill*18/100)
        print(f"total bill : {bill}")
        print(f"total bill after 5% discount : {discount_bill}")
        print(f"total bill after gst : {after_gst}")

class Sandwich(FoodItem):
    def total_bill(self,bill):
        discount_bill=bill-(bill*20/100)
        after_gst=discount_bill+(discount_bill*18/100)
        print(f"total bill : {bill}")
        print(f"total bill after 20% discount : {discount_bill}")
        print(f"total bill after gst : {after_gst}")


obj=Pizza()
obj.total_bill(1000)

print("------------------------------------------------------------------------")

obj=Burger()
obj.total_bill(1000)

print("------------------------------------------------------------------------")

obj=Sandwich()
obj.total_bill(1000)