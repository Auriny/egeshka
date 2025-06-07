def search(x):
    dels = []
    for i in range(2, x // 2 + 1):
        if x % i == 0:
            dels.append(i)
    return sorted(dels)

for x in range(214361, 214381):
    if len(search(x)) == 4:
        print(*search(x))