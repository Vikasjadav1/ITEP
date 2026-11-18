'''
23. Notification System

Abstract:

Notification

Derived:

EmailNotification
SMSNotification
PushNotification

'''

from abc import ABC,abstractmethod
class Notification(ABC):
    @abstractmethod
    def notification(self):
        pass

class EmailNotification(Notification):
    def notification(self):
        print("email notification.....")

class SMSNotification(Notification):
    def notification(self):
        print("sms notification.....")

class PushNotification(Notification):
    def notification(self):
        print("push notification.....")

obj=EmailNotification()
obj.notification()
print("...........................................")
obj=SMSNotification()
obj.notification()
print(".............................................")
obj=PushNotification()
obj.notification()