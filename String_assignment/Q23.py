# Reverse the order of words in a sentence.
# Example: "Python is easy" → "easy is Python"

s="Python is easy"
ans=""
s=s.split()
left=0
right=len(s)-1

while(left<right):
    s[left],s[right]=s[right],s[left]
    left+=1
    right-=1

s=" ".join(s)
print(s)

    


