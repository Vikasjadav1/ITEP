'''
 Write a Java program to create a class called "Bank" with a collection of accounts and methods to add and remove accounts, 
 and to deposit and withdraw money. Also define a class called "Account" to maintain account details of a particular customer.
 '''

class Account:
    accounts=[]

    def set_account(self,acc_no,cust_name,balance):
        self.__acc_no=acc_no
        self.__cust_name=cust_name
        self.__balance=balance

        Account.accounts.append(self)

acc1=Account()
acc2=Account()
acc1.set_account(1146549184,"vikas",200212)
acc2.set_account(1787987498,"jp",588)
print(Account.accounts)


    
    