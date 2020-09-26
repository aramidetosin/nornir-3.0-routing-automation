"""
nw_advertised is defined in hosts.yaml as a dictionary of OSPF area keys,
and list of networks to be advertised in each OSPF area as values.
Each OSPF area will advertised some networks.
For example: R7
nw_advertised: {"0": ["192.1.67.0/24", "7.0.0.0/8"], "10": ["192.1.78.0/24"]}
R7 will advertise 2 networks in area 0: ["192.1.67.0/24", "7.0.0.0/8"];
and 1 network in area 10: ["192.1.78.0/24"]
"""

from nornir import InitNornir
import ipaddress

nr = InitNornir(config_file="./../../config.yaml")
print(f"Hosts: {nr.inventory.hosts}")
print(f"Hosts: {nr.inventory.groups}")
print(f"Hosts of group AREA 0: {nr.inventory.children_of_group('area0')}")
print(f"Hosts of group AREA 10: {nr.inventory.children_of_group('area10')}")

print("network Advertised of router R6: ", nr.inventory.hosts["R6"]["nw_advertised"])


for k,v in nr.inventory.hosts["R6"]["nw_advertised"].items():
    # print(f"{k}: {v}")
    for value in v:
        print(f"Area is {k}: {value}")
        nw = ipaddress.ip_network(value)
        # print(nw.network_address, nw.hostmask)
        print(f"network {nw.network_address} {nw.hostmask} area {k}")

print("-"*95)
print("network Advertised of router R7: ", nr.inventory.hosts["R7"]["nw_advertised"])
for k,v in nr.inventory.hosts["R7"]["nw_advertised"].items():
    for value in v:
        print(f"Area is {k}: {value}")
        nw = ipaddress.ip_network(value)
        print(f"network {nw.network_address} {nw.hostmask} area {k}")