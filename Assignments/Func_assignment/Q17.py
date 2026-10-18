# 17. Find the first non-repeating character in a string.
# Example: "aabbcddee" → c

s="aabbcddeie"

def func(s):
    result={}

    for char in s:    
        if char in result:
            result[char]=result[char]+1
        else:
            result[char]=1
    
    print(result)

    for key in result.keys():
        if result[key]==1:
            print(f"fist non-repeating character in a string :{key}")
            break

func(s)