# https://prnt.sc/ET3UYMiOdQNn

def f(n):
    if n < 3:
        return 1
    if n > 2:
        if n % 2 == 0:
            return f(n - 1) + 2 * n - 1
        else:
            return f(n - 2) + 2 * n

a = f(21) - f(19)
print(a)