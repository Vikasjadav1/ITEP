n=int(input("enter  a number : "))

lastnumber=0
sum=0
while n!=0:
    lastnumber=n%10
    sum+=lastnumber
    n=n//10
    

print(f"sum is {sum}")
 