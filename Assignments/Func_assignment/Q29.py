# 29. Remove a particular character from a string without using replace().

s="particular"


def func(s):
    character="p"
    result=""

    for char in s:
        if char==character:
            continue
        else:
            result+=char

    print(result)

func(s)




