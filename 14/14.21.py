# https://openfipi.devinf.ru/task/217C79

from string import *

for x in printable[:19]:
    a = int(f'98{x}79731', 19) + int(f'36{x}14', 19)

    if a % 18 == 0:
        print(x, a // 18)