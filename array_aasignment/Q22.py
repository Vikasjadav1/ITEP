'''
Q.22) Java program to find nearest lesser and greater element in array
Given an array of N elements and we have to find nearest lesser and nearest greater element using C program.
Example:
    Input:
    Enter the number of elements for the arrray : 3  
 
    Enter the elements for array_1.. 
    array_1[0] : 1   
    array_1[1] : 2   
    array_1[2] : 3   
 
    Enter the number : 2 
 
    Output:
    Element lesser than 2 is : 1 
    Element greater than 2 is : 3
'''

size=int(input("Enter the number of elements for the arrray :"))
arr=[]
for i in range(size):
    arr.append(int(input("Enter the elements for arr : ")))

k=int(input(" Enter the number :"))

for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]>arr[j]:
            arr[i],arr[j]=arr[j],arr[i]

for i in range(size):
    if arr[i] == k:
        if arr[0]==k:
            print("no nearest lesser element")
            print(f"nearest greater  : {arr[i+1]}")
        elif arr[size-1]==k:
            print(f"nearest lesser  : {arr[i-1]}")
            print("no nearest greater element")
        else:
            print(f"nearest greater  : {arr[i+1]}")
            print(f"nearest lesser  : {arr[i-1]}")
    
    
    
    
    
