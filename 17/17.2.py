# https://openfipi.devinf.ru/task/E89C8A

a = [int(x) for x in open('17.2.txt')]

lst = []
mn = min([x for x in a if x > 0 and x % 110 == 0])

for i in range(len(a) - 1):
    if (a[i] + a[i+1]) < mn:
        lst.append(a[i] + a[i+1])

print(len(lst), max(lst))
