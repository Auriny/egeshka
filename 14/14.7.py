# 21709 kompege

lst = []

for x in range(1, 3001):
    a = (4 ** 210) + (4 ** 110) - x
    k = 0
    while a > 0:
        if a % 4 == 0:
            k += 1
        a //= 4
        # ???