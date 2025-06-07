# https://openfipi.devinf.ru/task/304763

def search(x):
    dels = []
    for i in range(1, x + 1):
        if x % i == 0:
            dels.append(i)
    return dels

lst = []
for x in range(500_000, 1_000_000_000):
    R = sum(search(x))
    if R % 10 == 6:
        lst.append([x, R])

    if len(lst) == 5:
        break

for x in lst:
    print(*x)