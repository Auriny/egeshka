# https://prnt.sc/XSGy8XPSQzLm

def f(a, m):
    if a >= 128:
        return m % 2 == 0
    if m == 0:
        return 0
    h = [f(a + 2, m - 1), f(a + 5, m - 1), f(a * 2, m - 1)]
    return any(h) if m % 2 != 0 else all(h)

print('19)', [s for s in range(1, 127) if f(s, 2)])
print('20)', [s for s in range(1, 127) if not f(s, 1) and f(s, 3)])
print('21)', [s for s in range(1, 127) if not f(s, 2) and f(s, 4)])