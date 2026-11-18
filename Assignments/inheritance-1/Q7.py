'''
7. Shopping Cart System

Base:

Product

Derived:

Electronics
Grocery
Clothing

Apply discounts.


'''

from abc import ABC,abstractmethod
class Product(ABC):
    @abstractmethod
    def discount(self):
        pass

class Electronics(Product):
    def discount(self,bill):
        after_discount=bill-(bill*30/100)
        print(f"original bill : {bill}")
        print(f"bill after 30% discount : {after_discount}")

class Grocery(Product):
    def discount(self,bill):
        after_discount=bill-(bill*20/100)
        print(f"original bill : {bill}")
        print(f"bill after 20% discount : {after_discount}")

class Clothing(Product):
    def discount(self,bill):
        after_discount=bill-(bill*10/100)
        print(f"original bill : {bill}")
        print(f"bill after 10% discount : {after_discount}")


obj=Electronics()
obj.discount(4000)
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++")
obj=Grocery()
obj.discount(4000)
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++")
obj=Clothing()
obj.discount(4000)
