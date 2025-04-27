# https://openfipi.devinf.ru/task/B93319

def f(x, y):
    if x < y:
        return 0
    if x == y:
        return 1
    return f(x - 2, y) + f(x // 2, y)

print(f(30, 12) * f(12, 1))