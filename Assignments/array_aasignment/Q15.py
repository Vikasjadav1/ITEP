'''
Sub with equal 0s and 1s
Given an array containing 0s and 1s. Find the number of subarrays having equal number of 0s and 1s. 
Example 1:
Input:
n = 7
A[] = {1,0,0,1,0,1,1}
Output: 8
Explanation: The index range for the 8 
sub-arrays are: (0, 1), (2, 3), (0, 3), (3, 4), 
(4, 5) ,(2, 5), (0, 5), (1, 6)
Example 2:
Input:
n = 5
A[] = {1,1,1,1,0}
Output: 1
Explanation: The index range for the 
subarray is (3,4)
'''
arr = [1,0,0,1,0,1,1]

'''
for i in range(len(arr)-1):
    count0=0
    count1=0
    if arr[i]==0:
        count0+=1
    else:
        count1+=1
    for j in range(i+1,len(arr)):
        if arr[j]==0:
            count0+=1
        else:
            count1+=1
 
        if count0==count1:
            print(f"{i,j}")
'''
      
