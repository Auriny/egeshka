from fnmatch import *

k = 0
for x in range(1, 10**6 + 1):
    if fnmatch(str(x), '5**??5'):
        if x % 625 == 0:
            k += 1
            print(x, k)