from itertools import *

a = '256 134 267 27 16 135 34'.split()
s = 'AF FB FE EC ED AB BD DG GC'.split()

print('1 2 3 4 5 6 7')
for p in permutations('ABCDEFG'):
    if all([str(p.index(x) + 1) in a[p.index(y)] for x, y in s]):
        print(*p)
