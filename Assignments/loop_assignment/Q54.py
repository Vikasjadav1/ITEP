# 54) WAP to print all the even numbers between two entered numbers

a=int(input("enter a : "))
b=int(input("enter b : "))

for i in range(a,b+1): 
    if(i%2==0):
        print(i)