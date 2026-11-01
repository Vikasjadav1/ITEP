'''
 Write a Java program to create a class called "Restaurant" 
 with attributes for menu items, prices, and ratings, and methods to add and remove items, 
 and to calculate average rating.
 '''

class Restaurant:
    def __init__(self):
        self.__items=[]
        self.__prices=[]
        self.__ratings=[]

    def add_item(self,item,price):
        if item not in self.__items:
            self.__items.append(item)
            self.__prices.append(price)

            print(f"...........item menu..............")
            for i in range(len(self.__items)):
                print(f"item {self.__items[i]} price {self.__prices[i]}")
        else:
            print(f"{item} already exist.........")
    
    def remove_item(self,item):
        if item in self.__items:
            index = self.__items.index(item)
            self.__items.pop(index)
            self.__prices.pop(index)
            print(f"{item} removed")
        else:
            print("item not exist")

obj=Restaurant()
obj.add_item("pizza",100)
obj.add_item("burger",50)
obj.add_item("choclate",50)

obj.remove_item("choclate")
obj.add_item("cophy",80)

