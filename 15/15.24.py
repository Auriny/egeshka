# https://openfipi.devinf.ru/task/C38156

def f(x, y):
    return ((y + 3 * x) > a) or (x < 30) or (y < 30)

for a in range(1, 300):
    if all(f(x, y) for x in range(1, 300) for y in range(1, 300)):
        print(a)