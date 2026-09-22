ch = input("enter char : ")

match ch:
    case "a"|"e"|"i"|"o"|"u":
        print("vowel")
    case _:
        print("not vowel")