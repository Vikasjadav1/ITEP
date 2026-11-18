'''
5. Banking System

Parent:

BankAccount

Child:

SavingsAccount
CurrentAccount

Implement withdrawal rules.
'''


from abc import ABC,abstractmethod
class BankAccount(ABC):
    @abstractmethod
    def withdraw_rules(self):
       pass

class SavingsAccount(BankAccount):
    def withdraw_rules(self):
        print("Withdrawal Rules for Savings Account:")
        print("1. Minimum balance of Rs. 1000 must be maintained.")
        print("2. Withdrawal amount must be greater than zero.")
        print("3. Withdrawal is allowed only if sufficient balance is available.")
        print("4. Balance must not go below Rs. 1000 after withdrawal.")
        print("5. If any rule is violated, withdrawal will be rejected.")


class CurrentAccount(BankAccount):
    def withdraw_rules(self):
        print("Withdrawal Rules for Current Account:")
        print("1. No minimum balance is required.")
        print("2. Withdrawal amount must be greater than zero.")
        print("3. Overdraft facility is available up to Rs. 5000.")
        print("4. Account balance can become negative up to Rs. -5000.")
        print("5. Withdrawal will be rejected if the overdraft limit is exceeded.")
        print("6. If any rule is violated, withdrawal will be rejected.")

obj=SavingsAccount()
obj.withdraw_rules()

print("***************************************************************")

obj=CurrentAccount()
obj.withdraw_rules()