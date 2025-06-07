#https://openfipi.devinf.ru/task/1F31B9
from string import *

for x in printable[:19]:
    a = int(f'78{x}79643', 19) + int(f'25{x}43', 19) + int(f'63{x}5', 19)

    if a % 18 == 0:
        print(x, a)