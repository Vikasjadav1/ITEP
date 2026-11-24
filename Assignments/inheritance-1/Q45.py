
'''
45. Food Ordering Application

Implement:
Menu
Orders
Payment
Discounts
'''

class Menu:
    menu = []

    def __init__(self, name, price):
        self.__name = name
        self.__price = price
        Menu.menu.append(self)

    @classmethod
    def display_menu(cls):
        print("\n----- MENU -----")
        for item in cls.menu:
            print(f"{item.__name} : Price {item.__price}")


class Order:
    orders = []

    def add_order(self, item_name, quantity):
        if quantity <= 0:
            print("Invalid quantity!")
            return

        for item in Menu.menu:
            if item._Menu__name == item_name:
                total = item._Menu__price * quantity
                self.orders.append([item_name, quantity, total])
                print("Order added successfully...")
                return

        print("Item not found!")

    def display_order(self):
        print("\n----- YOUR ORDER -----")
        for item in self.orders:
            print(item[0], "Quantity:", item[1], "Price:", item[2])

    def calculate_total(self):
        total = 0

        for item in self.orders:
            total += item[2]

        return total


class Discount:
    def __init__(self, amount, percentage):
        self.amount = amount
        self.percentage = percentage

    def apply_discount(self):
        if self.percentage < 0 or self.percentage > 100:
            print("Invalid discount!")
            return self.amount

        discount = self.amount * self.percentage / 100
        final_amount = self.amount - discount

        print("\n----- DISCOUNT DETAILS -----")
        print("Original Amount:", self.amount)
        print("Discount:", discount)
        print("Final Amount:", final_amount)

        return final_amount


class Payment:
    def __init__(self, amount, method):
        self.amount = amount
        self.method = method

    def make_payment(self):
        if self.amount <= 0:
            print("Invalid payment amount!")
            return

        print("\n----- PAYMENT DETAILS -----")
        print("Amount:", self.amount)
        print("Payment Method:", self.method)
        print("Payment Successful!")


item1 = Menu("pizza", 500)
item2 = Menu("burger", 250)
item3 = Menu("choclate", 100)

Menu.display_menu()

obj = Order()

obj.add_order("pizza", 2)
obj.add_order("burger", 1)

obj.display_order()

total = obj.calculate_total()

discount = Discount(total, 10)
final_amount = discount.apply_discount()

payment = Payment(final_amount, "UPI")
payment.make_payment()
