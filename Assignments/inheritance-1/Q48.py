'''
48. Inventory Management System

Features:

stock
suppliers
billing
'''
class Inventory:
    def __init__(self):
        self.stock = {}
        self.suppliers = {}
        
    def add_product(self, product_id, name, price, quantity):
        self.stock[product_id] = {
            "name": name,
            "price": price,
            "quantity": quantity
        }
        print("Product added successfully!")

    def add_supplier(self, supplier_id, name, phone):
        self.suppliers[supplier_id] = {
            "name": name,
            "phone": phone
        }
        print("Supplier added successfully!")

    def show_stock(self):
        print("\nAvailable Stock:")
        for product_id, details in self.stock.items():
            print(product_id, details)

    def generate_bill(self, product_id, quantity):
        if product_id not in self.stock:
            print("Product not found!")
            return

        product = self.stock[product_id]

        if quantity > product["quantity"]:
            print("Insufficient stock!")
        else:
            total = product["price"] * quantity
            product["quantity"] -= quantity

            print("\n----- BILL -----")
            print("Product:", product["name"])
            print("Quantity:", quantity)
            print("Price:", product["price"])
            print("Total Amount:", total)
            print("----------------")
            print("Bill generated successfully!")

    def show_suppliers(self):
        print("\nSupplier Details:")
        for supplier_id, details in self.suppliers.items():
            print(supplier_id, details)


inventory = Inventory()

inventory.add_product(101, "Laptop", 50000, 10)
inventory.add_product(102, "Mouse", 500, 20)
inventory.add_product(103, "Keyboard", 1000, 15)

inventory.add_supplier(1, "Amit Traders", "9876543210")
inventory.add_supplier(2, "Tech Solutions", "9876501234")

inventory.show_stock()


inventory.show_suppliers()

inventory.generate_bill(101, 2)
inventory.generate_bill(102, 3)

inventory.show_stock()
