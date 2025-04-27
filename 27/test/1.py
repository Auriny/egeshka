# https://prnt.sc/pWc9ubr_ebgd

lst = [x for x in range(1, 20000)]
c = 0

for i in range(len(lst)):
    for j in range(i+1, len(lst)):
        if (lst[i] + lst[j]) % 4 == 0:
            c += 1

print(c)