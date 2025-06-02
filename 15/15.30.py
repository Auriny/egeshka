# https://prnt.sc/Rl27EC0TzLhQ

def f(x):
    return (a < 30) and (x % a != 0 <= (x % 11 == 0 <= x % 9 != 9))


for a in range(1000, 0, -1):
    if all(f(x) for x in range(1, 1000)):
        print(a)
        break
