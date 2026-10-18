#Remove all digits from a string.
s="st8ri5ng99"

def func(s):
    result=""
    for char in s:
        if not char.isdigit():
            result+=char


    print(result)

func(s)
