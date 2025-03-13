f = open("27_B_1000.txt")
a = [int(x) for x in f]
# сколько различных остатков
ost = [0] * 3
col_par_cr_2 = 0
for i in range(len(a)):
    # куда распределить число
    # a[i] % 2 — адрес куда положить
    print(a[i], a[i] % 3, ost, col_par_cr_2)
    col_par_cr_2 = col_par_cr_2 + ost[a[i] % 3]
    ost[a[i] % 3] = ost[a[i] % 3] + 1
    print(a[i], a[i] % 3, ost, col_par_cr_2)
print(col_par_cr_2)