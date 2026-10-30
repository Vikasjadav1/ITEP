'''
Create a class Car with fields: brand, model, and year.
Use setters to assign values. Create a method to print full car info.
'''

class Car:
    def set_brand(self,brand):
        self.__brand=brand
    def set_model(self,model):
        self.__model=model
    def set_year(self,year):
        self.__year=year

    def display(self):
        print(f"brand {self.__brand}")
        print(f"model {self.__model}")
        print(f"year {self.__year}")

obj=Car()
obj.set_brand("BMW")
obj.set_model("xyz")
obj.set_year(2000)
obj.display()