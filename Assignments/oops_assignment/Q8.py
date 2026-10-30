'''
Create a class Mobile with fields: brand, model, price.
Use setters to set values. Create a method to check if phone is affordable (price < 20000).
'''

class Mobile:
    def set_brand(self,brand):
        self.__brand=brand
    def set_model(self,model):
        self.__model=model
    def set_price(self,price):
        self.__price=price

    def check(self):
        if self.__price<20000:
            print("affordable")
        else:
            print("not affordable")


obj=Mobile()
obj.set_brand("oppo")
obj.set_model(87)
obj.set_price(54854)
obj.check()