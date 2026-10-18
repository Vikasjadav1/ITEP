# 28. Check whether one string is a rotation of another.
# Example: "abcd" and "cdab" → True

s1="abcd"
s2="cdab"


def func(s1,s2):
    if len(s1)==len(s2) and s2 in (s1+s2):
        print(True)
    else:
        print(False)

func(s1,s2)
