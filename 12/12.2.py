s = 45 * '8'
while '1111' in s or '8888' in s:
    if '1111' in s:
        s = s.replace('1111', '88')
    else:
        s = s.replace('8888', '11')
print(s)