b = [B for B in range(30, 95)]
lst = []


def f(x):
    return (x % a == 0) or ((x in b) <= (not x % 30 == 0))


for a in range(1, 1000):
    if all(f(x) for x in range(1, 1000)):
        lst.append(a)

print(len(lst))
