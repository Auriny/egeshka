# 21413 kompege.ru
from string import printable

for x in printable[:21]:
    a1 = int(f'82934{x}2', 21)
    a2 = int(f'2924{x}{x}7', 21)
    a3 = int(f'67564{x}8', 21)

    if (a1 + a2 + a3) % 20 == 0:
        print(x, (a1 + a2 + a3) // 20)
