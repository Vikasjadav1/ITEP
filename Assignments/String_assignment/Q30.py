# 0. Find the longest common prefix among a list of strings.
# Example: ["flower", "flow", "flight"] → "fl"

s=["flower", "flow", "flight"]
prefix=""

for i in range(len(s[0])):
    char=s[0][i]

    for word in s:
        if i<=len(word):
           if word[i]!=char:
            print(prefix)
            exit()
        else:
            print(prefix)
            exit()

    prefix+=char

print(prefix)


