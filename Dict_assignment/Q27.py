'''
27. Group words that are anagrams of one another.
    Example: ["eat", "tea", "bat", "ate"]
    Expected groups: ["eat", "tea", "ate"] and ["bat"]'''

words=["eat", "tea", "bat", "ate"]
d={}

for word in words:
    key="".join(sorted(word))

    if key not in d:
        d[key]=[]
    
    d[key].append(word)

print(list(d.values()))