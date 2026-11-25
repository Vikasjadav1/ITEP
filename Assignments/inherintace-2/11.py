'''
11. Shape Drawing Application
Problem Statement

A drawing app supports multiple shapes.

Create abstract class Shape.

Child:

Circle
Rectangle
Triangle

Each implements:

draw()
area()
'''
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def draw(self):
     for i in range(6):
        for j in range(6):
            if i == 0 or j == 0 or i == 5 or j == 5:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
           
    def area(self):
        radius=float(input("enter radius.."))
        print(f"area of circle : {3.14*radius*radius}")

class Rectangle(Shape):
    def draw(self):
     for i in range(6):
        for j in range(10):
            if i == 0 or i == 5 or j == 0 or j == 9:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
           
    def area(self):
        length=int(input("enter length :"))
        width=int(input("enter width :"))
        print(f"area of rectangle : {3.14*length*width}")


class Traingle(Shape):
    def draw(self):
     for i in range(6):
        for j in range(11):
            if j == 5-i or j == 5+i or i == 5:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
           
    def area(self):
        length=int(input("enter length :"))
        width=int(input("enter width :"))
        base=int(input("enter base : "))
        print(f"area of circle : {0.5*base*length*width}")

obj=Circle()
obj.draw()
obj.area()

print("''''''''''''''''''''''''''''''")

obj=Rectangle()
obj.draw()
obj.area()


print("''''''''''''''''''''''''''''''")

obj=Traingle()
obj.draw()
obj.area()