# https://openfipi.devinf.ru/task/2A7489

def f(x, y):
    return ((y + 2 * x) < a) or (x > 25) or (y > 25)

for a in range(1, 300):
    if all(f(x, y) == 1 for x in range(1, 300) for y in range(1, 300)):
        print(a)
        break
