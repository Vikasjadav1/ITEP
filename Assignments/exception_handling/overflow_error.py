try:
    import math
    print(math.exp(1000))
except OverflowError:
    print("Number is too large!")