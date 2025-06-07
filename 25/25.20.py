# https://openfipi.devinf.ru/task/3A7D63
from fnmatch import fnmatch

for x in range(1991, 10**8, 1991):
    if fnmatch(str(x), '2*1?71'):
        print(x, x//1991)