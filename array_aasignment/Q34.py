#34. Write a java program to implement linear search


arr=[1,2,3,4,5,6,7,8,9]

target=int(input("enter target : "))

for i in range(len(arr)):
    if arr[i]==target:
        print(f"target found at index : {i}")
        break
else:
    print("target not found")
    