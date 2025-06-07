#https://prnt.sc/orlH1Y8mYwTP

lst = []

for n in range(3, 10001):
    s = '7' + n * '8'

    while '78' in s or '688' in s or '8888' in s:
        s = s.replace('78', '8', 1)
        s = s.replace('688', '87', 1)
        s = s.replace('8888', '6', 1)

    a = [int(x) for x in s]
    if sum(a) == 44:
        lst.append(n)

print(min(lst))