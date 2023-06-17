# Написать программу, которая в качестве входных данных принимает список кортежей,
# представляющих IP-адреса, и возвращает список уникальных сетевых адресов.адресов

import ipaddress

def get_network_addresses(ip_addresses):
    network_addresses = set()
    for ip_address in ip_addresses:
        network_address = str(ipaddress.ip_network(ip_address[0]+'/'+str(ip_address[1]), strict=False))
        network_addresses.add(network_address)
    return list(network_addresses)

ip_addresses_v1 = [('192.168.0.1', 24), ('10.0.0.1', 16), ('192.168.0.2', 24), ('192.168.1.1', 24), ('10.0.0.1', 16)]
ip_addresses_v2 = [('192.168.0.1', 24), ('10.0.0.1', 16), ('192.168.0.2', 24), ('192.168.3.1', 24), ('10.0.0.1', 17)]

network_addresses = get_network_addresses(ip_addresses_v1)
print(network_addresses)

network_addresses = get_network_addresses(ip_addresses_v2)
print(network_addresses)
