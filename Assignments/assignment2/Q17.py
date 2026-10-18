salary=int(input("enter salary : "))

if salary<=10000:
    hra=salary*0.20
    da=salary*0.80
    Gross=salary+hra+da
    print(f"gross {Gross}")
elif salary<=20000:
    hra=salary*0.25
    da=salary*0.90
    Gross=salary+hra+da
    print(f"gross {Gross}") 
else:
    hra=salary*0.30
    da=salary*0.95
    Gross=salary+hra+da
    print(f"gross {Gross}") 

     