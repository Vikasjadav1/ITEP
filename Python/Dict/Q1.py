#  s="aaabbccc" ---> a4b3c2 like
   
s="aaabbccc"
result={}
for ch in s:
    if ch in result:
        result[ch]=result[ch]+1
    else:
        result[ch]=1

print(result)
