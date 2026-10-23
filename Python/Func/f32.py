import time

def decorator(func):
    def wrapper():
        start=time.perf_counter()
        func()
        end=time.perf_counter()
        print(f"execution time : {end-start}")
    return wrapper


@decorator
def calculation_10000():
    total=sum(range(10000))
    print("10000 calculation done")

@decorator
def calculation_100000():
    total=sum(range(100000))
    print("100000 calculation done")

calculation_10000()
calculation_100000()