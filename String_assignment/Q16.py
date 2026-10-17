# 16. Check whether two strings are anagrams.
# Example: "listen" and "silent" → True

s1="listen"
s2="silent"

result1={}
result2={}
check=True

if len(s1)!=len(s2):
    check=False
else:
    for char in s1:
        if char in result1:
            result1[char]=result1[char]+1
        else:
            result1[char]=1
    for char in s2:
        if char in result2:
            result2[char]=result2[char]+1
        else:
            result2[char]=1
    
    if result1!=result2:
        check=False

if check:
    print("strings are anagrams")
else:
    print("strings are not anagrams")
