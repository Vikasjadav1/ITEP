'''
Write a Java program to create a class called "Shape" with abstract methods
 for calculating area and perimeter, and subclasses for "Rectangle", "Circle", and "Triangle".
'''
from abc import ABC,abstractmethod
class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self,length,width):
        self.__length=length
        self.__width=width

    def area(self):
        print(f"area of rectangle {self.__length*self.__width}")
    
    def perimeter(self):
        print(f"perimeter of rectangle {2*(self.__length+self.__width)}")

class Circle(Shape):
    def __init__(self,radius):
        self.__radius=radius

    def area(self):
        print(f"area of circle {3.14*(self.__radius**2)}")

    def perimeter(self):
        print(f"perimter of circle {2*3.14*self.__radius}")

class Traingle(Shape):
    def __init__(self,a,b,c,heigth):
        self.__a=a
        self.__b=b
        self.__c=c
        self.__heigth=heigth

    def area(self):
        print(f"area of traingle {1/2*(self.__b*self.__heigth)}")

    def perimeter(self):
        print(f"perimter of traingle {self.__a+self.__b+self.__c}")


# obj=Rectangle(5,10)
# obj.area()
# obj.perimeter()

# obj=Circle(5)
# obj.area()
# obj.perimeter()

# obj=Traingle(5,5,5,5)
# obj.area()
# obj.perimeter()



