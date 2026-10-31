'''
Write a Java program to create a class called "Airplane" with a flight number, destination, and 
departure time attributes, and methods to check flight status and delay.
'''
from datetime import datetime, timedelta

class Airplane:

    def __init__(self, flight_number, destination, departure_time):
        self.flight_number = flight_number
        self.destination = destination
        self.departure_time = datetime.strptime(departure_time, "%H:%M")
        self.status = "On Time"

    def check_status(self):
        print(f"Flight Number: {self.flight_number}")
        print(f"Destination: {self.destination}")
        print(f"Departure Time: {self.departure_time.strftime('%I:%M %p')}")
        print(f"Flight Status: {self.status}")

    def delay(self, minutes):
        self.departure_time += timedelta(minutes=minutes)
        self.status = "Delayed"
        print(f"Flight delayed by {minutes} minutes")


flight1 = Airplane("AI101", "Delhi", "10:30")
flight1.check_status()
print("\nAfter Delay")
flight1.delay(45)
flight1.check_status()