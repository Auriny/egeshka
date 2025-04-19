s = open('24.2.txt').readline()
lst = []
c = 0

for i in range(len(s) - 1):
    if s[i] == s[i+1]:
        lst.append(c)
        c = 1
    else:
        c += 1
        print(s[i], s[i + 1])

print(max(lst))