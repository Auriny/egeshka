max_count = 0

for n in range(1, 2025):
    s = '3' * 24 + '1' * n

    while '33' in s or '11111111' in s:
        if '33' in s:
            s = s.replace('33', '111', 1)
        else:
            s = s.replace('11111111', '5', 1)

    max_count = max(max_count, s.count('5'))

print(max_count)
