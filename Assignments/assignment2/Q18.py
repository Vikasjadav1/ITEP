units=int(input("enter electricity unit : "))

if units<=50:
    bill = (50 * 0.50) + ((units - 50) * 0.75)
elif units <= 150:
    bill = (50 * 0.50) + ((units - 50) * 0.75)
elif units <= 250:
    bill = (50 * 0.50)+(100 * 0.75)+((units - 150)*1.20)
else:
    bill =(50 * 0.50)+(100 * 0.75)+(100 * 1.20)+((units - 250)*1.50)

surcharge = bill * 0.20
total_bill = bill + surcharge
print("Electricity Bill:", bill)
print("Surcharge (20%):", surcharge)
print("Total Electricity Bill:", total_bill)