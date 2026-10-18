# 33. Check whether a string has balanced parentheses.[Stack]
# Example: "{[()]}" → True, "([)]" → False

s="{[()]}"

st=0
end=len(s)-1
check=True
while(st<end):
    if (s[st]=='{' and s[end]=='}') or (s[st]=='(' and s[end]==')') or (s[st]=='[' and s[end]==']'):
        st+=1
        end-=1
    else:
        check=False
        break

if check:
    print("string has balanced parentheses")
else:
    print("string has not balanced parentheses")
