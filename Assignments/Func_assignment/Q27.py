# Find all duplicate characters and their frequencies.

s="vikasjadavfromratlam"

def func(s):
    result={}
    for char in s:
        if char in result:
            result[char]=result[char]+1
        else:
            result[char]=1

    for key in result.keys():
        if result[key]>1:
            print(f"{key} : {result[key]}")
        
func(s)
