'''
Q.7 Sub array with given sum
Given an unsorted array A of size N that contains only non-negative integers, find a continuous sub-array which adds to a given number S.

Example 1:
Input:
N = 5, S = 12
A[] = {1,2,3,7,5}
Output: 2 4
Explanation: The sum of elements 
from 2nd position to 4th position 
is 12.
'''
arr=[1,2,3,7,5]
target=12
left=0
cursum=0

for i in range(len(arr)):
    cursum=cursum+arr[i]
    while(cursum>target):
        cursum-=arr[left]
        left+=1

    if cursum==target:
        print(left+1,i+1)
        break
   