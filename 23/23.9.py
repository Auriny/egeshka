# https://openfipi.devinf.ru/task/6CF4FF

def f(x, y):
    if x < y:
        return 0
    if x == y:
        return 1
    return f(x - 2, y) + f(x // 2, y)

print(f(36, 8) * f(8, 2))