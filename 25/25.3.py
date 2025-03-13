# Напиши программу, которая ищет среди целых чисел, принадлежащих числовому отрезку
# [128034; 128065] число, имеющее максимальное количество различных натуральных делителей.
# Выведи это число и количество его делителей через пробел.

def search_del(x):
    div_list = [1, x]
    for div in range(2, x // 2 + 1):
        if x % div == 0:
            div_list.append(div)
    return div_list

                # +1 важно ставить
count_max_div = 0
samo_chislo = 0
for x in range(128034, 128065 + 1):
    if len(search_del(x)) >= count_max_div:
        count_max_div = len(search_del(x))
        samo_chislo = x
print(count_max_div, samo_chislo)