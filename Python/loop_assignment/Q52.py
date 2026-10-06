# 52) WAP to find out all the Armstrong numbers between two entered numbers

a=int(input("enter a : "))
b=int(input("enter b : "))

for i in range(a,b+1): 
    lastnumber=0
    ans=0
    temp=i
    while(i>0):
         lastnumber=i%10
         ans+=lastnumber**3
         i=i//10
    if(temp==ans):
        print(f"Armstrong numbers between {a} and {b} : {temp}")  