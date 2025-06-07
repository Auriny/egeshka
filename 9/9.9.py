f = open('9.9.txt').readlines()
k = 0

for x in f:
    a = sorted([int(x) for x in x.split()])
    if max(a) < (sum(a) - max(a)) and len([s for s in a if a.count(s) == 2]) == 2:
        k += 1

print(k)