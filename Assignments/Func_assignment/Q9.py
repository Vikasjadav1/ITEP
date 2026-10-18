#9. Find the first and last character of a string.

def func(s):
    s=list(s)

    print(f"first character : {s[0]}")
    print(f"last character : {s[len(s)-1]}")

s="infobeans"
func(s)

