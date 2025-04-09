# https://prnt.sc/aVhYrFg7PEiP

b = [x for x in range(90, 105 + 1)]


def f(x):
    return (x % a == 0) or ((x in b) <= (x % 25 != 0))


for a in range(1, 1000):
    if all(f(x) == 1 for x in range(1, 1000)):
        print(a)
