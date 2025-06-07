lst = []

for x in range(2031, 1, -1):
    a = 7**170 + 7*100 - x
    k0 = 0

    while a > 0:
        if x % 7 == 0:
            k0 += 1
        a //= 7

    lst.append(k0)

print(max(lst))
