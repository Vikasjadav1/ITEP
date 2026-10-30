'''
Create a class Rectangle with fields: length, width.
Use setters to assign values. Add a method to calculate area.
'''

class Rectangle:
    def set_value(self,length,width):
        self.__length=length
        self.__width=width
    
    def area(self):
        print(f"area of rectangle {self.__length*self.__width}")

obj=Rectangle()
obj.set_value(5,5)
obj.area()