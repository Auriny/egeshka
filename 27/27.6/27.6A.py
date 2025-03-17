f = open("27-A.txt")
N = 2000

a = [int(x) for x in f]
count = 0

for i in range(N):
    for j in range(i + 1, N):
        summ = a[i] + a[j]
        ost = a[i] % 13 + a[j] % 13
        if abs(summ - ost) == 3:
            count += 1
print(count)
