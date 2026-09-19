# 50) WAP to find out all the palindrome numbers between two entered numbers


a=int(input("enter a : "))
b=int(input("enter b : "))

for i in range(a,b+1): 
    lastnumber=0
    reverse=0
    temp=i
    while(i>0):
         lastnumber=i%10
         reverse=reverse*10+lastnumber
         i=i//10
    if(temp==reverse):
        print(temp)
    