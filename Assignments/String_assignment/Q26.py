#  Find the longest word in a sentence.

s="Find the longest word in a sentence"
result={}
s=s.split()
max=0
ans=""
for word in s:
        result[word]=len(word)

for i in result.keys():
    if result[i]>max:
        max=result[i]
        ans=i

print(f"longest word in a sentence : {ans}")

