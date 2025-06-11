# https://openfipi.devinf.ru/task/DD7C72

def f(x, y):
    if x > y:
        return 0
    if x == y:
        return 1
    return f(x + 1, y) + f(x + 2, y) + f(x * 2, y)

a = f(4, 11) * f(11, 13) * f(13, 15)

print(a)

