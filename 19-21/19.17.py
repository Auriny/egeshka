# https://prnt.sc/gzh7NcSxf1EY

def f(a, b, m):
    if a + b >= 200:
        return m % 2 == 0
    if m == 0:
        return 0
    h = [f(a + 3, b, m - 1), f(a, b + 3, m - 1), f(a * 4, b, m - 1), f(a, b * 2, m - 1)]
    return any(h) if m % 2 != 0 else all(h)

print('19)', [s for s in range(100) if f(15, s, 2)])
print('20)', [s for s in range(100) if not f(15, s, 1) and f(15, s, 3)])
print('21)', [s for s in range(100) if not f(15, s, 2) and f(15, s, 4)])