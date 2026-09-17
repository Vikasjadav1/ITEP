x=int(input("enter  a number x : "))
y=int(input("enter  a number y : "))

result=1

for _ in range(y):
    result*=x

print(f"x^y : {result}")
