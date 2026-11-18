'''
1. Animal Sound System

Create parent class Animal and child classes:

Dog
Cat
Cow

Override sound() method.
'''

from abc import ABC,abstractmethod
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        print("Dog sound...")

class Cat(Animal):
    def sound(self):
        print("Cat sound...")

class Cow(Animal):
    def sound(self):
        print("Cow sound...")

obj=Dog()
obj.sound()
obj=Cow()
obj.sound()