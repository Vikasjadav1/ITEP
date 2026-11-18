'''
21. Shape Area Calculator

Abstract class Shape.

Derived:

Circle
Rectangle
Triangle

Implement area calculation.
'''

from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def area(self):
        radius=int(input("enter radius : "))
        print(f"area of circle : {3.14*radius*radius}")

class Rectangle(Shape):
    def area(self):
        length=int(input("enter legnth :"))
        width=int(input("enter width :"))
        print(f"area of rectangle : {length*width}")

class Traingle(Shape):
    def area(self):
        base=int(input("enter base :"))
        heigth=int(input("enter heigth :"))
        print(f"area of traingle : {0.5*base*heigth}")

obj=Circle()
obj.area()
print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
obj=Rectangle()
obj.area()
print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
obj=Traingle()
obj.area()