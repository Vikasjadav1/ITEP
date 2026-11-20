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

