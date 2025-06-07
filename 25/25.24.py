from fnmatch import fnmatch

lst = []
for x in range(738, 10**9, 738):
    if fnmatch(str(x), '???5?8?0'):
        lst.append([x, x//738])

print(len(lst))