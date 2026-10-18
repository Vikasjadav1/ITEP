#6. Find the length of a string without using len()

def func(s):
    length=0

    for char in s:
        if char:
            length+=1

    print(length)

s="infobeans"
func(s)