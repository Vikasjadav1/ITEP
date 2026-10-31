'''
Write a Java program to create a class called "Rectangle" with width and height attributes. Calculate the area and perimeter of the rectangle.
'''

class Rectangle:
    def __init__(self,height,width):
        self.__heigth=height
        self.__width=width

    def area(self):
        print(f"area of rectangle :{self.__heigth*self.__width}")
        
    
    def perimeter(self):
        print(f"perimeter of rectangle : {2*(self.__heigth+self.__width)}")

obj=Rectangle(5,5)
obj.area()
obj.perimeter()
