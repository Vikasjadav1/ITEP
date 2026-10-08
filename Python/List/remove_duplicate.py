'''
arr=[0,0,1,1,1,2,2,3]
pos=1
count=1
cnt=1
for i in range(1,len(arr)-1):
    if arr[i]==arr[i+1] or arr[i]==arr[i-1]:
        cnt+=1
    else:
        cnt=1
    if cnt>1 and arr[i]!=arr[i+1]:
        arr[pos]=arr[i+1]
        pos+=1
        count+=1

print(arr[:count])
'''

arr=[0,0,1,1,1,2,2,3]
arr=list(set(arr))

print(arr)

