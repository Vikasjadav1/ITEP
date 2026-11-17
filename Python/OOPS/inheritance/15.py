from abc import ABC,abstractmethod
#developer level
class Shape(ABC):
    @abstractmethod
    def get_area(self):
        pass

#programmer level

class Circle(Shape):
    def get_area(self):
        radius=float(input("enter radius.."))
        print(f"circle area : {3.14*radius*radius}")


class Rectangle(Shape):
    def get_area(self):
        l=float(input("enter length.."))
        w=float(input("enter width.."))
        print(f"rectangle area : {l*w}")

class Traingle(Shape):
    def get_area(self):
        b=float(input("enter base.."))
        h=float(input("enter heigth.."))
        print(f"traingle area : {0.5*b*h}")

# s=None
print("1 for circle")
print("2 for rectangle")
print("3 for traingle")
choice=int(input("enter choice.."))

if choice==1:
    s=Circle()
elif choice==2:
    s=Rectangle()
elif choice==3:
    s=Traingle()

s.get_area()

