# https://openfipi.devinf.ru/task/62CE57
for x in range(1, 2031):
    a = 5**150 + 5**100 - x
    k = 0

    while a > 0:
        if a % 5 == 0:
            k += 1
        a //= 5

    if k == 50:
        print(x)