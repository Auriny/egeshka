# https://openfipi.devinf.ru/task/0808A0

b = [x for x in range(60, 81)]


def f(x):
    return (x % a == 0) or ((x in b) <= (x % 22 != 0))


for a in range(1, 1000):
    if all(f(x) == 1 for x in range(1, 1000)):
        print(a)
