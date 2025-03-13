# Напиши программу, которая ищет среди целых чисел, принадлежащих числовому отрезку
# [150017; 150090] числа, имеющие ровно 12 различных натуральных делителей, кратных 2.
# Выведи все числа в порядке возрастания через пробел.

def even_divisors_count(n):
    count = 0
    for d in range(2, n + 1, 2):
        if n % d == 0:
            count += 1
        if count > 12:
            return count
    return count

for x in range(150017, 150091):
    if even_divisors_count(x) == 12:
        print(x)

