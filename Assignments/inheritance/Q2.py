from abc import ABC,abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass
    
class Car(Vehicle):
    def start(self):
        print("Car start...")
    
    def stop(self):
        print("Car stop...")

class Bike(Vehicle):
    def start(self):
        print("Bike start...")
    
    def stop(self):
        print("Bike stop...")

class Bus(Vehicle):
    def start(self):
        print("Bus start...")
    
    def stop(self):
        print("Bus stop...")

obj=Car()
obj.start()
obj.stop()

obj=Bike()
obj.start()
obj.stop()

obj=Bus()
obj.start()
obj.stop()