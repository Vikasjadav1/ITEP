'''
31. Drawable Interface

Interface:

draw()

Implement:

Circle
Rectangle
Line
'''

from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass

class Circle(Shape):
    def draw(self):
        print("circle is drawing ..........")

class Rectangle(Shape):
    def draw(self):
        print("rectangle is drawing ..........")

class Line(Shape):
    def draw(self):
        print("line is drawing ..........")


obj=Circle()
obj.draw()
print("........................")
obj=Rectangle()
obj.draw()
print("........................")
obj=Line()
obj.draw()
print("........................")