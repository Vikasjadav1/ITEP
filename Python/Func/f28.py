def f1(callback):
    print("F1-called..")
    print(callback)
    callback()

def f2():
    print("F2-called...")


f1(f2) 