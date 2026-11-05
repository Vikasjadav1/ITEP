class Software:
    def __init__(self,product_id,product_name,quantity,price):
        self.__product_id=product_id
        self.__product_name=product_name
        self.__quantity=quantity
        self.__price=price

    def add_stock(self,stock):
        if stock<=0:
            print("invalid stock.........")
        else:
            self.__quantity+=stock
            print("stock added successfully...........")

    def purchase(self,quantity):
        self.__quantity-=quantity
        print("purchase successfully....")

    def inventory_value(self):
        value=0
        value+=self.__quantity*self.__price
        return value
        
laptop=Software(101,"laptop",50,50000)
laptop.purchase(9)
laptop.add_stock(8)
laptop_inventory_value=laptop.inventory_value()
print(f"laptop_inventory_value : {laptop_inventory_value}")

