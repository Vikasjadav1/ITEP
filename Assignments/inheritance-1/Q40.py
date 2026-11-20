'''
40. AI Chatbot System

Methods:

reply()

Implement:

SupportBot
SalesBot
'''

from abc import ABC,abstractmethod
class Chatbot_System(ABC):
    @abstractmethod
    def reply(self):
        pass

class SupportBot(Chatbot_System):
    def reply(self):
        print("hi vikas i am supperBot how can i assit you.....")

class SalesBot(Chatbot_System):
    def reply(self):
        print("hi vikas i am SalesBot how can i assit you.....")

obj=SupportBot()
obj.reply()

print("................................................")

obj=SalesBot()
obj.reply()