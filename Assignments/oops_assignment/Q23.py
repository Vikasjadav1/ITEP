'''
. Write a Java program to create a class called "Inventory" with a collection of products and 
methods to add and remove products, and to check for low inventory.
'''

class Inventory:
    products=[]

    def add(self,product_id,product_name,quantity):
        self.__product_id=product_id
        self.__product_name=product_name
        self.__quantity=quantity

        Inventory.products.append({
            "product_id":product_id,
            "product_name":product_name,
            "quantity":quantity
        })

    def remove(self,product_id):
        for product in Inventory.products:
            if product["product_id"]==product_id:
                Inventory.products.remove(product)
                print("removed................")
        else:
            print("product not exist............")

    def check_quantity(self):
        for product in Inventory.products:
            if product["quantity"]<5:
                print(f"low quantity {product["product_name"]}")


pd1=Inventory()
pd2=Inventory()
pd3=Inventory()
pd1.add(101,"laptop",8)
pd2.add(102,"mouse",2)
pd3.add(103,"tv",3)
print(Inventory.products)

pd1.remove(101)
print(Inventory.products)

pd1.check_quantity()

