# 34. Compress a string by counting consecutive repeated characters.
# Example: "aaabbccccd" → "a3b2c4d1"

s="aaabbccccd"

def func(s):
    result={}
    ans=""
    for char in s:
        if char in result:
            result[char]=result[char]+1
        else:
            result[char]=1
    
    for key in result.keys():
        ans+=key
        ans+=str(result[key])
    print(ans)

func(s)