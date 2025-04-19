# https://openfipi.devinf.ru/task/ACD638

def f(x, y):
    if (x > y) or (x != 10):
        return 0
    if x == y:
        return 1
    return f(x - 1, y) + f(x // 2, y)

print(f(32, 1))