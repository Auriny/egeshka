# https://prnt.sc/M0N9bSbY8RUQ

a = [int(x) for x in open('17.7.txt')]
s_otr = sum(x for x in a if x < 0)

lst = []

for i in range(len(a) - 2):
    tr = a[i:i+3]
    if max(tr) * min(tr) > s_otr:
        lst.append(sum(tr))

print(len(lst), abs(max(lst)))


# или так:

a = [int(x) for x in open('17.7.txt')]
s_otr = sum(x for x in a if x < 0)

lst = []

for x, y, z in zip(a, a[1:], a[2:]):
    if max(x, y, z) * min(x, y, z) > s_otr:
        lst.append(x + y + z)

print(len(lst), abs(max(lst)))