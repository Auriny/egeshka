from ipaddress import *

k = 0
for ip in ip_network('192.160.80.25/255.255.252.0', 0):
    k += 1

print(k - 15)