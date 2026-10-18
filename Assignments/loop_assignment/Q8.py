# WAP to print Fibonacci series.

n=int(input("enter N : "))
first=0
second=1
i=1
print(first)
print(second)
while(i<=n-2):
      next=first+second
      first=second
      second=next
      print(next)
      i=i+1