n=int(input("enter number in binary  : "))

ans=0
pow=1 #2^0 

while(n>0):
    last=n%10
    n=n//10
    ans+=(last*pow)
    pow=pow*2


print(f"binary:{ans}")
    