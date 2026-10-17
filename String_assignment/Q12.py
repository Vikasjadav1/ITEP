# Check whether two strings are equal without using == for the complete strings.
s1="infobeans"
s2="infobeans"
s1=list(s1)
s2=list(s2)
check=True
if len(s1)!=len(s2):
        check = False
else:
    for i in range(len(s1)-1):
        if ord(s1[i])!=ord(s2[i]):
            check=False
            break

if check:
    print("strings are equal")
else:
    print("strings are not equal")


