# https://prnt.sc/Y_t9r9yRyF-y

from ipaddress import *
c = 0

for ip in ip_network('172.224.244.176/255.255.255.240'):
    if bin(int(ip))[2:].count('1') % 5 != 0:
        c += 1
        print(c, ip)
