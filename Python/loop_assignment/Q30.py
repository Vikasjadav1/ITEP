#30)   

#29) 1	11	111	1111	  11111	……

n=int(input("enter a number : "))

ans=0
for i in range(1,n+1):
    ans=ans*10+1
    if i == n:
        print(ans, end="")
    else:
        print(ans, end=" + ")