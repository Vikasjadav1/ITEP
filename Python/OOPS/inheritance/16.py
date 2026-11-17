from abc import ABC,abstractmethod

class Makepayment(ABC):
    @abstractmethod
    def payment(self):
        pass

class NetBanking(Makepayment):
    def payment(self,payment):
        print(f"payment using netbanking : {payment}")

class UPI(Makepayment):
    def payment(self,payment):
        print(f"payment using upi : {payment}")

class CreditCard(Makepayment):
    def payment(self,payment):
        print(f"payment using credit card  : {payment}")

print("1 for using NetBanking")
print("2 for using UPI")
print("3 for credit card")

choice=int(input("enter choice.."))

pay=None
if choice==1:
    pay=NetBanking()
elif choice==2:
    pay=UPI()
elif choice==3:
    pay=CreditCard()

pay.payment(200000)

