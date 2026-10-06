# 49) WAP to find out all the perfect numbers between two entered numbers

a=int(input("enter a : "))
b=int(input("enter b : "))

for i in range(a,b+1): 
    sum=0
    for j in range(1,i):
        if(i%j==0):
            sum+=j
    if i==sum:
        print(i)
        