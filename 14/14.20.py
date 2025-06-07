# https://openfipi.devinf.ru/task/5BFD7A
from string import printable

for x in printable[:22]:
    a = int(f'98{x}79641', 22) + int(f'36{x}14', 22) + int(f'73{x}4', 22)

    if a % 21 == 0:
        print(x, a // 21)