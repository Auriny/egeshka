# https://prnt.sc/x2ihQk9D1hli

def f(x, y):
    if x == y:
        return 1
    if x < y or x == 25:
        return 0

    return f(x - 5, y) + f(x - 10, y) + f(x / 5, y)

print(f(125, 55) * f(55, 5))