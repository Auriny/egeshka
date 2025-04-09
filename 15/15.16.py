# https://openfipi.devinf.ru/task/D5D16C

p = [P for P in range(17, 59)]
q = [Q for Q in range(29, 81)]
a = []


def f(x):
    return (x in p) <= (((x in q) and not(x in a)) <= (not(x in p)))

for x in range(1, 1000):
    if not f(x):
        a.append(x)

print(len(a) - 1)