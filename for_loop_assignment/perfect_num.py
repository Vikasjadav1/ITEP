n=int(input("enter  a number : "))
sum=0
for i in range(1,n):
    if n%i==0:
        sum+=i

if n==sum:
    print("perfect")
else:
    print("not perfect")