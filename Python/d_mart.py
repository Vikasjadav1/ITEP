cust_name=input("Enter Customer Name : ")
cust_gender=input("enter Customer Gender : ").lower()

item1=(input("Item1 : "))
item1_quantity=int(input("enter quantity of item1 : "))
item1_price=10
item1_total_price=item1_quantity*item1_price

item2=(input("Item2 : "))
item2_quantity=int(input("enter quantity of item2 : "))
item2_price=20
item2_total_price=item2_quantity*item2_price

item3=(input("Item3 : "))
item3_quantity=int(input("enter quantity of item3 : "))
item3_price=30
item3_total_price=item3_quantity*item3_price

item4=(input("Item4 : "))
item4_quantity=int(input("enter quantity of item4 : "))
item4_price=40
item4_total_price=item4_quantity*item4_price

item5=(input("Item5 : "))
item5_quantity=int(input("enter quantity of item5 : "))
item5_price=50
item5_total_price=item5_quantity*item5_price

item5_total_price_discount = item5_total_price - (item5_total_price * 0.10)


item6=(input("Item6 : "))
item6_quantity=int(input("enter quantity of item6 : "))
item6_price=60
item6_total_price=item6_quantity*item6_price

item7=(input("Item7 : "))
item7_quantity=int(input("enter quantity of item7 : "))
item7_price=70
item7_total_price=item7_quantity*item7_price

item8=(input("Item8 : "))
item8_quantity=int(input("enter quantity of item8 : "))
item8_price=80
item8_total_price=item8_quantity*item8_price

item9=(input("Item9 : "))
item9_quantity=int(input("enter quantity of item9 : "))
item9_price=90
item9_total_price=item9_quantity*item9_price

item10=(input("Item10 : "))
item10_quantity=int(input("enter quantity of item10 : "))
item10_price=100
item10_total_price=item10_quantity*item10_price

actual_price=item1_total_price + item2_total_price + item3_total_price + item4_total_price + item5_total_price + item6_total_price + item7_total_price + item8_total_price + item9_total_price + item10_total_price

item10_total_price_discount=item10_total_price-(item10_total_price*0.15)


item1_total_price_discount = item1_total_price




if item1_quantity>4:
    item1_total_price_discount=item1_total_price-(item1_total_price*0.05)

total_bill = item1_total_price_discount + item2_total_price + item3_total_price + item4_total_price + item5_total_price_discount + item6_total_price + item7_total_price + item8_total_price + item9_total_price + item10_total_price_discount


if total_bill > 10000:
	total_bill = total_bill - (total_bill*0.15)
elif total_bill>=5000 and total_bill<10000:
	total_bill = total_bill - (total_bill*0.10)
else:
	total_bill = total_bill

discounted_price = total_bill

gst= discounted_price*0.10

final_bill = discounted_price + gst

ask = input("Do you want carry bag yes/no? ").lower()

if ask == "yes":
    bag = "yes"
    total_bill = total_bill + 10
else:
    bag = "no"

if cust_gender=="female":
    gift="Cadeberry"

if cust_gender=="male":
    gift="Lather Wallet"



print("\t\t\tDmart")
print(f"name: {cust_name}")
print("------------------------------------------------------------------")

print(" item name\tquantity\tprice\ttotal\tafter-discount")

print(f" {item1}\t\t{item1_quantity}\t\t{item1_price}\t{item1_total_price}\t{item1_total_price_discount}")

print(f" {item2}\t\t{item2_quantity}\t\t{item2_price}\t{item2_total_price}\t{item2_total_price}")

print(f" {item3}\t\t{item3_quantity}\t\t{item3_price}\t{item3_total_price}\t{item3_total_price}")

print(f" {item4}\t\t{item4_quantity}\t\t{item4_price}\t{item4_total_price}\t{item4_total_price}")

print(f" {item5}\t\t{item5_quantity}\t\t{item5_price}\t{item5_total_price}\t{item5_total_price_discount}")

print(f" {item6}\t\t{item6_quantity}\t\t{item6_price}\t{item6_total_price}\t{item6_total_price}")

print(f" {item7}\t\t{item7_quantity}\t\t{item7_price}\t{item7_total_price}\t{item7_total_price}")

print(f" {item8}\t\t{item8_quantity}\t\t{item8_price}\t{item8_total_price}\t{item8_total_price}")

print(f" {item9}\t\t{item9_quantity}\t\t{item9_price}\t{item9_total_price}\t{item9_total_price}")

print(f" {item10}\t\t{item10_quantity}\t\t{item10_price}\t{item10_total_price}\t{item10_total_price_discount}")

print("------------------------------------------------------------------")

print("\t\t\t\t\tA.P\tD.P")
print(f"\t\t\t\t\t{final_bill}\t{discounted_price}")

print(f"Gift :- {gift}\t\t\t0.00\t 0.00 ")
print("\n")
print(f"Carry Bag : {bag} \t\t\t\t10.00\t10.00")
print(f"GST (10%)\t\t\t\t{gst}")

print("------------------------------------------------------------------")

print(f"\t\t\t\t\t{final_bill+gst}\t{discounted_price+gst}")
print("\n")
print("\t\t\t Thank You")
print("\t\t\t To Vist")
print("\t\t\t D-Mart ")

print("------------------------------------------------------------------")

