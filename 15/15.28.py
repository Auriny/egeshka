# https://prnt.sc/AKeE38Akj3Zh

def f(x, y):
    return (5 < y) or (x > 32) or ((x + 2*y) < a)

for a in range(1, 5000):
    if all(f(x, y) for x in range(1, 500) for y in range(1, 500)):
        print(a)
        break