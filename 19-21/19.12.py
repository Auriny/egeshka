# https://prnt.sc/lKCUCH0qG5oG
# ЗАДАЧА С ОТНИМАНИЕМ А НЕ ПРИБАВЛЕНИЕМ
# Вряд ли будет на ЕГЭ, но пусть будет
# UPD 11.06.2025: попалась >w<

def f(a, m):
    if a <= 87:
        return m % 2 == 0
    if m == 0:
        return 0
    h = [f(a - 2, m - 1), f(a // 2, m - 1)]
    return any(h) if m % 2 != 0 else all(h)

print('19)', [s for s in range(88, 1000) if f(s, 2)])
print('20)', [s for s in range(88, 1000) if not f(s, 1) and f(s, 3)])
print('21)', [s for s in range(88, 1000) if not f(s, 2) and f(s, 4)])
