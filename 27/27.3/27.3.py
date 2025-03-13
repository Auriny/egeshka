# Найди количество пар чисел, сумма которых кратна 115
f = open("27_1000.txt")
N = 1000

a = [int(x) for x in f]
count = 0

for i in range(N):
    for j in range(i + 1, N):
        if (a[j] + a[i]) % 115 == 0:
            count += 1
            print(count)
