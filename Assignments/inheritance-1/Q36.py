'''
36. Payment Interface

Methods:

pay()

Implement:

PayPal
Stripe
Razorpay
'''
from abc import ABC,abstractmethod
class Payment(ABC):
    @abstractmethod
    def pay(self):
        pass

class PayPal(Payment):
    def pay(self):
        print("payment successfull using paypal..........")

class Stripe(Payment):
    def pay(self):
        print("payment successfull using stripe.........")

class Razorpay(Payment):
    def pay(self):
        print("payment successfull using rozorpay.........")


obj=PayPal()
obj.pay()
print("........*********************.........")

obj=Stripe()
obj.pay()
print("........*********************.........")

obj=Razorpay()
obj.pay()
