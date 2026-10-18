# 22. Find the second most frequent character.

# 21. Find the most frequent character in a string.

s="pccrogrammming"
result={}
max=0
second=0
ans=''
for char in s:
    if char in result:
        result[char]=result[char]+
    else:
        result[char]=1


for key in result.keys():
    if result[key]>max:
        max=result[key]

for key in result.keys():
    if result[key]<max and result[key]>second:
        second=result[key]
        ans=key


print(f"most frequent character : {ans}")