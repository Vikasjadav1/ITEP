'''
28. Authentication System

Abstract:

Authentication

Derived:

OTPAuth
GoogleAuth
FacebookAuth
'''
from abc import ABC,abstractmethod
class Authentication(ABC):
    @abstractmethod
    def login(self):
        pass

class OTPAuth(Authentication):
    def login(self):
        print("logined using otp.............")

class GoogleAuth(Authentication):
    def login(self):
        print("logined using googel auth............")

class FacebookAuth(Authentication):
    def login(self):
        print("signed using facebook auth..........")

obj1=OTPAuth()
obj1.login()
print(".....................")
obj1=GoogleAuth()
obj1.login()
print(".....................")
obj1=FacebookAuth()
obj1.login()