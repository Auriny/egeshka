# https://openfipi.devinf.ru/task/9C8813

a = [int(x) for x in open('17.6.txt')]
mn = min(a)

lst = []

for i in range(len(a) - 1):
    if (a[i] % 18 + a[i + 1] % 18) == mn:
        lst.append(a[i] + a[i + 1])

print(len(lst), max(lst))