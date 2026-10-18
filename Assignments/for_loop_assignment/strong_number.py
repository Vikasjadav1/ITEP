n=int(input("enter  a number : "))
temp=n
lastnumber=0
ans=0
while n!=0:
    lastnumber=n%10
    fact=1
    for i in range(1,lastnumber+1):
        fact*=i
    ans=ans+fact
    n=n//10

if temp==ans:
    print("strong number")
else:
    print("not a strong number ")
    
