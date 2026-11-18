'''
18. Vehicle Insurance System
Vehicle
InsuredVehicle
Car

Calculate insurance amount.
'''
class Vehicle:
    def __init__(self,name,price):
        self.name = name
        self.price = price

    def vehicle_details(self):
        print("Vehicle Name:", self.name)
        print("Vehicle Price:", self.price)

class InsuredVehicle(Vehicle):
    def __init__(self,name,price,rate):
        super().__init__(name,price)
        self.rate=rate

    def insurance_amount(self):
        return self.price * self.rate / 100      


class Car(InsuredVehicle):
    def __init__(self, name, price, rate, model):
        super().__init__(name, price, rate)
        self.model = model

    def car_model(self):
        print("Car Model:", self.model)
        print("Insurance Amount:", self.insurance_amount())

obj = Car("Tata", 800000, 5, "Nexon")

obj.vehicle_details()
obj.car_model()