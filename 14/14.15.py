# https://openfipi.devinf.ru/task/DE4AE1
for x in range(1, 2031):
    a = 7**170 + 7**100 - x
    k = 0

    while a > 0:
        if a % 7 == 0:
            k += 1
        a //= 7

    if k == 73:
        print(x)