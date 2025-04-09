# https://openfipi.devinf.ru/task/46EF19

def f(x):
    return ((x % 2 == 0) <= (x % 5 != 0)) or (x + a >= 90)

for a in range(1, 300):
    if all(f(x) for x in range(1, 300)):
        print(a)
        break