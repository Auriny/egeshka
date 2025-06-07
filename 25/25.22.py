def dels(x):
    sp = [x]
    for i in range(1, x // 2 + 1):
        if x % i == 0:
            sp.append(i)

    return sorted(sp)

print(dels(20), sum(dels(20)))