def f(N):
    bn = bin(N)

    bn += str(bn.count('1') % 2)
    bn += str(bn.count('1') % 2)

    return bn

for n in range(1, 10000):
    if int(f(n), 2) > 123:
        print(int(f(n), 2))
        break