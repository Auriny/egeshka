from ipaddress import *

for ip in ip_network('172.225.145.140/255.255.255.252'):
    print(ip)