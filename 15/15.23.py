# https://openfipi.devinf.ru/task/9992AA

def f(x, y):
    return ((3 * x + 2 * y) > a) or (y < x) or (x < 10)

for a in range(1, 300):
    if all(f(x, y) for x in range(1, 300) for y in range(1, 300)):
        print(a)
