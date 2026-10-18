#peak element

arr=[5,6,7,5,9,10]

if len(arr)==1 or (arr[len(arr)-1] > arr[len(arr)-2]):
    print("1")
else:
    for i in range(len(arr)-1):
       if i==0 and arr[i]>arr[i+1]:
           print("1")
       if arr[i-1]<arr[i]>arr[i+1]:
           print("1")

    else:
        print("0")


