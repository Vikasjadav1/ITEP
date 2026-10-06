import tokenize
from io import BytesIO

code = b"x = 10 + 20"

for token in tokenize.tokenize(BytesIO(code).readline):
    print(token)