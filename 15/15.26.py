# https://openfipi.devinf.ru/task/0C2C4D

def f(x, y):
    return (x > a) or (y > a) or (y < (x - 2)) or (y > (2 * x - 10))

for a in range(1, 300):
    if all(f(x, y) for x in range(1, 300) for y in range(1, 300)):
        print(a)