# https://openfipi.devinf.ru/task/8271BC

def f(x, y):
    if x < y:
        return 0
    if x == y:
        return 1
    return f(x - 2, y) + f(x - 5, y)

print(f(32, 12))