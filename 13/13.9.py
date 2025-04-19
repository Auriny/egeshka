# https://openfipi.devinf.ru/task/B75086

from ipaddress import *

c = 0

for ip in ip_network("172.16.168.0/255.255.248.0"):
    if bin(int(ip))[2:].count('1') % 3 != 0:
        c += 1

print(c)