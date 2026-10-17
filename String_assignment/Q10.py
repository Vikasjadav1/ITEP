#Replace every space with a hyphen (-).

s = "InfoBeans-Foundation"
'''
s=s.replace("-"," ")
print(s)'''

s=list(s)

for char in s:
    if char=="-":
        char=" "
s="".join(s)
print(s)