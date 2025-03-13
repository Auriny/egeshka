# Откройте файл электронной таблицы, содержащей в каждой строке шесть натуральных чисел.
# Определите количество строк таблицы, содержащих числа, для которых выполнены оба условия:
# – в строке только одно число повторяется трижды, остальные числа различны;
# – квадрат суммы всех повторяющихся чисел строки больше квадрата суммы всех её неповторяющихся чисел.
# В ответе запишите только число.

f = open("9.5.txt")
count = 0

repeated = []
unique = []

for stroka in f:
    spisok = list(map(int, stroka.split()))
    for x in spisok:
        if spisok.count(x) == 3 and x not in repeated:
            repeated.append(x)
        elif spisok.count(x) == 1:
            unique.append(x)

        if len(repeated) == 1 and len(unique) == 3:
            if (sum(repeated) * 3) ** 2 > (sum(unique)) ** 2:
                count += 1

print(count)
