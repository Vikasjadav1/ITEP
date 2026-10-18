# 21. Find the most frequent character in a string.

s="programmming"
result={}
max=0
ans=''
for char in s:
    if char in result:
        result[char]=result[char]+1
    else:
        result[char]=1


for key in result.keys():
    if result[key]>max:
        max=result[key]
        ans=key

print(f"most frequent character : {ans}")