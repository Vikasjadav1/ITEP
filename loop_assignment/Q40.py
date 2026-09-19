#40) WAP to count no. Of even and odd digits in a number

n=int(input("enter  a number : "))

lastnumber=0
odd=0
even=0

while n!=0:
    lastnumber=n%10
    if(lastnumber%2==0):
        even+=1
    else:
        odd+=1
    n=n//10
    
print(f"even : {even}")
print(f"odd : {odd}")