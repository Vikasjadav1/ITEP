'''
  import sys
    sys.exit(0) ---> raise SystemExit()

  import os
    os._exit(0)  --> It doesn't raise SystemExit() error
'''

import sys

print("at the start")
try:
    sys.exit(0)
except SystemExit as e:
    print("exception caught....")

print("at the end...")