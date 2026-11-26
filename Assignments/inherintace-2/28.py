# 28. Transport Ticket Pricing
# Problem Statement

# Transport fares differ.

# Create:

# Bus
# Train
# Flight


from abc import ABC, abstractmethod

class Transport(ABC):

    def __init__(self, passenger_name, distance):
        self.__passenger_name = passenger_name
        self.__distance = distance

    def get_name(self):
        return self.__passenger_name

    def get_distance(self):
        return self.__distance

    @abstractmethod
    def calculate_fare(self):
        pass

    def display_details(self):
        print("Passenger Name:", self.__passenger_name)
        print("Distance:", self.__distance, "KM")


class Bus(Transport):

    def calculate_fare(self):
        fare = self.get_distance() * 2
        print("Bus Ticket Fare:", fare)


class Train(Transport):

    def calculate_fare(self):
        fare = self.get_distance() * 1.5
        print("Train Ticket Fare:", fare)


class Flight(Transport):

    def calculate_fare(self):
        fare = self.get_distance() * 8
        print("Flight Ticket Fare:", fare)


b = Bus("Rahul", 100)
t = Train("Amit", 100)
f = Flight("Raj", 100)

b.display_details()
b.calculate_fare()

t.display_details()
t.calculate_fare()

f.display_details()
f.calculate_fare()