'''
39. Navigation System

Methods:

navigate()

Implement:

GoogleMaps
AppleMaps
'''

from abc import ABC,abstractmethod
class Navigation_System(ABC):
    @abstractmethod
    def navigate(self):
        pass

class GoogleMaps(Navigation_System):
    def navigate(self):
        print("navigate on googelmap............")

class AppleMaps(Navigation_System):
    def navigate(self):
        print("navigate on AppleMaps............")

obj=GoogleMaps()
obj.navigate()
print("........................................")
obj=AppleMaps()
obj.navigate()