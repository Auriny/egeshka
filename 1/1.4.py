from itertools import *

a = '247 148 578 126 38 47 136 235'.split()
s = 'BH BA AH AE EG EC GC GF HF FD DC'.split()

print('1 2 3 4 5 6 7 8')
for p in permutations('ABCDEFGH'):
    if all([str(p.index(x) + 1) in a[p.index(y)] for x, y in s]):
        print(*p)