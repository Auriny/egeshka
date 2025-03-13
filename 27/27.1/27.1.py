f = open("27.1.txt")
N = 1000  # первое число из файла надо удалить, а переменная эта ваще не нужна
a = [int(x) for x in f]
count = 0
for i in range(0, len(a)):
    for j in range(i + 1, len(a)):
        if (a[i] + a[j]) % 228 == 0:
            count += 1
            print(count)