# https://openfipi.devinf.ru/task/1E71A4

def f(x, y):
    return (x >= 12) or ((3 * x) < y) or ((x * y) < a)

for a in range(0, 2000):
    if all(f(x, y) for x in range(0, 2000) for y in range(0, 2000)):
        print(a)
        break
