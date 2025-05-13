from itertools import product

c = 0

for s in product('0123456', repeat=6):
    s = ''.join(s)
    s1 = s.replace('0', 'ч').replace('2', 'ч').replace('4', 'ч').replace('6', 'ч') \
        .replace('1', 'н').replace('3', 'н').replace('5', 'н')
    if (s[0] != '0') and (s.count('6') == 1) and ('чч' not in s1) and ('нн' not in s1):
        c += 1

print(c)
