# https://openfipi.devinf.ru/task/4F6198
from fnmatch import fnmatch

for x in range(273, 10**8, 273):
    if fnmatch(str(x), '12??15*6'):
        print(x, x//273)