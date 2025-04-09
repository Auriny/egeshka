# https://openfipi.devinf.ru/task/2AC0B5

def f(x, y):
    return ((x + 2 * y) < a) or (y > x) or (x > 60)

for a in range(1, 300):
    if all(f(x, y) == 1 for x in range(1, 300) for y in range(1, 300)):
        print(a)
        break