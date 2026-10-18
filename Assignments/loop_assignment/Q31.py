# 31) 9	99	999	9999	  99999 …….

n=int(input("enter a number : "))

ans=0
for i in range(1,n+1):
    ans=ans*10+9
    print(ans, end=" ")