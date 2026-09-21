n=int(input("enter  a number : "))
temp=n
ans=0
length=0

while n!=0:
    length+=1
    n = n//10

n = temp 
while n!=0:
    lastnumber=n%10
    ans=ans+lastnumber**length
    n=n//10


if temp==ans:
    print("its armstrong")
else:
    print("its not armstrong")
 