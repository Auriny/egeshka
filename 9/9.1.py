# Открой файл электронной таблицы, содержащей в каждой строке пять натуральных чисел.

# Задание 9
# Определи количество строк таблицы, содержащих числа, для которых выполнены оба условия:
#
# в строке все числа различны;
# утроенная сумма максимального и минимального чисел строки не больше удвоенной суммы оставшихся трёх её чисел.
# В ответе запиши только число.

f = open('9.1.txt')
count = 0
for stroka in f:
    spisok = stroka.split()
    spisok_chisel = [int(x) for x in spisok]
    razl_chisla = [x for x in spisok_chisel if spisok_chisel.count(x) == 1]
    print(razl_chisla)
    if len(razl_chisla) == 5:
        sort_spisok = sorted(razl_chisla)
        utr_sum_max_min = (max(sort_spisok) + min(sort_spisok)) * 3
        utr_sum_ost = (sort_spisok[1] + sort_spisok[2] + sort_spisok[3]) * 2
        if not utr_sum_max_min > utr_sum_ost:
            count += 1
print(count)
