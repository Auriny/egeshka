# https://openfipi.devinf.ru/task/6EA065

a = [int(x) for x in open('17.3.txt')]

lst = []
mn = min(a)

for i in range(len(a) - 1):
    if a[i] % 16 == mn or a[i+1] % 16 == mn:
        lst.append(a[i] + a[i+1])

print(len(lst), max(lst))