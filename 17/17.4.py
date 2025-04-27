# https://openfipi.devinf.ru/task/42A7D2

a = [int(x) for x in open('17.4.txt')]

mn = min(x for x in a if x % 19 == 0)
lst = []

for i in range(len(a) - 1):
    if a[i] % mn == 0 or a[i + 1] % mn == 0:
        lst.append(a[i] + a[i+1])

print(len(lst), max(lst))