def f(x, y):
    return (x % a == 0) or ((x in b) <= (x % 20 != 0))
b = list(range(50, 65 + 1))
for a in range(1, 500):
    if all(f(x, y) for x in range(1, 500) for y in range(1, 500)):
        print(a)