# https://prnt.sc/35Q8y-h1j5rB

st = open('24.8.txt').readline()
gl_lett = 'AO'
lst = []
c = 1

for i in range(len(st) - 1):
    if (st[i] in gl_lett) + (st[i + 1] in gl_lett) == 1:
        c += 1
    else:
        lst.append(c)
        c = 1
print(max(lst))
