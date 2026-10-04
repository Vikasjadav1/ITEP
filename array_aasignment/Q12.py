'''
Find common elements in three sorted arrays.
Given three arrays sorted in increasing order. Find the elements that are common in all three arrays.
Note: can you take care of the duplicates without using any additional Data Structure?
Example 1:
Input:
n1 = 6; A = {1, 5, 10, 20, 40, 80}
n2 = 5; B = {6, 7, 20, 80, 100}
n3 = 8; C = {3, 4, 15, 20, 30, 70, 80, 120}
Output: 20 80
Explanation: 20 and 80 are the only
common elements in A, B and C.
'''

'''
A=[1, 5, 10, 20, 40, 80]
B=[6, 7, 20, 80, 100]
C=[3, 4, 15, 20, 30, 70, 80, 120]

for i in range(len(A)):
    for j in range(len(B)):
        if A[i]==B[j]:
            for k in range(len(C)):
                if A[i]==C[k]:
                    print(A[i])
'''
'''
A=[1, 5, 10, 20, 40, 80]
B=[6, 7, 20, 80, 100]
C=[3, 4, 15, 20, 30, 70, 80, 120]
D=[]

for x in A:
   if x in B and x in C:
       D.append(x)

print(D)
'''

arr1=[1, 5, 10, 20, 40, 80]
arr2=[6, 7, 20, 80, 100]
arr3=[3, 4, 15, 20, 30, 70, 80, 120]
ans=[]

i=0
j=0
k=0

while(i<len(arr1) and j<len(arr2) and k<len(arr3)):
    if arr1[i]==arr2[j]==arr3[k]:
        ans.append(arr1[i])
        i+=1
        j+=1
        k+=1
    elif(arr1[i]<arr2[j]):
        i+=1
    elif(arr2[j]<arr3[k]):
        j+=1
    else:
        k+=1

print(ans)

            
          
                
  
    