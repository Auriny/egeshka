# https://prnt.sc/K9v8lKYRyi5y

def f(x):
    return ((x % 5 != 0) <= (x % 8 == 0)) or (x + a >= 33)

for a in range(1, 1000):
    if all(f(x) == 1 for x in range(1, 1000)):
        print(a)
        break