arr=[-1,0,3,4,5,9,12,12]
target=int(input("enter target : "))

count=0
for i in range(len(arr)):
    if target==arr[i]:
        count+=1

print(f"occurance of an {target} is : {count} ")