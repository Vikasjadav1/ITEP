'''
42. E-Commerce Order Processing

Implement:

products
orders
payment methods
delivery system
'''

from abc import ABC,abstractmethod
class Payment(ABC):
    @abstractmethod
    def payment(self):
        pass

class Products:
    products = []

    def __init__(self, id, name, price):
        self.__id = id
        self.__name = name
        self.__price = price
        Products.products.append(self)

    def get_details(self):
        return self.__id, self.__name, self.__price

    @classmethod
    def available_product(cls):
        for product in cls.products:
            print(f"ID: {product.__id} | "
                  f"Name: {product.__name} | "
                  f"Price: Rs.{product.__price}")

class Order:
    def __init__(self, product_id, quantity):
        self.__product_id = product_id
        self.__quantity = quantity
        self.__total_amount = 0

    def place_order(self):
        for product in Products.products:
            if product._Products__id == self.__product_id:
                self.__total_amount = product._Products__price * self.__quantity

                print("----- ORDER DETAILS -----")
                print("Product:", product._Products__name)
                print("Quantity:", self.__quantity)
                print("Total Amount:", self.__total_amount)
                print("Order placed successfully!")
                return self.__total_amount

        print("Product not found!")

class UPIPayment(Payment):

    def payment(self, amount):
        print(f"Payment of Rs.{amount} through UPI successful!")


class CardPayment(Payment):

    def payment(self, amount):
        print(f"Payment of Rs.{amount} through Credit Card successful!")


class CODPayment(Payment):

    def payment(self, amount):
        print(f"Cash on Delivery selected.")
        print(f"Amount to pay: Rs.{amount}")


class Delivery:

    def __init__(self, tracking_id, delivery_partner):
        self.tracking_id = tracking_id
        self.delivery_partner = delivery_partner
        self.status = "Order Confirmed"

    def delivery_details(self):
        print("\n----- DELIVERY DETAILS -----")
        print("Tracking ID:", self.tracking_id)
        print("Delivery Partner:", self.delivery_partner)
        print("Delivery Status:", self.status)

p1 = Products(101, "Laptop", 50000)
p2 = Products(102, "Mobile", 20000)
p3 = Products(103, "Headphones", 2000)

Products.available_product()

product_id = int(input("\nEnter Product ID: "))
quantity = int(input("Enter Quantity: "))

obj = Order(product_id, quantity)
amount = obj.place_order()

if amount is not None:

    print("\n----- PAYMENT METHODS -----")
    print("1. UPI")
    print("2. Credit Card")
    print("3. Cash on Delivery")

    choice = int(input("Select Payment Method: "))

    if choice == 1:
        payment_obj = UPIPayment()

    elif choice == 2:
        payment_obj = CardPayment()

    elif choice == 3:
        payment_obj = CODPayment()

    else:
        payment_obj = None
        print("Invalid payment method!")

    if payment_obj:
        payment_obj.payment(amount)

        delivery = Delivery("ORD101", "Rahul")
        delivery.delivery_details()
