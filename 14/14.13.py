for x in range(1, 2031):
    a = 3 ** 100 - x
    k = 0

    while a > 0:
        if a % 3 == 0:
            k += 1
        a //= 3

    if k == 1:
        print(x)