# 53) WAP to print all the strong numbers between two entered numbers

a=int(input("enter a : "))
b=int(input("enter b : "))

for i in range(a,b+1): 
    fact=1
    for j in range(i,0,-1):
         fact*=j
         
    print(f"factorail of {i} : {fact}") 