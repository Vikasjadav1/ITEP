l=[1,2,3,4,5]

target=int(input("enter target :"))

for i in range(len(l)):
     if target==l[i]:
         print(f"element found at index : {i}")
         break
else:
    print(f"element is not found")
