# https://openfipi.devinf.ru/task/ED5E0C

def f(a, b, m):
    if a + b >= 65:
        return m % 2 == 0
    if m == 0:
        return 0
    h = [f(a + 1, b, m - 1), f(a, b + 1, m - 1), f(a * 3, b, m - 1), f(a, b * 3, m - 1)]
    return any(h) if m % 2 != 0 else all(h)

print("19)", [s for s in range(59) if f(6, s, 2)]) # тут надо all сверху в конце поменять на any
print("20)", [s for s in range(59) if not f(6, s, 1) and f(6, s, 3)])
print("21)", [s for s in range(59) if not f(6, s, 2) and f(6, s, 4)])