k = list(range(20, 62))
u = list(range(37, 82))
lst = []

for x in range(1, 1000):
    check = (not(x in a) <= (x in u) or not(x in k))
    if not check:
        lst.append(x)
print(len(lst) - 1)