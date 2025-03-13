# https://vimbox.skyeng.ru/kids/computer-science/room/kegahegorini?homework=true
def f(a, b, m):
    if not a + b < 102:
        return m % 2 == 0
    if m == 0:
        return 0
    h = [f(a + 1, b, m - 1), f(a, b + 1, m - 1), f(a * 2, b, m - 1), f(a, b * 3, m - 1)]
    return any(h) if m % 2 != 0 else all(h)

print('19)', [s for s in range(101 + 1) if f(s, 24, 2)])
print('20)', [s for s in range(101 + 1) if not f(s, 24, 1) and f(s, 24, 3)])
print('21)', [s for s in range(101 + 1) if not f(s, 24, 2) and f(s, 24, 4)])