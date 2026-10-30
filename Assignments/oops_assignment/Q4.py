'''
Create a class Product with fields: productId, name, quantity, price.
Use setters to assign values. Add a method to calculate total value (quantity * price).
'''

class Product:
    def set_productId(self,productId):
        self.__productId=productId
    def set_name(self,name):
        self.__name=name
    def set_quantity(self,quantity):
        self.__quantity=quantity
    def set_price(self,price):
        self.__price=price
    
    def display(self):
        print(f"product id {self.__productId}")
        print(f"name {self.__name}")
        print(f"quantity {self.__quantity}")

obj=Product()
obj.set_productId(101)
obj.set_name("burbone")
obj.set_quantity(652)
obj.set_price(65)

obj.display()
