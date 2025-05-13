# https://prnt.sc/vpl8LYu-IMRY

st = open('24.12.txt').readline()

lst = []

for i in range(len(st) - 1):
    if i[i + 1] % 6 == 0:
        lst.append(lst[i] + lst[i + 1])

print(max(lst) + 1)
