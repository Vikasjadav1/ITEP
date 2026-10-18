# 48) WAP to find out the factors of all the numbers between two entered numbers

a=int(input("enter a : "))
b=int(input("enter b : "))


for i in range(a,b+1):
    for j in range(1,i+1):
        if(i%j==0):
            print(f"factors of {i} : {j}")
    print()