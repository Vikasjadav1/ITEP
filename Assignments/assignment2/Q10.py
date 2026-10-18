year=int(input("enter a year : "))

if(year%400==0 or (year%4==0 and year%100!=0)):
    print("leaf year")
else:
    print("not leaf year")