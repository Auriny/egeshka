def f(x, y):
    return ((x < 10) <= ((x ** 2 + 3) < a)) and (((y ** 2) <= a) <= (y <= 20))

c = 0

for a in range(1, 300):
    if all(f(x, y) for x in range(1, 300) for y in range(1, 300)):
        c += 1

print(c)
