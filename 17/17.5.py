# https://openfipi.devinf.ru/task/655816

a = [int(x) for x in open('17.5.txt')]

lst = []
k = len([x for x in a if x % 32 == 0])

for i in range(len(a) - 1):
    if (a[i] < 0 or a[i + 1] < 0) and (a[i] + a[i + 1] < k):
        lst.append(a[i] + a[i+1])

print(len(lst), max(lst))