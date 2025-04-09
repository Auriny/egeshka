# https://openfipi.devinf.ru/task/CD8ED0

def f(x):
    return ((x % 2 == 0) <= (x % 5 != 0)) or (x + a >= 70)

for a in range(1, 300):
    if all(f(x) for x in range(1, 300)):
        print(a)
        break