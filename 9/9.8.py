f = open('9.8.txt')
c = 0

for s in f:
    lst = [int(x) for x in s.split()]

    for x in lst:
        if lst.count(x) == 2:
            if ((x * 2) * 2) >= (sum(lst) - (x * 2)):
                c += 1

print(c)
