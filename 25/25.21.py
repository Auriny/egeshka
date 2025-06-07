def s(x):
    dels = []
    for i in range(1, x // 2 + 1):
        if x % i == 0:
            dels.append(i)
        if x // 2 in dels:
            dels.append(x)
    return sorted(dels)

k = 0
for x in range(501_200, 10000000):
    R = sum(s(x))
    if R % 10 == 3:
        print(x, R)
        k += 1
    if k == 5:
        break
