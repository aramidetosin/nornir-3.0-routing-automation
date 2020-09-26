from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_netmiko import netmiko_send_config
from nornir.core.task import Task, Result
import ipaddress


def hello_world(task: Task):
    host = task.host
    result = f"{task.host.name} says Hello World!!"
    return result


def no_ospf_config(task):
    pass


def ospf_config(task):
    ospf_cms = ['router ospf 1']
    nw_advertised = task.host['nw_advertised']
    id = task.host['id']
    ospf_cm = f"router-id {id}.{id}.{id}.{id}"
    ospf_cms.append(ospf_cm)
    for k, v in nw_advertised.items():
        for value in v:
            nw = ipaddress.ip_network(value)
            ospf_cm = f"network {nw.network_address} {nw.hostmask} area {k}"
            ospf_cms.append(ospf_cm)
    task.run(netmiko_send_config, config_commands=ospf_cms)


def main():
    nr = InitNornir(config_file="../../config.yaml")
    # result = nr.run(task=hello_world)
    result = nr.run(task=ospf_config)
    print_result(result)


if __name__ == "__main__":
    main()
