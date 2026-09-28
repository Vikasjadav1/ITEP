#Q.2 Find minimum and maximum element in array

arr=[5,2,-3,6,4]

min_val=float('inf')
max_val=float('-inf')

for i in range(len(arr)):
    if arr[i]<min_val:
        min_val=arr[i]

    if arr[i]>max_val:
        max_val=arr[i]

    

print(f"minimum value : {min_val}")
print(f"maximum value : {max_val}")


min=arr[0]
max=arr[0]

for i in arr:
    if(i<min):
        min=i
    
    if(i>max):
        max=i

print(min)
print(max)


        