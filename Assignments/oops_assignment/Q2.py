'''
Create a class BankAccount with fields: accountNumber, holderName, balance.
Use setters to assign values. Add a method to display balance.'''

class BankAccount:
    def set_accountNumber(self,acnum):
        self.__acnum=acnum

    def set_holderName(self,holder_name):
        self.__holder_name=holder_name
    
    def set_balance(self,balance):
        self.__balance=balance
    
    def display(self):
        print(f"account number {self.__acnum}")
        print(f"holder name {self.__holder_name}")
        print(f"balance {self.__balance}")

obj=BankAccount()
obj.set_accountNumber(12848586985488)
obj.set_holderName("vikas")
obj.set_balance(54894)
obj.display()