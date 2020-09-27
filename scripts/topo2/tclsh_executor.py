from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_netmiko import netmiko_send_config


def main():

    commands = [
        "tclsh",
        "foreach address {172.16.100.238} {ping $address}",
        "exit"
    ]

    print(f"Initialising Nornir Instance...")

    nr = InitNornir(config_file="../../config-topo2.yaml")

    print(f"Running Task....")

    result = nr.run(
        task = netmiko_send_config,
        config_commands = commands,
        enter_config_mode = False,
    )

    print_result(result)

    print(f"Script job completed!!!!")

if __name__ == '__main__':
    main()