n=int(input("enter  a number : "))
temp=n
lastnumber=0
reverse=0
while n!=0:
    lastnumber=n%10
    reverse=reverse*10+lastnumber
    n=n//10
    
if temp==reverse:
    print("its palindrome")
else:
    print("its not palindrone")  