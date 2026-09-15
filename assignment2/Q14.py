percantage=int(input("enter percentage : "))

if percantage>90:
    print("grade A")
elif percantage>80 and percantage<=90:
    print("grade B")
elif percantage>=60 and percantage<=80:
    print("grade c")
else:
    print("grade d")