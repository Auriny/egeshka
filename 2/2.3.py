from itertools import permutations, product


def f(x, y, z, w):
    return ((not w) or y) and (((not x) or z) == ((not y) or x))

for x1, x2, x3, x4 in product([0, 1], repeat=4):
    t = (
        (x1, 1, x3, 0, 1),
        (0, x2, 1, x4, 1),
        (0, 1, 0, 1, 1),
    )

    if len(t) == len(set(t)):
        for p in permutations('xyzw', r=4):
            if all(f(**dict(zip(p, line))) == line[-1] for line in t):
                print(*p)
