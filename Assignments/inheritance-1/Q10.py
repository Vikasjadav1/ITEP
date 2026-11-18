'''
10. Movie Ticket Booking

Parent:

Ticket

Derived:

GoldTicket
PlatinumTicket
VIPTicket

Apply pricing logic.
'''

from abc import ABC,abstractmethod
class Ticket(ABC):
    @abstractmethod
    def pricing(self):
        pass

class GoldTicket(Ticket):
    def pricing(self,quantity):
        price=550
        if quantity<=0:
            print("invalid quantity......")
        elif quantity==1:
            print(f"price : {price}")
        elif quantity>1:
            price=price-(price*20/100)
            print(f"price after 20 % discount : {price}")



class PlatinumTicket(Ticket):
    def pricing(self,quantity):
        price=750
        if quantity<=0:
            print("invalid quantity......")
        elif quantity==1:
            print(f"price : {price}")
        elif quantity>1:
            price=price-(price*30/100)
            print(f"price after 30 % discount : {price}")

class VIPTicket(Ticket):
    def pricing(self,quantity):
        price=1050
        if quantity<=0:
            print("invalid quantity......")
        elif quantity==1:
            print(f"price : {price}")
        elif quantity>1:
            price=price-(price*35/100)
            print(f"price after 35 % discount : {price}")


print("1 GoldTicket price 550 discount 20 on more than 1 ticket")
print("2 PlatinumTicket price 750 discount 30 on more than 1 ticket")
print("3 VIPTicket price 1050 discount 35 on more than 1 ticket")
choice=int(input("enter choice..."))
obj=None

if choice==1:
    obj=GoldTicket()
elif choice==2:
    obj=PlatinumTicket()
elif choice==3:
    obj=VIPTicket()

obj.pricing(2)