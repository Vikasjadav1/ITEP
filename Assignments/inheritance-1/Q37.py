'''
37. Social Login System

Methods:

login()

Implement:

GoogleLogin
GitHubLogin
LinkedInLogin
'''

from abc import ABC,abstractmethod
class Login_System(ABC):
    @abstractmethod
    def login(self):
        pass


class GoogleLogin(Login_System):
    def login(self):
        print("login successfull using google.....")

class GitHubLogin(Login_System):
    def login(self):
        print("login successfull using github.....")

class LinkedInLogin(Login_System):
    def login(self):
        print("login successfull using linkedin.....")


obj=GoogleLogin()
obj.login()
print(".......................................................")
obj=GitHubLogin()
obj.login()
print(".......................................................")
obj=LinkedInLogin()
obj.login()