# https://prnt.sc/gfbUMvaxX0aV

def per(x, s):
    otv = ''
    while x > 0:
        otv = str(x % s) + otv
        x = x // 9
    return otv

for x in range(1, 5509 + 1):
    if per(9 ** 127 - x, 9).count('5') == 1:
        print(x)