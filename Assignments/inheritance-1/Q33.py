'''
33. Smart Home Devices

Methods:

turn_on()
turn_off()

Implement:

SmartFan
SmartLight
SmartAC
'''
from abc import ABC,abstractmethod
class Devices(ABC):
    @abstractmethod
    def turn_on(self):
        pass
    @abstractmethod
    def turn_off(self):
        pass

class SmartFan(Devices):
    def turn_on(self):
        print("smart fan turn on .....")
    
    def turn_off(self):
        print("smart fan turn off ............")

class SmartLight(Devices):
    def turn_on(self):
        print("smart light turn on .....")
    
    def turn_off(self):
        print("smart light turn off ............")

class SmartAC(Devices):
    def turn_on(self):
        print("smart ac turn on .....")
    
    def turn_off(self):
        print("smart ac turn off ............")

obj=SmartFan()
obj.turn_on()
obj.turn_off()
print(".............")

obj=SmartLight()
obj.turn_on()
obj.turn_off()
print(".............")

obj=SmartAC()
obj.turn_on()
obj.turn_off()
print(".............")