# 21900 kompege.ru

for x in range(2301, 1, -1):
    a = 7 ** 350 + 7 ** 150 - x
    k = 0

    while a > 0:
        if a % 7 == 0:
            k += 1
        a //= 7

    if k == 200:
        print(x)
        break