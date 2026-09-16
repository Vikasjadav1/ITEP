# WAP to check whether entered number is prime or not.

n=int(input("enter N : "))
i=1
count=0

while(i<=n):
    if(n%i==0):
        count+=1
    i=i+1

if(count==2):
    print("number is prime")
else:
    print("number is not prime")

