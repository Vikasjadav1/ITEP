#28. P is one-dimensional array of integers. Write a Java program search for a data VAL from P. If VAL is present in the array then “element found ” otherwise “element not found” should be displayed.

arr=[1,2,3,4,5,6,7,8,9]

target=int(input("enter target : "))

for i in range(len(arr)):
    if target==arr[i]:
        print("element found")
        break
else:
   print("element not found")