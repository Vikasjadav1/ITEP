'''
Write a Java program to create a class called "Circle" with a radius attribute. You can access and modify this attribute. Calculate the area and circumference of the circle.
'''
from math import pi

class Circle:
    def __init__(self,radius):
        self.__radius=radius

    def get_radius(self):
        return self.__radius

    def set_radius(self):
        self.__radius=int(input("enter radius : "))

    def area(self):
        print(f"area of circle : {pi*(self.__radius**2)}")

obj=Circle(5)
radius=obj.get_radius()

print(radius)
obj.area()

obj.set_radius()
print(radius)
obj.area()



    
