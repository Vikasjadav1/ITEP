'''
3. ATM Banking Simulator
Beginner–Intermediate
Concepts: Nested conditions, loops, functions
Requirements
•	Verify a PIN.
•	Display balance, deposit, withdrawal, and exit options.
•	Prevent withdrawals exceeding the available balance.
•	Reject invalid amounts.
•	Use separate functions for deposit, withdrawal, and balance enquiry.
Bonus: Allow only three PIN attempts.

'''

set_pin="123"
balance=10000

def check_pin(set_pin):
    check_pin=input("enter your pin:-")
    if set_pin==check_pin:
        return True
    else:
        return False

def deposit(deposit_amount):
    global balance
    if deposit_amount>0:
        balance+=deposit_amount
        print(f"{deposit_amount} Deposit successfull :.....")
        print(f"current balance :- {balance}")
    else:
        print("Invalid")

def withdraw(withdraw_amount):
    global balance
    if balance>=withdraw_amount:
        balance-=withdraw_amount
        print(f"{withdraw_amount} withdraw successfull :.....")
        print(f"current balance :- {balance}")
    else:
        print("insufficient balance...........")

def balance_enquiry():
    print(f"current balance :- {balance}")

for i in range(3,0,-1):
    if (check_pin(set_pin)):
        print("1.Deposit")
        print("2.Withdraw")
        print("3.Balance enquiry")
        print("4.Exit")

        choice=int(input("enter option : "))

        if(choice==1):
            amount=int(input("enter deposit amount :-"))
            deposit(amount)
        elif(choice==2):
            amount=int(input("enter withdraw amount :-"))
            withdraw(amount)
        elif(choice==3):
            balance_enquiry()
        elif(choice==4):
            break
        else:
            print("Transection failed")
        break
    else:
        if i!=1:
            print(f"{i-1} chance reamaning.........")

