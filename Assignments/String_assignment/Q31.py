# 31. Find the longest substring without repeating characters.
# Example: "abcabcbb" → 3 ("abc")

s="abcabcbb"
s=list(s)
result={}
index=1
for i in range(len(s)-1):
    if ord(s[i])==ord(s[i+1])-1:
        result[index]=[]
    else:
        result[index].append(s[i])
    
print(result)
