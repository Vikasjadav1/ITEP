# 61) WAP to find out all the leap years between two entered years

year1=int(input("enter year1 : "))
year2=int(input("enter year2 : "))

for i in range(year1,year2+1):
    if(i%400==0) or (i%4==0 and i%100!=0):
        print(f"leaf year : {i}")