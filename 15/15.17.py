# https://openfipi.devinf.ru/task/B3B99C

p = [x for x in range(15, 41)]
q = [x for x in range(21, 64)]
a = []


def f(x):
    return (x in p) <= (((x in q) and not(x in a)) <= (not(x in p)))

for x in range(1, 300):
    if not f(x):
        a.append(x)

print(len(a) - 1)