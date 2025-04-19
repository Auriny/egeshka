from ipaddress import *

c = 0

for ip in ip_network('142.124.0.0/255.255.0.0'):
    if bin(int(ip))[2:].count('1') <= 18:
        c += 1
        print(c, ip)