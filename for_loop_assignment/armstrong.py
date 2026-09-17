n=int(input("enter  a number : "))
temp=n
ans=0
while n!=0:
    lastnumber=n%10
    cube=lastnumber**3
    ans+=cube
    n=n//10

if temp==ans:
    print("its armstrong")
else:
    print("its not armstrong")
 