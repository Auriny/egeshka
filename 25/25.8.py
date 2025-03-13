# Напиши программу, которая ищет среди целых чисел, принадлежащих числовому отрезку
# [42000; 42100] числа, имеющие ровно 20 различных натуральных делителей.
# Выведи эти числа в порядке возрастания через пробелы.

def search_del(x):
    div_list = [1, x]
    for div in range(2, x // 2 + 1):
        if x % div == 0:
            div_list.append(div)
    return div_list
    # +1 важно ставить

for x in range(42000, 42100 + 1):
    if len(search_del(x)) == 20:
        print(sorted(search_del(x)))
