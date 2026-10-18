#8. Remove all spaces from a string.

def func(s):
    s=list(s)
    result=""
    for char in s:
        if char==" ":
            continue
        else:
            result+=char

    print(result)

s="vik k a s"
func(s)
