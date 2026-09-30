#Find the first repeating element in array of integers

arr = [10, 5, 3, 4, 3, 5, 6]

found=False

for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]==arr[j]:
            found=True
            break
    if found:
        print(f"first repeating element {arr[i]} at index {i}")
        break
    
    