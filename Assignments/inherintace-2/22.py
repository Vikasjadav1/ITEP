'''
22. Notification Service
Problem Statement

Application sends notifications differently.

Create:

abstract class Notification

Child:

EmailNotification
SMSNotification
PushNotification
'''

from abc import ABC,abstractmethod

class Notification(ABC):
    @abstractmethod
    def send_notification(self):
        pass

class EmailNotification(Notification):
    def send_notification(self):
        email = input("Enter email address: ")
        message = input("Enter message: ")
        print("Email sent successfully to:", email)
        print("Message:", message)

class SMSNotification(Notification):
    def send_notification(self):
        mobile = input("Enter mobile number: ")
        message = input("Enter message: ")
        print("SMS sent successfully to:", mobile)
        print("Message:", message)


class PushNotification(Notification):
    def send_notification(self):
        device = input("Enter device name: ")
        message = input("Enter message: ")
        print("Push notification sent to:", device)
        print("Message:", message)

print("1. Email Notification")
print("2. SMS Notification")
print("3. Push Notification")

choice = int(input("Enter your choice: "))

if choice == 1:
    obj = EmailNotification()

elif choice == 2:
    obj = SMSNotification()

elif choice == 3:
    obj = PushNotification()

else:
    print("Invalid choice")
    obj = None

if obj:
    obj.send_notification()