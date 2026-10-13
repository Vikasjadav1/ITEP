'''
Find the first non-repeating character in a string using a dictionary.
'''
s="hheelloo"
result={}
for char in s:
    if char in result:
        result[char]=result[char]+1
    else:
        result[char]=1

for key in result.keys():
    if result[key]==1:
        print(f"first non-repeating character in a string: {key}")
        break
else:
       print(f"there is no non-repeating character in a string:")
