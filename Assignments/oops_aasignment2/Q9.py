class ATM:
    def __init__(self,account_no,pin,balance):
        self.__account_no=account_no
        self.__pin=pin
        self.__balance=balance

    def login_verification(self):
        chance=3
        while(chance>0):
            password=int(input("enter pin : "))
            if self.__pin != password:
                print("incorrect pin...")
                chance-=1
                print(f"{chance} reamaning.....")
                
            else:
                print("pin **** matched ********.......")
                break

        if chance==0:
            print("account bloced try again after 24 hours..........")

    def deposit(self,amount):
        if amount<=0:
            print("invalid amount.....")
        else:
            self.__balance+=amount
            print(f"{amount} deposit succuessfull ........")

    def withdraw(self,amount):
        if amount<=0:
            print("invalid amount...")
        elif amount>self.__balance:
            print("insufficient balance.........")
        else:
            self.__balance-=amount
            print(f"{amount} withdraw successfull")


    def display(self):
        print(f"account number : {self.__account_no}")
        print(f"balance : {self.__balance}")

acc1=ATM(841681498,1234,50000)
# acc1.deposit(8)
# acc1.withdraw(88)
# acc1.display()
acc1.login_verification()
