'''
35. Messaging Application

Methods:

send_message()

Implement:

WhatsApp
Telegram
Signal
'''

from abc import ABC,abstractmethod
class Messaging(ABC):
    @abstractmethod
    def send_message(self):
        pass

class WhatsApp(Messaging):
    def send_message(self):
        print("message send using whatsapp.....")

class Telegram(Messaging):
    def send_message(self):
        print("message send using Telegram.....")

class Signal(Messaging):
    def send_message(self):
        print("message send using Signal.....")

obj=WhatsApp()
obj.send_message()
print(".............")

obj=Telegram()
obj.send_message()
print(".............")

obj=Signal()
obj.send_message()
print(".............")
 