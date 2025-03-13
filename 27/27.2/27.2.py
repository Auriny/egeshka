# https://vimbox.skyeng.ru/kids/computer-science/room/giduvebupiho 17 карточка
f = open("27_A_1000.txt")
N = 100  # можно заменить на len(a)
a = [int(x) for x in range(100)]

max_summa = 0
count = 0

for i in range(0, N):
    for j in range(i + 1, N):
        summa = a[i] + a[j]
        if summa % 2 == 0:
            if (a[i] % 17 == 0) or (a[j] % 17 == 0):
                max_summa = max(max_summa, summa)
                count += 1
                print(a[i], a[j], max_summa, count)
