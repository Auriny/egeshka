from fnmatch import fnmatch

for x in range(3023, 10**8, 3023):
    if fnmatch(str(x), "3?5*2?7"):
        print(x, x//3023)