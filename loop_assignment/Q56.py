#56) WAP to print factorial of all the numbers between two entered numbers

a=int(input("enter a : "))
b=int(input("enter b : "))

for i in range(a,b+1):  
    temp=i
    
    ans=0
    lastnumber=0
    while(i>0):
        lastnumber=i%10
        i=i//10
        fact=1
        for j in range(lastnumber,0,-1):
             fact=fact*j
        ans+=fact
    if temp==ans:
        print(temp)