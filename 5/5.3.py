def f(n):
    a = bin(n)[2:]
    for x in range(2):
        s = sum([int(x) for x in list(a)])
        a += str(s % 2)

    return int(a, 2)


lst = []

for b in range(15000):
    if f(b) > 75:
        lst.append(f(b))

print(min(lst))
