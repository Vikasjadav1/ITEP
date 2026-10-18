
s = "pccrogrammming"

def func(s):
    result = {}
    max = 0
    second = 0
    ans = ""

    for char in s:
        if char in result:
            result[char] += 1
        else:
            result[char] = 1

    for key in result.keys():
        if result[key] > max:
            max = result[key]

    for key in result.keys():
        if result[key] < max and result[key] > second:
            second = result[key]
            ans = key

    print(f"Second most frequent character: {ans}")
    print(f"Frequency: {second}")

func(s)
