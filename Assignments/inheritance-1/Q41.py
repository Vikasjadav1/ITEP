'''
41. Cab Booking Application

Features:

User booking
Driver assignment
Fare calculation

Use:

inheritance
abstraction
polymorphism
'''

from abc import ABC,abstractmethod
class Cab_Booking (ABC):
    @abstractmethod
    def book_cab(self):
        pass

    @abstractmethod
    def assign_driver(self):
        pass

    @abstractmethod 
    def fare(self):
        pass


class User_Details:
    def __init__(self,name,pickup,destination,km):
        self.__name=name
        self.__pickup=pickup
        self.__destination=destination
        self.__km=km

    def user_details(self):
        print(f"user name : {self.__name}")
        print(f"pickup : {self.__pickup}")
        print(f"destination : {self.__destination}")
        print(f"km : {self.__km}")

    def get_km(self):
        return self.__km

class MiniCab(User_Details,Cab_Booking):
    def book_cab(self):
        print("mini cab booked...........")

    def assign_driver(self):
        print("driver assigned............")

    def fare(self):
        print(f"fare : {10*self.get_km()}")

class SedanCab(User_Details,Cab_Booking):
    def book_cab(self):
        print("sedan cab booked...........")

    def assign_driver(self):
        print("driver assigned............")

    def fare(self):
        print(f"fare : {15*self.get_km()}")


class SUV_Cab(User_Details,Cab_Booking):
    def book_cab(self):
        print("SUV cab booked...........")

    def assign_driver(self):
        print("driver assigned............")

    def fare(self):
        print(f"fare : {20*self.get_km()}")


obj=None
print("select cab")
print("1 mini cab")
print("2 Sedan")
print("3 SUV")

choice=int(input("enter choice : "))

if choice==1:
    obj=MiniCab("vikas","ujjain","indore",55)
elif choice==2:
    obj=SedanCab("vikas", "ujjain", "indore", 55)
elif choice==3:
    obj=SUV_Cab("vikas", "ujjain", "indore", 55)

obj.user_details()
obj.book_cab()
obj.assign_driver()
obj.fare()
