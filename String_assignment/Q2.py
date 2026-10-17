#2. Check whether a string is a palindrome.

s="A1 b@2 #c3 C# 3c2@b .1A"
s=s.lower()
st=0
end=len(s)-1
palindrome=True
while(st<end):
    while st<end and (not s[st].isalnum()):
        st+=1
    while st<end and (not s[end].isalnum()):
        end-=1

    if s[st]==s[end]:
        st+=1
        end-=1
    else:
        palindrome=False
        break

if palindrome:
    print("palindrome")
else:
    print("not palindrome")



'''
pal=False
while(st<end):
    if s[st]!=s[end]:
        pal=True
        break
    else:
        st+=1
        end-=1    
if pal:
    print("not palindrome")
else:
    print("palindrome")
    '''
    
