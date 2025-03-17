def f(a, b, m):
    if not a + b < 118:
        return m % 2 == 0
    if m == 0:
        return 0
    h = [f(a + 1, b, m - 1), f(a, b + 1, m - 1), f(a, b + 4, m - 1), f(a, b + 4, m - 1), f(a * 3, b, m - 1), f(a, b * 3, m - 1)]
    return any(h) if m % 2 != 0 else all(h)

print('19)', [s for s in range(118) if f(10, s, 2)])
print('20)', [s for s in range(118) if not f(10, s, 1) and f(10, s, 3)])
print('21)', [s for s in range(118) if not f(10, s, 2) and f(10, s, 4)])