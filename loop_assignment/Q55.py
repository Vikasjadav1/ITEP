# 55) WAP to print all the odd numbers between two entered numbers

a=int(input("enter a : "))
b=int(input("enter b : "))

for i in range(a,b+1): 
    if(i%2!=0):
        print(i)