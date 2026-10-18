# 47) WAP to print tables of all the numbers between two entered numbers

a=int(input("enter a : "))
b=int(input("enter b : "))


for i in range(a,b+1):
    for j in range(1,11):
        print(f"{i} * {j} = {i*j}")
    print()

