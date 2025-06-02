from ipaddress import *

for mask in range(33):
    net = ip_network('111.61.106.21/' + str(mask), 0)
    print(net, net.netmask, 32 - mask)

