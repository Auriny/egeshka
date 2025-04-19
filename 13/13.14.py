# https://prnt.sc/_OOAVBOKyTwX

from ipaddress import *

for mask in range(33):  # 0-32. IPv4 э [/0; /32], т.е. 32 бита (4 байта). делаем перебор битов
    net = ip_network(f'{ip_address("111.61.106.21")}/{mask}', False)  # False = 0, заменяет strict=False. можно просто 0 впиндюрить
    if ip_address('111.61.95.0') in net:
        print(mask, net.netmask)  # mask в данном случае - число, net.netmask - сама маска

