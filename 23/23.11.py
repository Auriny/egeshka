# https://prnt.sc/pLh3_hMp2Mtg

def f(x, y):
    if x > 51 or x == 35:
        return 0
    if x == y:
        return 1
    return f(x + 1, y) + f(x + 2, y) + f(x * 2, y)

a = f(7, 13) * f(13, 15) * f(15, 51)

print(a)