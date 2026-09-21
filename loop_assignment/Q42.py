#42) WAP to find out HCF of a number

a=int(input("enter  a : "))
b=int(input("enter  b : "))

org_a=a
org_b=b

while(a>0 and b>0):
    if(a>b):
        a=a%b
    else:
        b=b%a

if(a==0):
    hcf=b
else:
    hcf=a

lcm=(org_a*org_b)/hcf
print(f"lcm : {lcm}")
