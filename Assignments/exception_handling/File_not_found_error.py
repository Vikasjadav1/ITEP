try:
    file = open("abc.txt", "r")
    print(file.read())
except FileNotFoundError:
    print("File not found!")