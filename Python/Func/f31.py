def decorator(func):
    def wrapper():
        print("before")
        func()
        print("after")
    return wrapper


@decorator
def say_hello():
    print("hello")

say_hello()