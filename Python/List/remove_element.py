element=int(input("enter element : "))

arr=[1,6,3,2,5]
rem=[]

for i in range(len(arr)):
    if arr[i]!=element:
        rem.append(arr[i])

print(rem)