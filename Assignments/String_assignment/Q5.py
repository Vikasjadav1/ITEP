#Count the number of words in a sentence.

s="infobeans foundation indore"

word=0
for char in s:
    if char==" ":
        word+=1

print(word)

'''s=s.split()
print(len(s))'''