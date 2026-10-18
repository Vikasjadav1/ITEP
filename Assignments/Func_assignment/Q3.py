#3. Count the number of vowels and consonants in a string.

def func(s):
    vowel=0
    consonant=0
    l=['a','e','i','o','u','A','E','I','O','U']
    for char in s:
        if char in l:
            vowel+=1
        else:
            consonant+=1

    print(f"vowel {vowel}")
    print(f"consonant {consonant}")

s="infobeans"
func(s)