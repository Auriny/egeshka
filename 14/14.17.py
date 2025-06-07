# https://openfipi.devinf.ru/task/412BA2
from string import printable

for x in printable[:19]:
    a1 = int(f'98{x}79731', 19)
    a2 = int(f'36{x}14', 19)
    a3 = int(f'73{x}4', 19)

    if (a1 + a2 + a3) % 18 == 0:
        print(x, (a1 + a2 + a3) // 18)
        break