#11. Count how many times a particular character occurs.


def func(s):
    result={}

    for char in s:
        if char in result:
            result[char]=result[char]+1
        else:
            result[char]=1
    
    print(result)

s="infobeans"
func(s)