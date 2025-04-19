# https://openfipi.devinf.ru/task/1D3C68

from ipaddress import *

c = 0

for ip in ip_network("172.16.96.0/255.255.224.0"):
    if bin(int(ip))[2:].count('1') % 3 == 0:
        c += 1

print(c)