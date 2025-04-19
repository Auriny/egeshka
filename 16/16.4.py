# https://openfipi.devinf.ru/task/1A2ED5
from sys import setrecursionlimit


def f(n):
    if n == 1:
        return 1
    if n > 1:
        return 2 * n * f(n - 1)

setrecursionlimit(3000)

a = (f(2024) - 3 * f(2023)) // f(2022)
print(a)