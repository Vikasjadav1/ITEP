'''
4. Restaurant Billing System
Beginner–Intermediate
Concepts: Loops, conditions, functions
Requirements
•	Display a menu with item prices.
•	Let customers select items and quantities.
•	Calculate the running bill.
•	Apply discounts based on the bill amount.
•	Calculate the final bill, including tax.
Bonus: Add coupon codes and repeat-order functionality.

'''

print("========= MENU =========")
print("1. Pizza       - ₹200")
print("2. Burger      - ₹100")
print("3. Sandwich    - ₹80")
print("4. Coffee      - ₹50")
print("5. Exit             ")
print("========================")

total_bill=0
gst=0
def bill_cal(item,quantity):
    global total_bill
    if item==1:
        current_bill=200*quantity
        total_bill+=current_bill
        return total_bill
    elif item==2:
        current_bill=100*quantity
        total_bill+=current_bill
        return total_bill
    elif item==3:
        current_bill=80*quantity
        total_bill+=current_bill
        return total_bill
    elif item==4:
        current_bill=50*quantity
        total_bill+=current_bill
        return total_bill

def discount_cal(total_bill):
    if total_bill > 2000:
        discount = 400
    elif total_bill > 1000:
        discount = 200
    else:
        discount = 0

    total_bill-=discount
    return total_bill,discount

def cal_gst(total_bill):
    gst=(total_bill*5)/100
    return gst

def coupon_cal(total_bill):
    coupon = input("Enter coupon code: ").upper()

    if coupon == "SAVE10":
        discount = total_bill * 10 / 100
    elif coupon == "FOOD50":
        discount = 50
    else:
        discount = 0
        print("Invalid coupon code")

    total_bill -= discount
    return total_bill, discount
    
    
while(True):
    item=int(input("enter item no...."))
    if item < 1 or item > 5:
        print("Item is not available")
        break
    else:
        if item==5:
            print(f"Total bill : {total_bill}")
            break
    quantity=int(input("enter item quantity...."))
    total_bill=bill_cal(item,quantity)

    choice = input("Do you want to order more? (yes/no): ").lower()

    if choice == "no":
        break
    
original_bill = total_bill

total_bill, discount = discount_cal(total_bill)

total_bill, coupon_discount = coupon_cal(total_bill)

gst = cal_gst(total_bill)
final_amount = total_bill + gst

print("\n===== FINAL BILL =====")
print("Original Bill:", original_bill)
print("Normal Discount:", discount)
print("Coupon Discount:", coupon_discount)
print("Bill after discounts:", total_bill)
print("GST:", gst)
print("Final Amount:", final_amount)




