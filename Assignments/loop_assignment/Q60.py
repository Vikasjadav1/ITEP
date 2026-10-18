# 60) WAP to print Square, Cube and Square Root of all numbers from 1 to N

n=int(input("enter number  : "))

for i in range(1,n+1):
    square=i**2
    cube=i**3
    root=i**0.5
    print(f"square of {i} : {square} , cube of {i} : {cube}  , root of {i} : {root}")