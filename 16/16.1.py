def f(n):
    if n >= 1000:
        return n
    else:
        return n * 2 + f(n + 2)

print(f(30) - f(20))
