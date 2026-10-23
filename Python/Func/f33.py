def decorator(func):
    def wrapper(x,y):
        result=func(x*x,y*y)
        return result
    return wrapper

@decorator
def add(a,b):
    return a+b

result=add(2,2)
print(result)