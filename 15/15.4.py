F = list(range(6, 37))
h = list(range(32, 9, -1))  # или range(10, 33)
a = []

for x in range(1, 100000):
    f = not(x in F) and not(x in h) or (x in a)
    if not f:
        a.append(x)

print(len(a) - 1)
