'''
6. Shopping Cart and Checkout
Intermediate
Concepts: Loops, conditions, functions, lists, dictionaries
Requirements
•	Store products and prices.
•	Allow customers to add items and quantities.
•	Calculate item-wise and total costs.
•	Apply discounts based on purchase value.
•	Generate a final bill.
Bonus: Implement removing an item and checking product availability.

'''
print("'''''''''''''''''''Menu'''''''''''''''''''")
print("1. Mouse            500RS")
print("2. Keyboard         800RS")
print("3. Headphone        1200RS")
print("4. USB              400RS")
print("5. Check Product Availability")
print("6. Remove Item")
print("7. Exit")


products={
    "Mouse":500,
    "Keyboard":800,
    "Headphone":1200,
    "USB":400
}

total_bill = 0

purchase_items=[]

def add_items():
    while(True):
        choose = int(input("Choose product: "))

        if choose == 7:
            break
        elif choose == 5:
            check_availability()
            continue
        elif choose == 6:
            remove_item()
            continue
        elif choose < 1 or choose > 7:
            print("Invalid choice")
            continue

        quantity = int(input("Quantity: "))

        if choose == 1:
            purchase_items.append({"Mouse": quantity})
        elif choose == 2:
            purchase_items.append({"Keyboard": quantity})
        elif choose == 3:
            purchase_items.append({"Headphone": quantity})
        elif choose == 4:
            purchase_items.append({"USB": quantity})

        ask = input("Do you want to purchase more? (yes/no): ")

        if ask.lower() == "no":
            break

def check_availability():
    name = input("Enter product name: ").title()

    if name in products:
        print("Available. Price:", products[name])
    else:
        print("Product not available")

def remove_item():
    name = input("Enter item to remove: ").title()

    for item in purchase_items:
        if name in item:
            purchase_items.remove(item)
            print("Item removed")
            return

    print("Item not found")

def discount(total_bill):
    if total_bill>5000:
        discount=(total_bill*10)/100
    elif total_bill>1000:
        discount=(total_bill*5)/100
    elif total_bill<=10000:
        discount=0
    
    return discount



def cal_price(purchase_items):
    global total_bill
    for item in purchase_items:
        for name,quantity in item.items():
            price=products[name]
            cost=price*quantity
            total_bill = total_bill + cost

        print(f"{name} | Quantity: {quantity} | Price: ₹{price} | Total: ₹{cost}")

    return total_bill

def display_bill(purchase_items, total_bill, discount_amount):
    print("\n========== FINAL BILL ==========")
    print("Item\t\tQty\tPrice\tTotal")


    final_bill = total_bill - discount_amount

    print("--------------------------------")
    print("Total Bill :", total_bill)
    print("Discount   :", discount_amount)
    print("Final Bill :", final_bill)
    print("================================")


add_items()
total_bill=cal_price(purchase_items)
discount_amount=discount(total_bill)
display_bill(purchase_items,total_bill,discount_amount)


    



    








