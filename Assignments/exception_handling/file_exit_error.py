try:
    file = open("test.txt", "x")
    file.write("Hello")

except FileExistsError:
    print("File already exists!")