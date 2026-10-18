#Replace every space with a hyphen (-).


'''
s=s.replace("-"," ")
print(s)'''



def func(s):
    s=list(s)

    for i in range(len(s)):
        if s[i] == "-":
            s[i] = " "
    s="".join(s)
    print(s)

s = "InfoBeans-Foundation"
func(s)