#1. Write a program to reverse a string without using slicing ([::-1]).
s="infobeans"
s=list(s)
st=0
end=len(s)-1
ans=""

while(st<end):
    s[st],s[end]=s[end],s[st]
    st+=1
    end-=1
    ans="".join(s)


'''
j=""
for i in s:
    j=i+j

print(j)
'''

print(ans)