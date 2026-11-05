'''
3. Online Shopping Cart
Problem

Create a shopping cart system.

Requirements

A cart should:

store customer name
maintain list of products
maintain total bill
Functionalities
Add product
Remove product
Calculate final amount 
Apply discount using static method
Track total carts created
Concepts Practiced
list inside object
object interaction
static method
class variable
'''

class Shopping:
    __cart_count=0
    
    def __init__(self,name):
        self.__name=name
        self.__product=[]
        self.__total_bill=0
        Shopping.__cart_count+=1

    def add_item(self,item,price):
        self.__product.append({item:price})


    def remove_item(self, item):
        for product in self.__product:
            if item in product:
                self.__product.remove(product)
                print("Removed successfully")
                return

        print("Product not found")

    def discount(self,total_bill):
        final_bill=total_bill
        final_bill-=(total_bill*10)/100
        return final_bill

    def final_bill(self):
        __total_bill=0
        for items in self.__product:
            for item,price in items.items():
                __total_bill+=price
        return __total_bill

    @classmethod
    def get_counter(cls):
        return cls.__cart_count


obj1=Shopping("jp")
obj1.add_item("mouse",500)
obj1.add_item("laptop",50000)
# obj1.remove_item("mouse")
print(Shopping.get_counter())

# obj2=Shopping("jp")
# obj2.add_item("laptop",50000)
# obj2.remove_item("mouse")
print(f"total carts created :{Shopping.get_counter()}")

total_bill=obj1.final_bill()
print(f"total bill {total_bill}")

final_bill=obj1.discount(total_bill)
print(f"after 10 % discount {final_bill}")


                                                 