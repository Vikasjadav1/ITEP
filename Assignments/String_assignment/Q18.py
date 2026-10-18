# 18. Find the first repeating character.
# Example: "programming" → r

s="programming"

result={}

for char in s:
    if char in result:
        result[char]=result[char]+1
    else:
        result[char]=1
    
for key in result.keys():
    if result[key]==2:
        print(f"fist repeating character in a string :{key}")
        break
