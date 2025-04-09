# https://openfipi.devinf.ru/task/2EE07F

b = [B for B in range(50, 71)]


def f(x):
    return (x % a == 0) or ((x in b) <= (not (x % 15 == 0)))

for a in range(1, 300):
    if all(f(x) for x in range(1, 300)):
        print(a)