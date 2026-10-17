# Reverse every word without changing the word order.
# Example: "Python is easy" → "nohtyP si ysae"

s="Python is easy"
s=s.split()

for i in range(len(s)):
    st=0
    end = len(s[i]) - 1
    word=list(s[i])
    while(st<end):
        word[st],word[end]=word[end],word[st]
        st+=1
        end-=1
    
    s[i]="".join(word)

s=" ".join(s)
print(s)

