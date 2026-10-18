#Count the number of words in a sentence.


def func(s):
    word=0
    for char in s:
        if char==" ":
            word+=1

    print(word)

s="infobeans foundation indore"
func(s)

'''s=s.split()
print(len(s))'''