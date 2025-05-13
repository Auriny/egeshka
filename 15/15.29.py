def f(x, y, z):
    return ((2 * x + y) != 136) or ((z * y) < 100) or ((a ** 2) >= x + y)

for a in range(1, 100):
    if all(f(x, y, z) for x in range(1, 100) for y in range(1, 100) for z in range(1, 100)):
        print(a)
        break