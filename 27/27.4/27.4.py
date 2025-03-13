# Найди количество пар чисел, произведение которых кратно 120
f = open("27_1000.txt")
N = 1000

a = [int(x) for x in f]
count = 0

for i in range(N):
    for j in range(i + 1, N):
        if (a[i] * a[j]) % 120 == 0:
            count += 1
print(count)
