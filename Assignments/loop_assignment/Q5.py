# WAP to find out the factorial of a number.

n=int(input("enter N : "))
fact=1

while(n!=0):
    fact=fact*n
    n=n-1

print(f"factorial of a number {fact}")

