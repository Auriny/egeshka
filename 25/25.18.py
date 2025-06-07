from fnmatch import *

for x in range(2023, 10**8 +1, 2023):
    if fnmatch(str(x), '1*23?9'):
        print(x, x//2023)
