#Suppose A, B, C are arrays of integers of size M, N, and M + N respectively. The numbers in array A appear in ascending order while the numbers in array B appear in descending order. Write a java progtam to produce third array C by merging arrays A and B in ascending order.

A=[1,2,4,5,9,10,14,48]
B=[9,8,7,6,5,4,3,2,1]
c=[]

i=0
j=0

st=0
end=len(B)-1
while(st<end):
    B[st],B[end]=B[end],B[st]
    st+=1
    end-=1


while(i<len(A) and j<len(B)):
    if A[i]<B[j]:
        c.append(A[i])
        i+=1
    else:
       c.append(B[j])
       j+=1

while(i<len(A)):
    c.append(A[i])
    i+=1

while(j<len(B)):
    c.append(B[j])
    j+=1

print(c)


