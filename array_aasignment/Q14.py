'''
Q.14. Find the first non-repeating elment in given array of integers
Find the first non-repeating element in a given array arr of N integers.
Note: Array consists of only positive and negative integers and not zero.
Example 1:
Input : arr[] = {-1, 2, -1, 3, 2}
Output : 3
Explanation:
-1 and 2 are repeating whereas 3 is 
the only number occuring once.
Hence, the output is 3.

Example 2:
Input : arr[] = {1, 1, 1}
Output : 0
'''

arr = [-1, 2, -1, 3, 2]


for i in range(len(arr)):
    found=False
    for j in range(len(arr)):
        if i!=j and arr[i]==arr[j]:
            found=True
    if found==False:
        print(f"first non repeating element {arr[i]} at index {i}")
        break
