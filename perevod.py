def con(n, syst):
    result = ''
    while n > 0:
        result = printable[n % syst] + result
        n //= syst
    return result
print(con(14, 2))  # 14->1110
