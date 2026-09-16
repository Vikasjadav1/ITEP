# 1	2	2	4	8	32	…… n terms

n=int(input("enter number : "))

first=1
second=2
i=1

while(i<=n):
    print(first, end=" ")
    next=first*second
    first=second
    second=next
    i=i+1

