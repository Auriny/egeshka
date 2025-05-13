# https://prnt.sc/QfoNl30PDPlD

a = [int(x) for x in open('17.8.txt')]
mn = min(x for x in a if x % 103 == 0)

lst = []

for x, y in zip(a, a[1:]):
    if ((x + y) % 2) == 0 and abs(x - y) % mn == 0:
        lst.append(x + y)

print(len(lst), max(lst))