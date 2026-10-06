#  WAP to find out the factors of a number.

n=int(input("enter N : "))
i=1

while(i<=n):
    if(n%i==0):
        print(i)
    i=i+1