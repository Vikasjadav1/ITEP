'''
Longest consecutive sequence.
Given an array of positive integers. Find the length of the longest sub-sequence such that elements in the subsequence are consecutive integers, the consecutive numbers can be in any order.
 
Example 1:
Input:
N = 7
a[] = {2,6,1,9,4,5,3}
Output:
6
Explanation:
The consecutive numbers here
are 1, 2, 3, 4, 5, 6. These 6 
numbers form the longest consecutive
subsquence.
Example 2:
Input:
N = 7
a[] = {1,9,3,10,4,20,2}
Output:
4
Explanation:
1, 2, 3, 4 is the longest
consecutive subsequence.
'''

a=[2,6,1,9,4,5,3]
count=1
max_count=1
for i in range(len(a)-1):
    for j in range(i+1,len(a)):
        if a[i]>a[j]:
            a[i],a[j]=a[j],a[i]
        
for i in range(1,len(a)):
    if a[i]==a[i-1]+1:
        count+=1
    else:
        count=1
       
    if count>max_count:
        max_count=count

print(max_count)





       


    
    

