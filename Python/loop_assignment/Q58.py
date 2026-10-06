#58) WAP to convert decimal number into binary number without using array

n=int(input("enter number  : "))

ans=0
pow=1
while(n>0):
    reminder=n%2
    n=n//2
    ans+=(reminder*pow)
    pow=pow*10


print(f"binary:{ans}")
    