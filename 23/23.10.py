# https://openfipi.devinf.ru/task/0B1894

def f(x, y):
    if x > y or x == 9:
        return 0
    if x == y:
        return 1
    return f(x + 2, y) + f(x + 3, y) + f(x * 2, y)

a = f(3, 15) * f(15, 25)

print(a)