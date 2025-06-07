# https://openfipi.devinf.ru/task/D5D16C

p = [x for x in range(17, 59)]
q = [x for x in range(29, 80)]


def f(x):
    return (x in p) <= (((x in q) and (not (x in a))) <= (not (x in p)))


for a in range(1, 1000):
    if all(f(x) for x in range(1, 1000)):
        print(a)
        break
