# https://openfipi.devinf.ru/task/AAAAAA

def f(x, y):
    if x > 17 or x == 12:  # если не содержит N, просто x == N делаем и меняем < на >
        return 0
    if x == y:
        return 1
    return f(x + 1, y) + f(x + 2, y) + f(x * 2, y)

a = f(2, 9) * f(9, 17)

print(a)