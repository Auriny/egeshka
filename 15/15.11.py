# https://prnt.sc/W25nGnbyLh7f

def f(x, y):
    return ((x + 2 * y) < a) or (y > x) or (x > 80)

for a in range(1, 300):
    if all(f(x, y) for x in range(1, 300) for y in range(1, 300)):
        print(a)
        break
