'''
50. Cryptocurrency Wallet System

Features:

wallet
transactions
deposits
withdrawals

Implement secure transaction architecture.
'''
class Wallet:

    def __init__(self, owner):
        self.owner = owner
        self.balance = 0
        self.transactions = []

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid amount!")
        else:
            self.balance += amount
            self.transactions.append("Deposited: " + str(amount))
            print("Deposit successful!")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid amount!")
        elif amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            self.transactions.append("Withdrawn: " + str(amount))
            print("Withdrawal successful!")

    def show_balance(self):
        print("Wallet Balance:", self.balance)

    def show_transactions(self):
        print("\nTransaction History:")
        for transaction in self.transactions:
            print(transaction)

wallet = Wallet("Vikas")

wallet.deposit(5000)
wallet.deposit(2000)

wallet.withdraw(1000)
wallet.withdraw(10000)

wallet.show_balance()
wallet.show_transactions()
