# Открой файл электронной таблицы, содержащей в каждой строке пять натуральных чисел.
#
# .txt
# Задание 9
# Определи количество строк таблицы, содержащих числа, для которых выполнены оба условия:
#
# в строке все числа различны;
# разность максимального и минимального чисел строки больше суммы оставшихся трёх её чисел.
# В ответе запиши только число.

f = open("9.2.txt")
count = 0
for stroka in f:
    spisok = stroka.split()
    int_spisok = [int(x) for x in spisok]
    razl_spisok = [x for x in int_spisok if int_spisok.count(x) == 1]
    if len(razl_spisok) == 5:
        sort_list = sorted(razl_spisok)
        min_max = max(sort_list) - min(sort_list)
        ost = sort_list[1] + sort_list[2] + sort_list[3]
        if min_max > ost:
            count += 1
print(count)
