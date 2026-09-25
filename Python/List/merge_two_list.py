arr1=[1,2,5,6,9]
arr2=[1,3,5,8,8,8,9,9]

i=0
j=0
result=[]

while(i<len(arr1) and j<len(arr2)):
    if arr1[i]<arr2[j]:
        result.append(arr1[i])
        i+=1
    else:
        result.append(arr2[j])
        j+=1

while(i<len(arr1)):
    result.append(arr1[i])
    i+=1

while(j<len(arr2)):
    result.append(arr2[j])
    j=j+1


print(result)

    
    