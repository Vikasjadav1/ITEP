'''
Create a class Circle with field radius.
Use a setter to assign radius. Add methods to compute area and circumference.

'''

class Circle:
    def set_radius(self,radius):
        self.__radius=radius
    
    def calculation(self):
        print(f"area {3.14*(self.__radius**2)}")
        print(f"circumference {2*3.14*self.__radius}")

obj=Circle()
obj.set_radius(5)
obj.calculation()
