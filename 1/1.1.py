# https://prnt.sc/pBLyzQTYIhCb
from itertools import permutations

a = '26 147 456 237 37 13 245'.split()
s = 'BD DE EF FG FC EA AC CG GB'.split()

for p in permutations('ABCDEFG'):
    if all([str(p.index(x) + 1) in a[p.index(y)] for x, y in s]):
        print(*p)