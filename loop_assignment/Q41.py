a=int(input("enter  a : "))
b=int(input("enter  b : "))

while(a>0 and b>0):
    if(a>b):
        a=a%b
    else:
        b=b%a

if(a==0):
    print(f"HCF : {b}")
else:
    print(f"HCF : {a}")
