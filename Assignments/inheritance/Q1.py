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