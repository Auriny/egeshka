from itertools import *

a = '234 157 147 138 268 58 23 456'.split()
s = 'BD DG GA GF FH FA EH CH DE BE BC'.split()

print('1 2 3 4 5 6 7 8')
for p in permutations('ABCDEFGH'):
    if all([str(p.index(x) + 1) in a[p.index(y)] for x,y in s]):
        print(*p)